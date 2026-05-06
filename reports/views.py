from datetime import timedelta

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Avg, Count, Q
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from django.views.decorators.http import require_POST

from accounts.models import User, UserRole
from capstone.models import CapstoneSubmission, CapstoneStatus
from content.models import Course, Domain
from core.decorators.roles import manager_required, manager_or_ceo_required, ceo_required
from documents.models import AuditLog
from enrollment.models import (
    CourseEnrollment, EnrollmentStatus, ModuleProgress, UnlockRequest, UnlockRequestStatus,
)
from exams.models import ExamAttempt, ExamAttemptQuestion, AttemptStatus


# ─── helpers ──────────────────────────────────────────────────────────────────

def _trainee_summary(trainee: User) -> dict:
    enrollments = list(CourseEnrollment.objects.filter(user=trainee).select_related("course"))
    status_counts = {}
    for e in enrollments:
        status_counts[e.status] = status_counts.get(e.status, 0) + 1

    total_courses = Course.objects.filter(is_active=True).count()
    pending_requests = UnlockRequest.objects.filter(user=trainee, status=UnlockRequestStatus.PENDING).count()
    last_activity = (
        ModuleProgress.objects.filter(user=trainee)
        .order_by("-started_at")
        .values_list("started_at", flat=True)
        .first()
    )
    days_inactive = (timezone.now() - last_activity).days if last_activity else None

    return {
        "trainee": trainee,
        "passed": status_counts.get(EnrollmentStatus.PASSED, 0),
        "in_progress": status_counts.get(EnrollmentStatus.IN_PROGRESS, 0),
        "open": status_counts.get(EnrollmentStatus.OPEN, 0),
        "failed": status_counts.get(EnrollmentStatus.FAILED, 0),
        "pending_requests": pending_requests,
        "total_courses": total_courses,
        "days_inactive": days_inactive,
        "is_struggling": days_inactive is not None and days_inactive >= 14,
    }


# ─── trainees list ────────────────────────────────────────────────────────────

@manager_or_ceo_required
def trainees_list(request: HttpRequest) -> HttpResponse:
    trainees = User.objects.filter(role=UserRole.TRAINEE, is_active=True).order_by("full_name_he", "email")
    summaries = [_trainee_summary(t) for t in trainees]
    return render(request, "reports/trainees_list.html", {"summaries": summaries})


# ─── trainee detail ───────────────────────────────────────────────────────────

@manager_or_ceo_required
def trainee_detail(request: HttpRequest, pk: int) -> HttpResponse:
    trainee = get_object_or_404(User, pk=pk, role=UserRole.TRAINEE)
    courses = Course.objects.filter(is_active=True).order_by("course_number")
    enrollment_map = {e.course_id: e for e in CourseEnrollment.objects.filter(user=trainee).select_related("course")}
    module_progress_map = {mp.module_id: mp for mp in ModuleProgress.objects.filter(user=trainee).select_related("module")}

    course_data = []
    for course in courses:
        enrollment = enrollment_map.get(course.pk)
        modules = list(course.modules.filter(is_active=True).order_by("module_number"))
        module_rows = [
            {"module": m, "progress": module_progress_map.get(m.pk)}
            for m in modules
        ]
        attempts = ExamAttempt.objects.filter(
            user=trainee, course=course
        ).order_by("attempt_number")
        course_data.append({
            "course": course,
            "enrollment": enrollment,
            "status": enrollment.status if enrollment else "locked",
            "module_rows": module_rows,
            "attempts": attempts,
        })

    summary = _trainee_summary(trainee)
    return render(request, "reports/trainee_detail.html", {
        "trainee": trainee,
        "summary": summary,
        "course_data": course_data,
    })


# ─── unlock requests inbox ────────────────────────────────────────────────────

@manager_required
def unlock_requests(request: HttpRequest) -> HttpResponse:
    pending = UnlockRequest.objects.filter(
        status=UnlockRequestStatus.PENDING
    ).select_related("user", "course").order_by("requested_at")
    recent = UnlockRequest.objects.filter(
        status__in=[UnlockRequestStatus.APPROVED, UnlockRequestStatus.DENIED]
    ).select_related("user", "course", "responded_by").order_by("-responded_at")[:20]
    return render(request, "reports/unlock_requests.html", {
        "pending": pending,
        "recent": recent,
    })


@require_POST
@manager_required
def approve_request(request: HttpRequest, pk: int) -> HttpResponse:
    unlock_req = get_object_or_404(UnlockRequest, pk=pk, status=UnlockRequestStatus.PENDING)
    note = request.POST.get("note", "").strip()
    unlock_req.approve(approved_by=request.user, note=note)
    unlock_req.save()
    from core.services.email import EmailService
    EmailService.send_unlock_approved(unlock_req.user, unlock_req.course)
    messages.success(request, f"בקשת הגישה של {unlock_req.user.display_name} אושרה.")
    return redirect("unlock_requests")


@require_POST
@manager_required
def deny_request(request: HttpRequest, pk: int) -> HttpResponse:
    unlock_req = get_object_or_404(UnlockRequest, pk=pk, status=UnlockRequestStatus.PENDING)
    note = request.POST.get("note", "").strip()
    unlock_req.deny(denied_by=request.user, note=note)
    unlock_req.save()
    # Roll back enrollment to locked
    enrollment = CourseEnrollment.objects.filter(user=unlock_req.user, course=unlock_req.course).first()
    if enrollment and enrollment.status == EnrollmentStatus.REQUESTED:
        enrollment.deny_unlock(denied_by=request.user)
        enrollment.save()
    from core.services.email import EmailService
    EmailService.send_unlock_denied(unlock_req.user, unlock_req.course, reason=note)
    messages.success(request, f"בקשת הגישה של {unlock_req.user.display_name} נדחתה.")
    return redirect("unlock_requests")


# ─── capstone inbox ───────────────────────────────────────────────────────────

@manager_required
def capstone_inbox(request: HttpRequest) -> HttpResponse:
    pending = CapstoneSubmission.objects.filter(
        status__in=[CapstoneStatus.SUBMITTED, CapstoneStatus.UNDER_REVIEW]
    ).select_related("user", "course").order_by("submitted_at")
    completed = CapstoneSubmission.objects.filter(
        status__in=[CapstoneStatus.PASSED, CapstoneStatus.FAILED]
    ).select_related("user", "course").order_by("-submitted_at")[:20]
    return render(request, "reports/capstone_inbox.html", {
        "pending": pending,
        "completed": completed,
    })


# ─── group report ─────────────────────────────────────────────────────────────

@manager_or_ceo_required
def group_report(request: HttpRequest) -> HttpResponse:
    trainee_count = User.objects.filter(role=UserRole.TRAINEE, is_active=True).count()
    courses = Course.objects.filter(is_active=True).order_by("course_number")

    course_stats = []
    for course in courses:
        enrollments = CourseEnrollment.objects.filter(course=course)
        enrolled = enrollments.count()
        passed = enrollments.filter(status=EnrollmentStatus.PASSED).count()
        in_progress = enrollments.filter(status=EnrollmentStatus.IN_PROGRESS).count()
        graded_attempts = ExamAttempt.objects.filter(course=course, status=AttemptStatus.GRADED)
        avg_score = graded_attempts.aggregate(avg=Avg("score_pct"))["avg"]
        pass_rate = round((passed / enrolled) * 100) if enrolled else 0
        course_stats.append({
            "course": course,
            "enrolled": enrolled,
            "passed": passed,
            "in_progress": in_progress,
            "pass_rate": pass_rate,
            "avg_score": round(avg_score, 1) if avg_score else None,
            "attempt_count": graded_attempts.count(),
        })

    # Struggling trainees: enrolled in ≥1 course but no activity in 14 days
    two_weeks_ago = timezone.now() - timedelta(days=14)
    struggling = []
    for t in User.objects.filter(role=UserRole.TRAINEE, is_active=True):
        has_enrollment = CourseEnrollment.objects.filter(
            user=t, status__in=[EnrollmentStatus.OPEN, EnrollmentStatus.IN_PROGRESS]
        ).exists()
        if not has_enrollment:
            continue
        recent_activity = ModuleProgress.objects.filter(user=t, started_at__gte=two_weeks_ago).exists()
        if not recent_activity:
            struggling.append(t)

    pending_requests = UnlockRequest.objects.filter(status=UnlockRequestStatus.PENDING).count()

    return render(request, "reports/group_report.html", {
        "trainee_count": trainee_count,
        "course_stats": course_stats,
        "struggling": struggling,
        "pending_requests": pending_requests,
    })


# ─── confidence map ───────────────────────────────────────────────────────────

@manager_or_ceo_required
def confidence_map(request: HttpRequest) -> HttpResponse:
    courses = Course.objects.filter(is_active=True).order_by("course_number")
    selected_slug = request.GET.get("course", "")
    selected_course = None

    overconfident_qs = ExamAttemptQuestion.objects.none()
    lucky_guess_qs = ExamAttemptQuestion.objects.none()

    if selected_slug:
        selected_course = Course.objects.filter(slug=selected_slug).first()
        if selected_course:
            base_qs = ExamAttemptQuestion.objects.filter(
                attempt__course=selected_course,
                attempt__status=AttemptStatus.GRADED,
            ).select_related("attempt__user", "question")

            overconfident_qs = (
                base_qs.filter(confidence="confident", is_correct=False)
                .values("stem_html_snapshot", "question_id")
                .annotate(count=Count("id"))
                .order_by("-count")[:10]
            )
            lucky_guess_qs = (
                base_qs.filter(confidence="not_sure", is_correct=True)
                .values("stem_html_snapshot", "question_id")
                .annotate(count=Count("id"))
                .order_by("-count")[:10]
            )

    return render(request, "reports/confidence_map.html", {
        "courses": courses,
        "selected_course": selected_course,
        "selected_slug": selected_slug,
        "overconfident": list(overconfident_qs),
        "lucky_guesses": list(lucky_guess_qs),
    })
