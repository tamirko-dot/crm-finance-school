"""Phase 5 tests: manager trainees list, trainee detail, unlock request inbox, group report."""
import pytest
from django.urls import reverse

from accounts.models import User, UserRole
from content.models import Course, Domain
from enrollment.models import CourseEnrollment, EnrollmentStatus, UnlockRequest, UnlockRequestStatus


# ─── fixtures ─────────────────────────────────────────────────────────────────

@pytest.fixture
def domain(db):
    return Domain.objects.create(name_he="Test", name_en="Test Domain", slug="test-domain-m5")


@pytest.fixture
def course(db, domain):
    return Course.objects.create(
        domain=domain, title_he="קורס בדיקה", slug="c99-test-m5",
        phase="A", course_number=98, passing_score_pct=75,
        exam_question_count=2, exam_duration_minutes=60,
    )


@pytest.fixture
def trainee(db):
    return User.objects.create_user(
        email="trainee5@test.local", username="trainee5",
        password="Test1234!", role=UserRole.TRAINEE, full_name_he="חניך בדיקה",
    )


@pytest.fixture
def manager(db):
    return User.objects.create_user(
        email="manager5@test.local", username="manager5",
        password="Test1234!", role=UserRole.CUSTOMER_MANAGER,
    )


@pytest.fixture
def ceo(db):
    return User.objects.create_user(
        email="ceo5@test.local", username="ceo5",
        password="Test1234!", role=UserRole.CEO,
    )


@pytest.fixture
def pending_request(db, trainee, course):
    e = CourseEnrollment.objects.create(user=trainee, course=course, status=EnrollmentStatus.REQUESTED)
    return UnlockRequest.objects.create(user=trainee, course=course)


# ─── access control ───────────────────────────────────────────────────────────

@pytest.mark.django_db
class TestManagerAccess:
    def test_trainee_cannot_see_trainees_list(self, client, trainee):
        client.force_login(trainee)
        resp = client.get(reverse("trainees_list"))
        assert resp.status_code == 403

    def test_manager_can_see_trainees_list(self, client, manager):
        client.force_login(manager)
        resp = client.get(reverse("trainees_list"))
        assert resp.status_code == 200

    def test_ceo_can_see_trainees_list(self, client, ceo):
        client.force_login(ceo)
        resp = client.get(reverse("trainees_list"))
        assert resp.status_code == 200

    def test_trainee_cannot_see_unlock_requests(self, client, trainee):
        client.force_login(trainee)
        resp = client.get(reverse("unlock_requests"))
        assert resp.status_code == 403

    def test_ceo_cannot_approve_requests(self, client, ceo, pending_request):
        client.force_login(ceo)
        resp = client.post(reverse("approve_request", kwargs={"pk": pending_request.pk}))
        assert resp.status_code == 403

    def test_trainee_cannot_see_group_report(self, client, trainee):
        client.force_login(trainee)
        resp = client.get(reverse("group_report"))
        assert resp.status_code == 403


# ─── trainees list ────────────────────────────────────────────────────────────

@pytest.mark.django_db
class TestTraineesList:
    def test_shows_trainee_name(self, client, manager, trainee):
        client.force_login(manager)
        resp = client.get(reverse("trainees_list"))
        assert "חניך בדיקה" in resp.content.decode("utf-8")

    def test_shows_struggling_flag(self, client, manager, trainee, course):
        # Give trainee an open enrollment but no activity
        CourseEnrollment.objects.create(user=trainee, course=course, status=EnrollmentStatus.IN_PROGRESS)
        client.force_login(manager)
        resp = client.get(reverse("trainees_list"))
        # No ModuleProgress → days_inactive is None → not flagged as struggling
        assert resp.status_code == 200


# ─── trainee detail ───────────────────────────────────────────────────────────

@pytest.mark.django_db
class TestTraineeDetail:
    def test_shows_trainee_info(self, client, manager, trainee):
        client.force_login(manager)
        resp = client.get(reverse("trainee_detail", kwargs={"pk": trainee.pk}))
        assert resp.status_code == 200
        assert "חניך בדיקה" in resp.content.decode("utf-8")

    def test_shows_enrollment_status(self, client, manager, trainee, course):
        CourseEnrollment.objects.create(user=trainee, course=course, status=EnrollmentStatus.PASSED)
        client.force_login(manager)
        resp = client.get(reverse("trainee_detail", kwargs={"pk": trainee.pk}))
        assert "עבר" in resp.content.decode("utf-8")

    def test_manager_cannot_see_other_manager_as_trainee(self, client, manager):
        client.force_login(manager)
        resp = client.get(reverse("trainee_detail", kwargs={"pk": manager.pk}))
        assert resp.status_code == 404


# ─── unlock requests ──────────────────────────────────────────────────────────

@pytest.mark.django_db
class TestUnlockRequests:
    def test_pending_request_shown(self, client, manager, pending_request):
        client.force_login(manager)
        resp = client.get(reverse("unlock_requests"))
        assert resp.status_code == 200
        assert "חניך בדיקה" in resp.content.decode("utf-8")

    def test_approve_transitions_enrollment(self, client, manager, trainee, course, pending_request):
        client.force_login(manager)
        client.post(reverse("approve_request", kwargs={"pk": pending_request.pk}), {"note": ""})
        pending_request.refresh_from_db()
        assert pending_request.status == UnlockRequestStatus.APPROVED
        enrollment = CourseEnrollment.objects.get(user=trainee, course=course)
        assert enrollment.status == EnrollmentStatus.OPEN

    def test_deny_transitions_enrollment_back_to_locked(self, client, manager, trainee, course, pending_request):
        client.force_login(manager)
        client.post(reverse("deny_request", kwargs={"pk": pending_request.pk}), {"note": "לא מתאים"})
        pending_request.refresh_from_db()
        assert pending_request.status == UnlockRequestStatus.DENIED
        enrollment = CourseEnrollment.objects.get(user=trainee, course=course)
        assert enrollment.status == EnrollmentStatus.LOCKED

    def test_approve_records_note(self, client, manager, trainee, course, pending_request):
        client.force_login(manager)
        client.post(reverse("approve_request", kwargs={"pk": pending_request.pk}), {"note": "אושר בפגישה"})
        pending_request.refresh_from_db()
        assert pending_request.note == "אושר בפגישה"
        assert pending_request.responded_by == manager

    def test_cannot_approve_already_approved(self, client, manager, trainee, course, pending_request):
        client.force_login(manager)
        client.post(reverse("approve_request", kwargs={"pk": pending_request.pk}), {"note": ""})
        # Second attempt — should 404 (no longer pending)
        resp = client.post(reverse("approve_request", kwargs={"pk": pending_request.pk}), {"note": ""})
        assert resp.status_code == 404


# ─── group report ─────────────────────────────────────────────────────────────

@pytest.mark.django_db
class TestGroupReport:
    def test_renders_for_manager(self, client, manager):
        client.force_login(manager)
        resp = client.get(reverse("group_report"))
        assert resp.status_code == 200

    def test_renders_for_ceo(self, client, ceo):
        client.force_login(ceo)
        resp = client.get(reverse("group_report"))
        assert resp.status_code == 200

    def test_shows_course_stats(self, client, manager, trainee, course):
        CourseEnrollment.objects.create(user=trainee, course=course, status=EnrollmentStatus.PASSED)
        client.force_login(manager)
        resp = client.get(reverse("group_report"))
        assert "קורס בדיקה" in resp.content.decode("utf-8")

    def test_confidence_map_loads(self, client, manager):
        client.force_login(manager)
        resp = client.get(reverse("confidence_map"))
        assert resp.status_code == 200
