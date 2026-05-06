import logging
import os
from datetime import datetime

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_http_methods

from capstone.models import CapstoneSubmission, CapstoneRubricScore, CapstoneStatus, RubricCategory
from content.models import Course
from core.decorators.roles import manager_required
from core.services.storage import StorageService
from documents.models import AuditLog
from enrollment.models import CourseEnrollment, EnrollmentStatus

logger = logging.getLogger(__name__)

_MAX_UPLOAD_BYTES = 25 * 1024 * 1024  # 25 MB
_ALLOWED_EXTENSIONS = {".docx"}
_RUBRIC_PASS_THRESHOLD = 3.5  # avg score out of 5.0 required to pass


# ─── trainee: submit capstone ─────────────────────────────────────────────────

@login_required
@require_http_methods(["GET", "POST"])
def submit_capstone(request: HttpRequest, course_slug: str) -> HttpResponse:
    course = get_object_or_404(Course, slug=course_slug, is_capstone=True, is_active=True)
    enrollment = CourseEnrollment.objects.filter(user=request.user, course=course).first()
    if not enrollment or enrollment.status not in (
        EnrollmentStatus.IN_PROGRESS, EnrollmentStatus.OPEN, EnrollmentStatus.PASSED
    ):
        raise PermissionDenied

    existing_submissions = CapstoneSubmission.objects.filter(
        user=request.user, course=course
    ).order_by("-submitted_at")

    if request.method == "POST":
        uploaded = request.FILES.get("capstone_file")

        if not uploaded:
            messages.error(request, "יש לבחור קובץ להגשה.")
            return redirect("capstone_submit", course_slug=course_slug)

        ext = os.path.splitext(uploaded.name)[1].lower()
        if ext not in _ALLOWED_EXTENSIONS:
            messages.error(request, "ניתן להגיש קבצי Word בלבד (.docx).")
            return redirect("capstone_submit", course_slug=course_slug)

        if uploaded.size > _MAX_UPLOAD_BYTES:
            messages.error(request, "גודל הקובץ חורג מהמקסימום המותר (25MB).")
            return redirect("capstone_submit", course_slug=course_slug)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        storage_key = f"capstone/{request.user.pk}/{course_slug}/{timestamp}.docx"

        try:
            storage = StorageService()
            storage.upload(
                file=uploaded,
                key=storage_key,
                content_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
            )
            file_url = storage.get_url(storage_key)
        except Exception as exc:
            logger.error("Capstone upload failed for user %s: %s", request.user.pk, exc)
            messages.error(request, "שגיאה בהעלאת הקובץ. נסה שוב.")
            return redirect("capstone_submit", course_slug=course_slug)

        submission = CapstoneSubmission.objects.create(
            user=request.user,
            course=course,
            file_url=file_url,
            file_key=storage_key,
        )

        AuditLog.objects.create(
            user=request.user,
            action="capstone_submitted",
            entity_type="CapstoneSubmission",
            entity_id=str(submission.pk),
            metadata_json={"course_slug": course_slug, "file_key": storage_key},
        )

        from core.services.email import EmailService
        EmailService.send_capstone_received(request.user)

        messages.success(request, "פרויקט הגמר הוגש בהצלחה! מנהל הלקוחות יבדוק אותו בהקדם.")
        return redirect("course_detail", course_slug=course_slug)

    return render(request, "capstone/submit.html", {
        "course": course,
        "existing_submissions": existing_submissions,
    })


# ─── manager: review capstone ─────────────────────────────────────────────────

@manager_required
@require_http_methods(["GET", "POST"])
def review_capstone(request: HttpRequest, pk: int) -> HttpResponse:
    submission = get_object_or_404(CapstoneSubmission, pk=pk)
    existing_scores = {s.category: s for s in submission.rubric_scores.all()}
    categories = [
        (cat.value, cat.label) for cat in RubricCategory
    ]

    if submission.status == CapstoneStatus.SUBMITTED:
        submission.begin_review(reviewer=request.user)
        submission.save()

    if request.method == "POST":
        scores = {}
        valid = True
        for cat_value, _ in categories:
            try:
                score = int(request.POST.get(f"score_{cat_value}", 0))
                if not (1 <= score <= 5):
                    raise ValueError
                scores[cat_value] = {
                    "score": score,
                    "comment": request.POST.get(f"comment_{cat_value}", "").strip(),
                }
            except (ValueError, TypeError):
                messages.error(request, f"ציון לא תקין עבור קריטריון {cat_value}. נדרש מספר בין 1 ל-5.")
                valid = False
                break

        if valid:
            for cat_value, data in scores.items():
                CapstoneRubricScore.objects.update_or_create(
                    submission=submission,
                    category=cat_value,
                    defaults={
                        "score": data["score"],
                        "comment_he": data["comment"],
                        "scored_by": request.user,
                    },
                )

            avg = sum(d["score"] for d in scores.values()) / len(scores)
            action = request.POST.get("action", "")

            if action == "pass" or (action == "auto" and avg >= _RUBRIC_PASS_THRESHOLD):
                submission.mark_passed(reviewer=request.user)
                submission.save()
                from core.services.email import EmailService
                EmailService.send_capstone_graded(submission.user, passed=True)
                messages.success(request, f"פרויקט הגמר של {submission.user.display_name} סומן כעבר (ממוצע: {avg:.1f}/5.0).")
            elif action == "fail" or (action == "auto" and avg < _RUBRIC_PASS_THRESHOLD):
                submission.mark_failed(reviewer=request.user)
                submission.save()
                from core.services.email import EmailService
                EmailService.send_capstone_graded(submission.user, passed=False)
                messages.success(request, f"פרויקט הגמר של {submission.user.display_name} סומן כנכשל (ממוצע: {avg:.1f}/5.0).")

            return redirect("capstone_inbox")

    return render(request, "capstone/review.html", {
        "submission": submission,
        "categories": categories,
        "existing_scores": existing_scores,
        "pass_threshold": _RUBRIC_PASS_THRESHOLD,
        "score_range": range(1, 6),
    })
