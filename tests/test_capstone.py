"""Phase 7 tests: capstone submission and rubric review flow."""
import io
import pytest
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
from unittest.mock import patch, MagicMock

from accounts.models import User, UserRole
from capstone.models import CapstoneSubmission, CapstoneRubricScore, CapstoneStatus
from content.models import Course, Domain
from enrollment.models import CourseEnrollment, EnrollmentStatus


# ─── fixtures ─────────────────────────────────────────────────────────────────

@pytest.fixture
def domain(db):
    return Domain.objects.create(name_he="Test", name_en="Test", slug="test-domain-p7")


@pytest.fixture
def capstone_course(db, domain):
    return Course.objects.create(
        domain=domain, title_he="פרויקט גמר", slug="c12-capstone-test",
        phase="E", course_number=96, passing_score_pct=80, is_capstone=True,
        exam_question_count=2, exam_duration_minutes=60,
    )


@pytest.fixture
def trainee(db):
    return User.objects.create_user(
        email="trainee7@test.local", username="trainee7",
        password="Test1234!", role=UserRole.TRAINEE,
    )


@pytest.fixture
def manager(db):
    return User.objects.create_user(
        email="manager7@test.local", username="manager7",
        password="Test1234!", role=UserRole.CUSTOMER_MANAGER,
    )


@pytest.fixture
def open_enrollment(db, trainee, manager, capstone_course):
    e = CourseEnrollment.objects.create(user=trainee, course=capstone_course, status=EnrollmentStatus.LOCKED)
    e.request_unlock(); e.save()
    e.approve_unlock(approved_by=manager); e.save()
    e.start_course(); e.save()
    return e


@pytest.fixture
def docx_file():
    return SimpleUploadedFile(
        "test_capstone.docx",
        b"PK\x03\x04fake-docx-content",
        content_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
    )


@pytest.fixture
def submission(db, trainee, capstone_course):
    return CapstoneSubmission.objects.create(
        user=trainee,
        course=capstone_course,
        file_url="https://example.com/file.docx",
        file_key="capstone/1/test/file.docx",
    )


# ─── access control ───────────────────────────────────────────────────────────

@pytest.mark.django_db
class TestCapstoneAccess:
    def test_unauthenticated_redirects(self, client, capstone_course):
        resp = client.get(reverse("capstone_submit", kwargs={"course_slug": capstone_course.slug}))
        assert resp.status_code == 302
        assert "login" in resp["Location"]

    def test_trainee_without_enrollment_gets_403(self, client, trainee, capstone_course):
        client.force_login(trainee)
        resp = client.get(reverse("capstone_submit", kwargs={"course_slug": capstone_course.slug}))
        assert resp.status_code == 403

    def test_trainee_with_enrollment_sees_form(self, client, trainee, open_enrollment, capstone_course):
        client.force_login(trainee)
        resp = client.get(reverse("capstone_submit", kwargs={"course_slug": capstone_course.slug}))
        assert resp.status_code == 200

    def test_trainee_cannot_review(self, client, trainee, submission):
        client.force_login(trainee)
        resp = client.get(reverse("capstone_review", kwargs={"pk": submission.pk}))
        assert resp.status_code == 403

    def test_manager_can_review(self, client, manager, submission):
        client.force_login(manager)
        resp = client.get(reverse("capstone_review", kwargs={"pk": submission.pk}))
        assert resp.status_code == 200


# ─── submission upload ────────────────────────────────────────────────────────

@pytest.mark.django_db
class TestCapstoneSubmission:
    def test_non_docx_rejected(self, client, trainee, open_enrollment, capstone_course):
        client.force_login(trainee)
        pdf = SimpleUploadedFile("report.pdf", b"PDF content", content_type="application/pdf")
        resp = client.post(
            reverse("capstone_submit", kwargs={"course_slug": capstone_course.slug}),
            {"capstone_file": pdf},
        )
        assert resp.status_code == 302
        assert not CapstoneSubmission.objects.filter(user=trainee).exists()

    def test_oversized_file_rejected(self, client, trainee, open_enrollment, capstone_course):
        client.force_login(trainee)
        big = SimpleUploadedFile("big.docx", b"x" * (26 * 1024 * 1024), content_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document")
        resp = client.post(
            reverse("capstone_submit", kwargs={"course_slug": capstone_course.slug}),
            {"capstone_file": big},
        )
        assert resp.status_code == 302
        assert not CapstoneSubmission.objects.filter(user=trainee).exists()

    def test_valid_docx_creates_submission(self, client, trainee, open_enrollment, capstone_course, docx_file):
        client.force_login(trainee)
        with patch("capstone.views.StorageService") as MockStorage:
            mock_instance = MagicMock()
            mock_instance.upload.return_value = "capstone/key.docx"
            mock_instance.get_url.return_value = "https://storage.example.com/file.docx"
            MockStorage.return_value = mock_instance
            resp = client.post(
                reverse("capstone_submit", kwargs={"course_slug": capstone_course.slug}),
                {"capstone_file": docx_file},
            )
        assert resp.status_code == 302
        assert CapstoneSubmission.objects.filter(user=trainee, course=capstone_course).exists()

    def test_submission_status_is_submitted(self, client, trainee, open_enrollment, capstone_course, docx_file):
        client.force_login(trainee)
        with patch("capstone.views.StorageService") as MockStorage:
            mock_instance = MagicMock()
            mock_instance.get_url.return_value = "https://storage.example.com/file.docx"
            MockStorage.return_value = mock_instance
            client.post(
                reverse("capstone_submit", kwargs={"course_slug": capstone_course.slug}),
                {"capstone_file": docx_file},
            )
        sub = CapstoneSubmission.objects.get(user=trainee, course=capstone_course)
        assert sub.status == CapstoneStatus.SUBMITTED


# ─── rubric review ────────────────────────────────────────────────────────────

@pytest.mark.django_db
class TestCapstoneReview:
    def _rubric_data(self, action="pass"):
        data = {"action": action}
        for cat in ("analysis", "risk", "structure", "presentation", "conclusion"):
            data[f"score_{cat}"] = "4"
            data[f"comment_{cat}"] = ""
        return data

    def test_viewing_submission_transitions_to_under_review(self, client, manager, submission):
        client.force_login(manager)
        client.get(reverse("capstone_review", kwargs={"pk": submission.pk}))
        submission.refresh_from_db()
        assert submission.status == CapstoneStatus.UNDER_REVIEW

    def test_pass_action_marks_passed(self, client, manager, submission):
        submission.begin_review(reviewer=manager); submission.save()
        client.force_login(manager)
        client.post(
            reverse("capstone_review", kwargs={"pk": submission.pk}),
            self._rubric_data(action="pass"),
        )
        submission.refresh_from_db()
        assert submission.status == CapstoneStatus.PASSED

    def test_fail_action_marks_failed(self, client, manager, submission):
        submission.begin_review(reviewer=manager); submission.save()
        client.force_login(manager)
        client.post(
            reverse("capstone_review", kwargs={"pk": submission.pk}),
            self._rubric_data(action="fail"),
        )
        submission.refresh_from_db()
        assert submission.status == CapstoneStatus.FAILED

    def test_rubric_scores_created(self, client, manager, submission):
        submission.begin_review(reviewer=manager); submission.save()
        client.force_login(manager)
        client.post(
            reverse("capstone_review", kwargs={"pk": submission.pk}),
            self._rubric_data(action="pass"),
        )
        assert CapstoneRubricScore.objects.filter(submission=submission).count() == 5

    def test_invalid_score_rejected(self, client, manager, submission):
        submission.begin_review(reviewer=manager); submission.save()
        client.force_login(manager)
        data = self._rubric_data(action="pass")
        data["score_analysis"] = "9"
        resp = client.post(
            reverse("capstone_review", kwargs={"pk": submission.pk}),
            data,
        )
        submission.refresh_from_db()
        assert submission.status == CapstoneStatus.UNDER_REVIEW

    def test_auto_action_passes_on_high_avg(self, client, manager, submission):
        submission.begin_review(reviewer=manager); submission.save()
        client.force_login(manager)
        data = self._rubric_data(action="auto")
        for cat in ("analysis", "risk", "structure", "presentation", "conclusion"):
            data[f"score_{cat}"] = "4"
        client.post(reverse("capstone_review", kwargs={"pk": submission.pk}), data)
        submission.refresh_from_db()
        assert submission.status == CapstoneStatus.PASSED

    def test_auto_action_fails_on_low_avg(self, client, manager, submission):
        submission.begin_review(reviewer=manager); submission.save()
        client.force_login(manager)
        data = self._rubric_data(action="auto")
        for cat in ("analysis", "risk", "structure", "presentation", "conclusion"):
            data[f"score_{cat}"] = "2"
        client.post(reverse("capstone_review", kwargs={"pk": submission.pk}), data)
        submission.refresh_from_db()
        assert submission.status == CapstoneStatus.FAILED
