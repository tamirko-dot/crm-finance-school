import pytest
from django_fsm import TransitionNotAllowed

from accounts.models import User, UserRole
from content.models import Course, Domain
from enrollment.models import CourseEnrollment, EnrollmentStatus, UnlockRequest


@pytest.mark.django_db
class TestUserModel:
    def test_display_name_uses_full_name_he(self, trainee):
        trainee.full_name_he = "ישראל ישראלי"
        trainee.save()
        assert trainee.display_name == "ישראל ישראלי"

    def test_display_name_falls_back_to_username(self, trainee):
        trainee.full_name_he = ""
        trainee.save()
        assert trainee.display_name == trainee.username

    def test_str_returns_name_or_email(self, trainee):
        assert str(trainee) in (trainee.full_name_he, trainee.email)


@pytest.fixture
def domain(db):
    return Domain.objects.create(name_he="Test Domain", name_en="Test Domain", slug="test-domain")


@pytest.fixture
def course(db, domain):
    return Course.objects.create(
        domain=domain,
        title_he="קורס בדיקה",
        slug="test-course",
        phase="A",
        course_number=99,
        passing_score_pct=75,
    )


@pytest.mark.django_db
class TestCourseEnrollmentFSM:
    def test_initial_status_is_locked(self, trainee, course):
        e = CourseEnrollment.objects.create(user=trainee, course=course)
        assert e.status == EnrollmentStatus.LOCKED

    def test_request_unlock_transition(self, trainee, course):
        e = CourseEnrollment.objects.create(user=trainee, course=course)
        e.request_unlock()
        e.save()
        assert e.status == EnrollmentStatus.REQUESTED

    def test_approve_unlock_transition(self, trainee, manager, course):
        e = CourseEnrollment.objects.create(user=trainee, course=course, status=EnrollmentStatus.REQUESTED)
        e.approve_unlock(approved_by=manager)
        e.save()
        assert e.status == EnrollmentStatus.OPEN
        assert e.unlocked_by == manager

    def test_cannot_skip_from_locked_to_open(self, trainee, course):
        e = CourseEnrollment.objects.create(user=trainee, course=course)
        with pytest.raises(TransitionNotAllowed):
            e.approve_unlock(approved_by=trainee)

    def test_deny_unlock_returns_to_locked(self, trainee, manager, course):
        e = CourseEnrollment.objects.create(user=trainee, course=course, status=EnrollmentStatus.REQUESTED)
        e.deny_unlock(denied_by=manager)
        e.save()
        assert e.status == EnrollmentStatus.LOCKED

    def test_mark_passed_sets_completed_at(self, trainee, course):
        e = CourseEnrollment.objects.create(user=trainee, course=course, status=EnrollmentStatus.IN_PROGRESS)
        e.mark_passed()
        e.save()
        assert e.status == EnrollmentStatus.PASSED
        assert e.completed_at is not None

    def test_cannot_double_request(self, trainee, course):
        e = CourseEnrollment.objects.create(user=trainee, course=course, status=EnrollmentStatus.REQUESTED)
        with pytest.raises(TransitionNotAllowed):
            e.request_unlock()
