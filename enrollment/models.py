from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django_fsm import FSMField, transition

from content.models import Course, Module, ModuleComponent


class EnrollmentStatus(models.TextChoices):
    LOCKED = "locked", _("נעול")
    REQUESTED = "requested", _("ממתין לאישור")
    OPEN = "open", _("פתוח")
    IN_PROGRESS = "in_progress", _("בתהליך")
    PASSED = "passed", _("עבר")
    FAILED = "failed", _("נכשל")


class CourseEnrollment(models.Model):
    user = models.ForeignKey("accounts.User", on_delete=models.CASCADE, related_name="enrollments")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="enrollments")
    status = FSMField(default=EnrollmentStatus.LOCKED, choices=EnrollmentStatus.choices)
    unlocked_by = models.ForeignKey(
        "accounts.User", on_delete=models.SET_NULL, null=True, blank=True, related_name="enrollments_unlocked"
    )
    unlocked_at = models.DateTimeField(null=True, blank=True)
    completed_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("הרשמה לקורס")
        verbose_name_plural = _("הרשמות לקורסים")
        unique_together = [("user", "course")]

    def __str__(self) -> str:
        return f"{self.user} / {self.course} [{self.status}]"

    @transition(field=status, source=EnrollmentStatus.LOCKED, target=EnrollmentStatus.REQUESTED)
    def request_unlock(self) -> None:
        self._log_action("request_unlock")

    @transition(field=status, source=EnrollmentStatus.REQUESTED, target=EnrollmentStatus.OPEN)
    def approve_unlock(self, approved_by) -> None:
        self.unlocked_by = approved_by
        self.unlocked_at = timezone.now()
        self._log_action("approve_unlock", actor=approved_by)

    @transition(field=status, source=EnrollmentStatus.REQUESTED, target=EnrollmentStatus.LOCKED)
    def deny_unlock(self, denied_by) -> None:
        self._log_action("deny_unlock", actor=denied_by)

    @transition(field=status, source=EnrollmentStatus.OPEN, target=EnrollmentStatus.IN_PROGRESS)
    def start_course(self) -> None:
        self._log_action("start_course")

    @transition(field=status, source=EnrollmentStatus.IN_PROGRESS, target=EnrollmentStatus.PASSED)
    def mark_passed(self) -> None:
        self.completed_at = timezone.now()
        self._log_action("mark_passed")

    @transition(field=status, source=EnrollmentStatus.IN_PROGRESS, target=EnrollmentStatus.FAILED)
    def mark_failed(self) -> None:
        self._log_action("mark_failed")

    @transition(
        field=status,
        source=[EnrollmentStatus.FAILED, EnrollmentStatus.LOCKED],
        target=EnrollmentStatus.OPEN,
    )
    def admin_reopen(self, reopened_by) -> None:
        self.unlocked_by = reopened_by
        self.unlocked_at = timezone.now()
        self._log_action("admin_reopen", actor=reopened_by)

    def _log_action(self, action: str, actor=None) -> None:
        from documents.models import AuditLog
        AuditLog.objects.create(
            user=actor or self.user,
            action=action,
            entity_type="CourseEnrollment",
            entity_id=str(self.pk or ""),
            metadata_json={"course_slug": self.course.slug, "target_user": str(self.user)},
        )


class UnlockRequestStatus(models.TextChoices):
    PENDING = "pending", _("ממתין")
    APPROVED = "approved", _("אושר")
    DENIED = "denied", _("נדחה")


class UnlockRequest(models.Model):
    user = models.ForeignKey("accounts.User", on_delete=models.CASCADE, related_name="unlock_requests")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="unlock_requests")
    status = FSMField(default=UnlockRequestStatus.PENDING, choices=UnlockRequestStatus.choices)
    requested_at = models.DateTimeField(auto_now_add=True)
    responded_by = models.ForeignKey(
        "accounts.User", on_delete=models.SET_NULL, null=True, blank=True, related_name="unlock_responses"
    )
    responded_at = models.DateTimeField(null=True, blank=True)
    note = models.TextField(blank=True)

    class Meta:
        verbose_name = _("בקשת פתיחת קורס")
        verbose_name_plural = _("בקשות פתיחת קורס")
        ordering = ["-requested_at"]

    def __str__(self) -> str:
        return f"{self.user} → {self.course} [{self.status}]"

    @transition(field=status, source=UnlockRequestStatus.PENDING, target=UnlockRequestStatus.APPROVED)
    def approve(self, approved_by, note: str = "") -> None:
        self.responded_by = approved_by
        self.responded_at = timezone.now()
        self.note = note
        enrollment, _ = CourseEnrollment.objects.get_or_create(
            user=self.user, course=self.course, defaults={"status": "locked"}
        )
        if enrollment.status == "locked":
            enrollment.request_unlock()
            enrollment.save()
        enrollment.approve_unlock(approved_by=approved_by)
        enrollment.save()

    @transition(field=status, source=UnlockRequestStatus.PENDING, target=UnlockRequestStatus.DENIED)
    def deny(self, denied_by, note: str = "") -> None:
        self.responded_by = denied_by
        self.responded_at = timezone.now()
        self.note = note


class ModuleProgress(models.Model):
    user = models.ForeignKey("accounts.User", on_delete=models.CASCADE, related_name="module_progress")
    module = models.ForeignKey(Module, on_delete=models.CASCADE, related_name="progress_records")
    started_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(null=True, blank=True)
    is_completed = models.BooleanField(default=False)
    practice_score_pct = models.FloatField(null=True, blank=True)

    class Meta:
        verbose_name = _("התקדמות מודול")
        verbose_name_plural = _("התקדמות מודולים")
        unique_together = [("user", "module")]

    def __str__(self) -> str:
        return f"{self.user} / {self.module}"


class ComponentProgress(models.Model):
    user = models.ForeignKey("accounts.User", on_delete=models.CASCADE, related_name="component_progress")
    component = models.ForeignKey(ModuleComponent, on_delete=models.CASCADE, related_name="progress_records")
    is_completed = models.BooleanField(default=False)
    completed_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name = _("התקדמות רכיב")
        verbose_name_plural = _("התקדמות רכיבים")
        unique_together = [("user", "component")]

    def __str__(self) -> str:
        return f"{self.user} / {self.component}"
