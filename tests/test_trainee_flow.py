"""
Phase 4 tests: course list, course detail, module flow, request access, exam.
"""
import pytest
from django.urls import reverse

from accounts.models import User, UserRole
from content.models import (
    Course, Domain, Module, ModuleComponent, ComponentType,
    Question, QuestionOption, QuestionExplanation, QuestionType, QuestionDifficulty, QuestionUsage,
)
from enrollment.models import CourseEnrollment, EnrollmentStatus, ModuleProgress, ComponentProgress
from exams.models import ExamAttempt, AttemptStatus


# ─── fixtures ─────────────────────────────────────────────────────────────────

@pytest.fixture
def domain(db):
    return Domain.objects.create(name_he="Test", name_en="Test Domain", slug="test-domain")


@pytest.fixture
def course(db, domain):
    return Course.objects.create(
        domain=domain, title_he="קורס בדיקה", slug="c99-test-course",
        phase="A", course_number=99, passing_score_pct=75,
        exam_question_count=2, exam_duration_minutes=60,
    )


@pytest.fixture
def module(db, course):
    return Module.objects.create(
        course=course, title_he="מודול בדיקה", slug="test-module", module_number=1, estimated_minutes=30,
    )


@pytest.fixture
def components(db, module):
    reading = ModuleComponent.objects.create(
        module=module, component_type=ComponentType.READING, order=1,
        body_html_he="<p>תוכן קריאה</p>",
    )
    comprehension = ModuleComponent.objects.create(
        module=module, component_type=ComponentType.COMPREHENSION, order=2, instructions_he="ענה"
    )
    exercises = ModuleComponent.objects.create(
        module=module, component_type=ComponentType.EXERCISES, order=3, instructions_he="תרגל"
    )
    summary = ModuleComponent.objects.create(
        module=module, component_type=ComponentType.SUMMARY, order=4, body_html_he="<p>סיכום</p>",
    )
    return reading, comprehension, exercises, summary


@pytest.fixture
def exam_question(db, course, module):
    q = Question.objects.create(
        course=course, module=module,
        question_id_external="C99-M01-Q01",
        question_type=QuestionType.RETRIEVAL,
        difficulty=QuestionDifficulty.BASIC,
        usage_context=QuestionUsage.EXAM,
        stem_html_he="<p>מה זה LTV?</p>",
        points=1,
    )
    QuestionOption.objects.create(question=q, text_he="סכום הלוואה חלקי שווי נכס", is_correct=True, display_order=0)
    QuestionOption.objects.create(question=q, text_he="שווי נכס חלקי הלוואה", is_correct=False, display_order=1, distractor_rationale_he="הפוך")
    QuestionExplanation.objects.create(question=q, explanation_html_he="<p>LTV = הלוואה / שווי</p>")
    return q


@pytest.fixture
def trainee(db):
    return User.objects.create_user(email="t@test.local", username="t_test", password="Test1234!", role=UserRole.TRAINEE)


@pytest.fixture
def manager(db):
    return User.objects.create_user(email="m@test.local", username="m_test", password="Test1234!", role=UserRole.CUSTOMER_MANAGER)


@pytest.fixture
def open_enrollment(db, trainee, manager, course):
    e = CourseEnrollment.objects.create(user=trainee, course=course, status=EnrollmentStatus.LOCKED)
    e.request_unlock(); e.save()
    e.approve_unlock(approved_by=manager); e.save()
    return e


# ─── course list ──────────────────────────────────────────────────────────────

@pytest.mark.django_db
class TestCourseList:
    def test_requires_login(self, client):
        resp = client.get(reverse("course_list"))
        assert resp.status_code == 302
        assert "login" in resp["Location"]

    def test_trainee_sees_courses(self, client, trainee, course):
        client.force_login(trainee)
        resp = client.get(reverse("course_list"))
        assert resp.status_code == 200
        assert "קורס בדיקה" in resp.content.decode("utf-8")

    def test_locked_course_shows_locked_badge(self, client, trainee, course):
        client.force_login(trainee)
        resp = client.get(reverse("course_list"))
        assert "נעול" in resp.content.decode("utf-8")

    def test_open_course_shows_open_badge(self, client, trainee, open_enrollment, course):
        client.force_login(trainee)
        resp = client.get(reverse("course_list"))
        content = resp.content.decode("utf-8")
        assert "פתוח" in content or "בתהליך" in content


# ─── course detail ────────────────────────────────────────────────────────────

@pytest.mark.django_db
class TestCourseDetail:
    def test_locked_shows_request_button(self, client, trainee, course):
        client.force_login(trainee)
        resp = client.get(reverse("course_detail", kwargs={"course_slug": course.slug}))
        assert resp.status_code == 200
        assert "בקשת גישה" in resp.content.decode("utf-8")

    def test_open_shows_modules(self, client, trainee, open_enrollment, course, module, components):
        client.force_login(trainee)
        resp = client.get(reverse("course_detail", kwargs={"course_slug": course.slug}))
        assert resp.status_code == 200
        assert "מודול בדיקה" in resp.content.decode("utf-8")

    def test_exam_locked_before_modules_done(self, client, trainee, open_enrollment, course, module, components):
        client.force_login(trainee)
        resp = client.get(reverse("course_detail", kwargs={"course_slug": course.slug}))
        content = resp.content.decode("utf-8")
        assert "יש להשלים את כל המודולים" in content


# ─── request access ───────────────────────────────────────────────────────────

@pytest.mark.django_db
class TestRequestAccess:
    def test_creates_unlock_request(self, client, trainee, course):
        client.force_login(trainee)
        resp = client.post(reverse("request_course_access", kwargs={"course_slug": course.slug}))
        assert resp.status_code == 302
        from enrollment.models import UnlockRequest, UnlockRequestStatus
        assert UnlockRequest.objects.filter(user=trainee, course=course, status=UnlockRequestStatus.PENDING).exists()

    def test_enrollment_transitions_to_requested(self, client, trainee, course):
        client.force_login(trainee)
        client.post(reverse("request_course_access", kwargs={"course_slug": course.slug}))
        e = CourseEnrollment.objects.get(user=trainee, course=course)
        assert e.status == EnrollmentStatus.REQUESTED

    def test_duplicate_request_blocked(self, client, trainee, course):
        client.force_login(trainee)
        client.post(reverse("request_course_access", kwargs={"course_slug": course.slug}))
        client.post(reverse("request_course_access", kwargs={"course_slug": course.slug}))
        from enrollment.models import UnlockRequest
        assert UnlockRequest.objects.filter(user=trainee, course=course).count() == 1


# ─── module flow ──────────────────────────────────────────────────────────────

@pytest.mark.django_db
class TestModuleFlow:
    def test_locked_course_denies_module_access(self, client, trainee, course, module):
        client.force_login(trainee)
        resp = client.get(reverse("module_view", kwargs={"course_slug": course.slug, "module_slug": module.slug}))
        assert resp.status_code == 403

    def test_open_course_shows_reading_component(self, client, trainee, open_enrollment, course, module, components):
        client.force_login(trainee)
        resp = client.get(reverse("module_view", kwargs={"course_slug": course.slug, "module_slug": module.slug}))
        assert resp.status_code == 200
        assert "תוכן קריאה" in resp.content.decode("utf-8")

    def test_reading_complete_advances_to_comprehension(self, client, trainee, open_enrollment, course, module, components):
        reading, comprehension, _, _ = components
        client.force_login(trainee)
        client.post(
            reverse("module_view", kwargs={"course_slug": course.slug, "module_slug": module.slug}),
            {"action": "read_complete"}
        )
        cp = ComponentProgress.objects.filter(user=trainee, component=reading).first()
        assert cp is not None and cp.is_completed

    def test_cannot_skip_components(self, client, trainee, open_enrollment, course, module, components):
        _, comprehension, _, _ = components
        client.force_login(trainee)
        # Try to complete comprehension without finishing reading first
        client.post(
            reverse("module_view", kwargs={"course_slug": course.slug, "module_slug": module.slug}),
            {"action": "comprehension_complete"}
        )
        # Reading should still be the current component (no progress on comprehension)
        cp = ComponentProgress.objects.filter(user=trainee, component=comprehension, is_completed=True).first()
        assert cp is None

    def test_summary_completes_module(self, client, trainee, open_enrollment, course, module, components):
        reading, comprehension, exercises, summary = components
        client.force_login(trainee)
        # Complete all prior components
        for comp in [reading, comprehension, exercises]:
            ComponentProgress.objects.create(user=trainee, component=comp, is_completed=True)
        # Now complete summary
        client.post(
            reverse("module_view", kwargs={"course_slug": course.slug, "module_slug": module.slug}),
            {"action": "summary_complete"}
        )
        mp = ModuleProgress.objects.filter(user=trainee, module=module).first()
        assert mp is not None and mp.is_completed


# ─── exam flow ────────────────────────────────────────────────────────────────

@pytest.mark.django_db
class TestExamFlow:
    def test_exam_blocked_before_modules_done(self, client, trainee, open_enrollment, course, module, components, exam_question):
        client.force_login(trainee)
        resp = client.post(reverse("exam_start", kwargs={"course_slug": course.slug}))
        assert resp.status_code == 302
        assert not ExamAttempt.objects.filter(user=trainee, course=course).exists()

    def test_exam_creates_attempt_when_modules_done(self, client, trainee, open_enrollment, course, module, components, exam_question):
        client.force_login(trainee)
        ModuleProgress.objects.create(user=trainee, module=module, is_completed=True)
        resp = client.post(reverse("exam_start", kwargs={"course_slug": course.slug}))
        assert resp.status_code == 302
        assert ExamAttempt.objects.filter(user=trainee, course=course).exists()

    def test_exam_snapshots_questions(self, client, trainee, open_enrollment, course, module, components, exam_question):
        client.force_login(trainee)
        ModuleProgress.objects.create(user=trainee, module=module, is_completed=True)
        client.post(reverse("exam_start", kwargs={"course_slug": course.slug}))
        attempt = ExamAttempt.objects.get(user=trainee, course=course)
        assert attempt.attempt_questions.count() > 0
        aq = attempt.attempt_questions.first()
        assert aq.stem_html_snapshot == exam_question.stem_html_he

    def test_answer_saved_and_advances(self, client, trainee, open_enrollment, course, module, components, exam_question):
        client.force_login(trainee)
        ModuleProgress.objects.create(user=trainee, module=module, is_completed=True)
        client.post(reverse("exam_start", kwargs={"course_slug": course.slug}))
        attempt = ExamAttempt.objects.get(user=trainee, course=course)
        client.post(
            reverse("exam_question", kwargs={"course_slug": course.slug, "attempt_pk": attempt.pk}),
            {"answer": "0"}
        )
        aq = attempt.attempt_questions.first()
        aq.refresh_from_db()
        assert aq.user_answer_option_index == 0
        assert aq.answered_at is not None

    def test_submit_grades_and_transitions_fsm(self, client, trainee, open_enrollment, course, module, components, exam_question):
        client.force_login(trainee)
        ModuleProgress.objects.create(user=trainee, module=module, is_completed=True)
        client.post(reverse("exam_start", kwargs={"course_slug": course.slug}))
        attempt = ExamAttempt.objects.get(user=trainee, course=course)
        # Answer all questions
        for aq in attempt.attempt_questions.all():
            client.post(
                reverse("exam_question", kwargs={"course_slug": course.slug, "attempt_pk": attempt.pk}),
                {"answer": "0"}
            )
        # Submit
        client.post(
            reverse("exam_submit", kwargs={"course_slug": course.slug, "attempt_pk": attempt.pk}),
            {"confirm": "1"}
        )
        attempt.refresh_from_db()
        assert attempt.status == AttemptStatus.GRADED
        assert attempt.score_pct is not None

    def test_result_page_shows_score(self, client, trainee, open_enrollment, course, module, components, exam_question):
        client.force_login(trainee)
        ModuleProgress.objects.create(user=trainee, module=module, is_completed=True)
        client.post(reverse("exam_start", kwargs={"course_slug": course.slug}))
        attempt = ExamAttempt.objects.get(user=trainee, course=course)
        for aq in attempt.attempt_questions.all():
            client.post(
                reverse("exam_question", kwargs={"course_slug": course.slug, "attempt_pk": attempt.pk}),
                {"answer": "0"}
            )
        client.post(
            reverse("exam_submit", kwargs={"course_slug": course.slug, "attempt_pk": attempt.pk}),
            {"confirm": "1"}
        )
        resp = client.get(reverse("exam_result", kwargs={"course_slug": course.slug, "attempt_pk": attempt.pk}))
        assert resp.status_code == 200
        content = resp.content.decode("utf-8")
        assert "%" in content
        assert "תוצאות" in content
