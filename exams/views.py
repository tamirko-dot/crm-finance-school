import logging

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from django.views.decorators.http import require_POST

from content.models import Course
from enrollment.models import CourseEnrollment, EnrollmentStatus, ModuleProgress
from exams.models import ExamAttempt, ExamAttemptQuestion, AttemptStatus
from exams.services import create_exam_attempt, grade_exam_attempt, seconds_remaining

logger = logging.getLogger(__name__)


def _get_open_enrollment(user, course):
    e = CourseEnrollment.objects.filter(user=user, course=course).first()
    if not e or e.status not in (EnrollmentStatus.IN_PROGRESS, EnrollmentStatus.OPEN,
                                  EnrollmentStatus.PASSED, EnrollmentStatus.FAILED):
        raise PermissionDenied
    return e


def _check_retry_eligibility(user, course) -> tuple[bool, str]:
    """Returns (can_start, reason_if_blocked)."""
    from datetime import timedelta
    attempts = ExamAttempt.objects.filter(
        user=user, course=course, status=AttemptStatus.GRADED
    ).order_by("-attempt_number")

    if not attempts.exists():
        return True, ""

    last = attempts.first()
    count = attempts.count()

    if last.passed:
        return False, "כבר עברת את המבחן בהצלחה."

    if count == 1:
        cooldown = last.submitted_at + timedelta(hours=24)
        if timezone.now() < cooldown:
            remaining = cooldown - timezone.now()
            hours = int(remaining.total_seconds() // 3600)
            return False, f"עליך להמתין {hours} שעות נוספות לפני ניסיון שני."

    if count == 2:
        cooldown = last.submitted_at + timedelta(hours=72)
        if timezone.now() < cooldown:
            remaining = cooldown - timezone.now()
            hours = int(remaining.total_seconds() // 3600)
            return False, f"עליך להמתין {hours} שעות נוספות. גם נדרשת פגישה עם מנטור לפני ניסיון שלישי."

    if count >= 3:
        return False, "הגעת למספר הניסיונות המרבי. נדרש אישור מנהל מערכת להמשך."

    return True, ""


# ─── exam start ───────────────────────────────────────────────────────────────

@login_required
def exam_start(request: HttpRequest, course_slug: str) -> HttpResponse:
    course = get_object_or_404(Course, slug=course_slug, is_active=True)
    enrollment = _get_open_enrollment(request.user, course)

    # Check all modules done
    modules = list(course.modules.filter(is_active=True))
    done_count = ModuleProgress.objects.filter(
        user=request.user, module__in=modules, is_completed=True
    ).count()
    all_modules_done = done_count >= len(modules)

    # In-progress attempt (resume)
    active_attempt = ExamAttempt.objects.filter(
        user=request.user, course=course, status=AttemptStatus.IN_PROGRESS
    ).first()

    can_start, block_reason = _check_retry_eligibility(request.user, course)
    past_attempts = ExamAttempt.objects.filter(
        user=request.user, course=course
    ).exclude(status=AttemptStatus.IN_PROGRESS).order_by("-attempt_number")

    if request.method == "POST":
        if active_attempt:
            return redirect("exam_question", course_slug=course_slug, attempt_pk=active_attempt.pk)

        if not all_modules_done:
            messages.error(request, "יש להשלים את כל המודולים לפני המבחן.")
            return redirect("course_detail", course_slug=course_slug)

        if not can_start:
            messages.error(request, block_reason)
            return redirect("exam_start", course_slug=course_slug)

        attempt = create_exam_attempt(request.user, course)
        return redirect("exam_question", course_slug=course_slug, attempt_pk=attempt.pk)

    return render(request, "exams/exam_start.html", {
        "course": course,
        "enrollment": enrollment,
        "all_modules_done": all_modules_done,
        "active_attempt": active_attempt,
        "can_start": can_start,
        "block_reason": block_reason,
        "past_attempts": past_attempts,
    })


# ─── exam question (forward-only) ─────────────────────────────────────────────

@login_required
def exam_question(request: HttpRequest, course_slug: str, attempt_pk: int) -> HttpResponse:
    course = get_object_or_404(Course, slug=course_slug, is_active=True)
    attempt = get_object_or_404(ExamAttempt, pk=attempt_pk, user=request.user, course=course)

    if attempt.status != AttemptStatus.IN_PROGRESS:
        return redirect("exam_result", course_slug=course_slug, attempt_pk=attempt_pk)

    # Server-side timer enforcement
    secs = seconds_remaining(attempt)
    if secs == 0:
        logger.info("Auto-submitting exam attempt %s — time expired", attempt_pk)
        _auto_submit(attempt)
        return redirect("exam_result", course_slug=course_slug, attempt_pk=attempt_pk)

    # First unanswered question
    current_aq = attempt.attempt_questions.filter(user_answer_option_index__isnull=True).order_by("display_order").first()
    if current_aq is None:
        return redirect("exam_submit", course_slug=course_slug, attempt_pk=attempt_pk)

    total = attempt.attempt_questions.count()
    answered = attempt.attempt_questions.filter(user_answer_option_index__isnull=False).count()

    if request.method == "POST":
        try:
            chosen_idx = int(request.POST.get("answer", -1))
        except (ValueError, TypeError):
            chosen_idx = -1

        confidence = request.POST.get("confidence") or None
        if confidence not in ("confident", "not_sure"):
            confidence = None

        if chosen_idx < 0:
            messages.error(request, "יש לבחור תשובה לפני המעבר לשאלה הבאה.")
        else:
            current_aq.user_answer_option_index = chosen_idx
            current_aq.confidence = confidence
            current_aq.answered_at = timezone.now()
            current_aq.save(update_fields=["user_answer_option_index", "confidence", "answered_at"])

        return redirect("exam_question", course_slug=course_slug, attempt_pk=attempt_pk)

    options = current_aq.options_snapshot_json

    return render(request, "exams/exam_question.html", {
        "course": course,
        "attempt": attempt,
        "current_aq": current_aq,
        "options": options,
        "total": total,
        "answered": answered,
        "question_number": answered + 1,
        "seconds_remaining": secs,
    })


def _auto_submit(attempt: ExamAttempt) -> None:
    unanswered = attempt.attempt_questions.filter(user_answer_option_index__isnull=True)
    unanswered.update(user_answer_option_index=-1, answered_at=timezone.now())
    grade_exam_attempt(attempt)
    _update_enrollment_after_exam(attempt)


# ─── exam submit ──────────────────────────────────────────────────────────────

@login_required
def exam_submit(request: HttpRequest, course_slug: str, attempt_pk: int) -> HttpResponse:
    course = get_object_or_404(Course, slug=course_slug, is_active=True)
    attempt = get_object_or_404(ExamAttempt, pk=attempt_pk, user=request.user, course=course)

    if attempt.status != AttemptStatus.IN_PROGRESS:
        return redirect("exam_result", course_slug=course_slug, attempt_pk=attempt_pk)

    unanswered_count = attempt.attempt_questions.filter(user_answer_option_index__isnull=True).count()

    if request.method == "POST" and request.POST.get("confirm") == "1":
        if unanswered_count > 0:
            unanswered = attempt.attempt_questions.filter(user_answer_option_index__isnull=True)
            unanswered.update(user_answer_option_index=-1, answered_at=timezone.now())
        grade_exam_attempt(attempt)
        _update_enrollment_after_exam(attempt)
        return redirect("exam_result", course_slug=course_slug, attempt_pk=attempt_pk)

    return render(request, "exams/exam_submit.html", {
        "course": course,
        "attempt": attempt,
        "unanswered_count": unanswered_count,
        "seconds_remaining": seconds_remaining(attempt),
    })


def _update_enrollment_after_exam(attempt: ExamAttempt) -> None:
    enrollment = CourseEnrollment.objects.filter(user=attempt.user, course=attempt.course).first()
    if not enrollment:
        return
    if attempt.passed and enrollment.status == EnrollmentStatus.IN_PROGRESS:
        enrollment.mark_passed()
        enrollment.save()
        from core.services.email import EmailService
        EmailService.send_exam_passed(attempt.user, attempt.course, attempt.score_pct)
    elif not attempt.passed and enrollment.status == EnrollmentStatus.IN_PROGRESS:
        can_retry, _ = _check_retry_eligibility(attempt.user, attempt.course)
        if not can_retry:
            enrollment.mark_failed()
            enrollment.save()
        from core.services.email import EmailService
        past_count = ExamAttempt.objects.filter(
            user=attempt.user, course=attempt.course, status=AttemptStatus.GRADED
        ).count()
        EmailService.send_exam_failed(attempt.user, attempt.course, attempt.score_pct, max(0, 3 - past_count))


# ─── exam result ──────────────────────────────────────────────────────────────

@login_required
def exam_result(request: HttpRequest, course_slug: str, attempt_pk: int) -> HttpResponse:
    course = get_object_or_404(Course, slug=course_slug, is_active=True)
    attempt = get_object_or_404(ExamAttempt, pk=attempt_pk, user=request.user, course=course)

    if attempt.status == AttemptStatus.IN_PROGRESS:
        return redirect("exam_question", course_slug=course_slug, attempt_pk=attempt_pk)

    question_results = attempt.attempt_questions.select_related("question").order_by("display_order")
    correct_count = sum(1 for aq in question_results if aq.is_correct)

    return render(request, "exams/exam_result.html", {
        "course": course,
        "attempt": attempt,
        "question_results": question_results,
        "correct_count": correct_count,
        "total_count": question_results.count(),
    })
