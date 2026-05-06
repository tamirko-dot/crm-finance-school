import logging

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from django.views.decorators.http import require_POST

from content.models import Course, Module, ModuleComponent, ComponentType, Question, QuestionUsage
from documents.models import AuditLog
from enrollment.models import (
    CourseEnrollment, EnrollmentStatus, UnlockRequest, UnlockRequestStatus,
    ModuleProgress, ComponentProgress,
)

logger = logging.getLogger(__name__)


# ─── helpers ──────────────────────────────────────────────────────────────────

def _get_enrollment_map(user) -> dict:
    """Returns {course_pk: enrollment_or_None} for all courses."""
    enrollments = {e.course_id: e for e in CourseEnrollment.objects.filter(user=user).select_related("course")}
    return enrollments


def _require_enrollment(user, course, allowed_statuses):
    enrollment = CourseEnrollment.objects.filter(user=user, course=course).first()
    if not enrollment or enrollment.status not in allowed_statuses:
        raise PermissionDenied
    return enrollment


def _get_current_component(user, module: Module):
    """Returns the first incomplete component, or None if all done."""
    components = list(module.components.filter(is_active=True).order_by("order"))
    completed_pks = set(
        ComponentProgress.objects.filter(user=user, component__in=components, is_completed=True)
        .values_list("component_id", flat=True)
    )
    for comp in components:
        if comp.pk not in completed_pks:
            return comp
    return None


def _mark_component_complete(user, component: ModuleComponent) -> None:
    cp, _ = ComponentProgress.objects.get_or_create(user=user, component=component)
    if not cp.is_completed:
        cp.is_completed = True
        cp.completed_at = timezone.now()
        cp.save()


def _check_all_modules_complete(user, course: Course) -> bool:
    modules = list(course.modules.filter(is_active=True))
    completed = ModuleProgress.objects.filter(user=user, module__in=modules, is_completed=True).count()
    return completed >= len(modules)


# ─── course list ──────────────────────────────────────────────────────────────

@login_required
def course_list(request: HttpRequest) -> HttpResponse:
    courses = Course.objects.filter(domain__is_active=True, is_active=True).select_related("domain").order_by("course_number")
    enrollment_map = _get_enrollment_map(request.user)

    course_data = []
    for course in courses:
        enrollment = enrollment_map.get(course.pk)
        course_data.append({
            "course": course,
            "enrollment": enrollment,
            "status": enrollment.status if enrollment else "locked",
        })

    return render(request, "content/course_list.html", {"course_data": course_data})


# ─── course detail ────────────────────────────────────────────────────────────

@login_required
def course_detail(request: HttpRequest, course_slug: str) -> HttpResponse:
    course = get_object_or_404(Course, slug=course_slug, is_active=True)
    enrollment = CourseEnrollment.objects.filter(user=request.user, course=course).first()
    status = enrollment.status if enrollment else "locked"

    can_access = status in (EnrollmentStatus.OPEN, EnrollmentStatus.IN_PROGRESS,
                            EnrollmentStatus.PASSED, EnrollmentStatus.FAILED)

    modules = course.modules.filter(is_active=True).order_by("module_number") if can_access else []
    module_progress_map = {}
    if can_access and modules:
        for mp in ModuleProgress.objects.filter(user=request.user, module__in=modules):
            module_progress_map[mp.module_id] = mp

    modules_data = [
        {"module": m, "progress": module_progress_map.get(m.pk)}
        for m in modules
    ]

    # Check if all modules done (exam unlocked)
    all_modules_done = can_access and _check_all_modules_complete(request.user, course)

    # Existing exam attempts
    from exams.models import ExamAttempt, AttemptStatus
    latest_attempt = ExamAttempt.objects.filter(
        user=request.user, course=course
    ).order_by("-attempt_number").first()

    # Capstone submission (Course 12 only)
    latest_capstone = None
    if course.is_capstone:
        from capstone.models import CapstoneSubmission
        latest_capstone = CapstoneSubmission.objects.filter(
            user=request.user, course=course
        ).order_by("-submitted_at").first()

    return render(request, "content/course_detail.html", {
        "course": course,
        "enrollment": enrollment,
        "status": status,
        "can_access": can_access,
        "modules_data": modules_data,
        "all_modules_done": all_modules_done,
        "latest_attempt": latest_attempt,
        "latest_capstone": latest_capstone,
    })


# ─── request access ───────────────────────────────────────────────────────────

@require_POST
@login_required
def request_course_access(request: HttpRequest, course_slug: str) -> HttpResponse:
    course = get_object_or_404(Course, slug=course_slug, is_active=True)
    user = request.user

    # Check no pending/approved request already exists
    existing = UnlockRequest.objects.filter(user=user, course=course, status=UnlockRequestStatus.PENDING).first()
    if existing:
        messages.info(request, "הבקשה כבר נשלחה וממתינה לאישור.")
        return redirect("course_detail", course_slug=course_slug)

    enrollment, _ = CourseEnrollment.objects.get_or_create(user=user, course=course)
    if enrollment.status not in (EnrollmentStatus.LOCKED,):
        messages.info(request, "אין צורך בבקשה — הקורס כבר פתוח עבורך.")
        return redirect("course_detail", course_slug=course_slug)

    enrollment.request_unlock()
    enrollment.save()

    UnlockRequest.objects.create(user=user, course=course)

    AuditLog.objects.create(
        user=user, action="request_unlock", entity_type="Course",
        entity_id=str(course.pk), metadata_json={"course_slug": course_slug},
    )
    messages.success(request, "הבקשה נשלחה בהצלחה. מנהל הלקוחות יאשר אותה בהקדם.")
    return redirect("course_detail", course_slug=course_slug)


# ─── module view ──────────────────────────────────────────────────────────────

@login_required
def module_view(request: HttpRequest, course_slug: str, module_slug: str) -> HttpResponse:
    course = get_object_or_404(Course, slug=course_slug, is_active=True)
    module = get_object_or_404(Module, course=course, slug=module_slug, is_active=True)
    enrollment = _require_enrollment(
        request.user, course,
        [EnrollmentStatus.OPEN, EnrollmentStatus.IN_PROGRESS, EnrollmentStatus.PASSED]
    )

    # Auto-transition enrollment to in_progress on first module entry
    if enrollment.status == EnrollmentStatus.OPEN:
        enrollment.start_course()
        enrollment.save()

    # Ensure ModuleProgress exists
    mp, _ = ModuleProgress.objects.get_or_create(user=request.user, module=module)

    current_component = _get_current_component(request.user, module)

    if request.method == "POST":
        return _handle_component_post(request, course, module, mp, current_component)

    # Build feedback from session if present
    sess_key = f"comp_feedback_{module.pk}"
    feedback = request.session.pop(sess_key, None)

    return render(request, "content/module_view.html", {
        "course": course,
        "module": module,
        "current_component": current_component,
        "module_complete": current_component is None,
        "feedback": feedback,
        "all_components": module.components.filter(is_active=True).order_by("order"),
    })


def _handle_component_post(request, course, module, mp, current_component):
    action = request.POST.get("action", "")

    if action == "read_complete" and current_component and current_component.component_type == ComponentType.READING:
        _mark_component_complete(request.user, current_component)
        messages.success(request, "קריאה הושלמה.")
        return redirect("module_view", course_slug=course.slug, module_slug=module.slug)

    if action == "summary_complete" and current_component and current_component.component_type == ComponentType.SUMMARY:
        _mark_component_complete(request.user, current_component)
        mp.is_completed = True
        mp.completed_at = timezone.now()
        mp.save()
        messages.success(request, "המודול הושלם בהצלחה!")
        return redirect("course_detail", course_slug=course.slug)

    if action == "submit_comprehension" and current_component and current_component.component_type == ComponentType.COMPREHENSION:
        return _process_comprehension(request, course, module, mp, current_component)

    if action == "comprehension_complete" and current_component and current_component.component_type == ComponentType.COMPREHENSION:
        _mark_component_complete(request.user, current_component)
        return redirect("module_view", course_slug=course.slug, module_slug=module.slug)

    if action == "submit_exercises" and current_component and current_component.component_type == ComponentType.EXERCISES:
        return _process_exercises(request, course, module, mp, current_component)

    if action == "exercises_complete" and current_component and current_component.component_type == ComponentType.EXERCISES:
        _mark_component_complete(request.user, current_component)
        return redirect("module_view", course_slug=course.slug, module_slug=module.slug)

    return redirect("module_view", course_slug=course.slug, module_slug=module.slug)


def _get_component_questions(module: Module, usage: str) -> list:
    return list(
        Question.objects.filter(module=module, usage_context=usage, is_active=True)
        .prefetch_related("options", "explanation")
        .order_by("question_id_external")
    )


def _process_comprehension(request, course, module, mp, component):
    questions = _get_component_questions(module, QuestionUsage.COMPREHENSION)
    results = []
    for q in questions:
        answer_key = f"answer_{q.pk}"
        try:
            chosen_idx = int(request.POST.get(answer_key, -1))
        except (ValueError, TypeError):
            chosen_idx = -1
        options = list(q.options.order_by("display_order"))
        correct_idx = next((i for i, o in enumerate(options) if o.is_correct), 0)
        is_correct = chosen_idx == correct_idx
        chosen_option = options[chosen_idx] if 0 <= chosen_idx < len(options) else None
        correct_option = options[correct_idx] if options else None
        results.append({
            "question": q,
            "options": options,
            "chosen_idx": chosen_idx,
            "correct_idx": correct_idx,
            "is_correct": is_correct,
            "chosen_option": chosen_option,
            "correct_option": correct_option,
        })

    sess_key = f"comp_feedback_{module.pk}"
    request.session[sess_key] = {"type": "comprehension", "results": [
        {
            "stem": r["question"].stem_html_he,
            "is_correct": r["is_correct"],
            "chosen_text": r["chosen_option"].text_he if r["chosen_option"] else "—",
            "correct_text": r["correct_option"].text_he if r["correct_option"] else "—",
            "explanation": r["question"].explanation.explanation_html_he if hasattr(r["question"], "explanation") else "",
        }
        for r in results
    ]}
    return redirect("module_view", course_slug=course.slug, module_slug=module.slug)


def _process_exercises(request, course, module, mp, component):
    questions = _get_component_questions(module, QuestionUsage.PRACTICE)
    sess_key_scores = f"exercise_scores_{module.pk}"
    scores = request.session.get(sess_key_scores, {})
    is_second_attempt = bool(scores)

    results = []
    correct_count = 0
    for q in questions:
        answer_key = f"answer_{q.pk}"
        try:
            chosen_idx = int(request.POST.get(answer_key, -1))
        except (ValueError, TypeError):
            chosen_idx = -1
        options = list(q.options.order_by("display_order"))
        correct_idx = next((i for i, o in enumerate(options) if o.is_correct), 0)
        is_correct = chosen_idx == correct_idx
        chosen_option = options[chosen_idx] if 0 <= chosen_idx < len(options) else None
        correct_option = options[correct_idx] if options else None
        distractor = chosen_option.distractor_rationale_he if (chosen_option and not is_correct) else ""

        if is_correct:
            correct_count += 1
        scores[str(q.pk)] = {"attempts": (scores.get(str(q.pk), {}).get("attempts", 0) + 1), "correct": is_correct}
        results.append({
            "question": q,
            "options": options,
            "chosen_idx": chosen_idx,
            "correct_idx": correct_idx,
            "is_correct": is_correct,
            "chosen_option": chosen_option,
            "correct_option": correct_option,
            "distractor": distractor,
            "locked": is_correct or is_second_attempt,
        })

    score_pct = round((correct_count / len(questions)) * 100) if questions else 0
    mp.practice_score_pct = score_pct
    mp.save(update_fields=["practice_score_pct"])
    request.session[sess_key_scores] = scores

    sess_key = f"comp_feedback_{module.pk}"
    request.session[sess_key] = {"type": "exercises", "results": [
        {
            "stem": r["question"].stem_html_he,
            "is_correct": r["is_correct"],
            "chosen_text": r["chosen_option"].text_he if r["chosen_option"] else "—",
            "correct_text": r["correct_option"].text_he if r["correct_option"] else "—",
            "distractor": r["distractor"],
            "explanation": r["question"].explanation.explanation_html_he if hasattr(r["question"], "explanation") else "",
            "locked": r["locked"],
        }
        for r in results
    ], "score_pct": score_pct, "is_second_attempt": is_second_attempt}
    return redirect("module_view", course_slug=course.slug, module_slug=module.slug)
