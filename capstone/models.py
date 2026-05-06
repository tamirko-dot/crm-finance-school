from django.db import models
from django.utils.translation import gettext_lazy as _
from django_fsm import FSMField, transition

from content.models import Course


class CapstoneStatus(models.TextChoices):
    SUBMITTED = "submitted", _("הוגש")
    UNDER_REVIEW = "under_review", _("בבדיקה")
    PASSED = "passed", _("עבר")
    FAILED = "failed", _("נכשל")


class CapstoneSubmission(models.Model):
    user = models.ForeignKey("accounts.User", on_delete=models.CASCADE, related_name="capstone_submissions")
    course = models.ForeignKey(Course, on_delete=models.PROTECT, related_name="capstone_submissions")
    file_url = models.URLField(max_length=500)
    file_key = models.CharField(max_length=500, blank=True)
    submitted_at = models.DateTimeField(auto_now_add=True)
    status = FSMField(default=CapstoneStatus.SUBMITTED, choices=CapstoneStatus.choices)

    class Meta:
        verbose_name = _("הגשת פרויקט גמר")
        verbose_name_plural = _("הגשות פרויקט גמר")
        ordering = ["-submitted_at"]

    def __str__(self) -> str:
        return f"{self.user} / {self.course} [{self.status}]"

    @transition(field=status, source=CapstoneStatus.SUBMITTED, target=CapstoneStatus.UNDER_REVIEW)
    def begin_review(self, reviewer) -> None:
        from documents.models import AuditLog
        AuditLog.objects.create(
            user=reviewer,
            action="capstone_review_started",
            entity_type="CapstoneSubmission",
            entity_id=str(self.pk),
            metadata_json={"trainee": str(self.user)},
        )

    @transition(field=status, source=CapstoneStatus.UNDER_REVIEW, target=CapstoneStatus.PASSED)
    def mark_passed(self, reviewer) -> None:
        from documents.models import AuditLog
        AuditLog.objects.create(
            user=reviewer,
            action="capstone_passed",
            entity_type="CapstoneSubmission",
            entity_id=str(self.pk),
            metadata_json={"trainee": str(self.user)},
        )

    @transition(field=status, source=CapstoneStatus.UNDER_REVIEW, target=CapstoneStatus.FAILED)
    def mark_failed(self, reviewer) -> None:
        from documents.models import AuditLog
        AuditLog.objects.create(
            user=reviewer,
            action="capstone_failed",
            entity_type="CapstoneSubmission",
            entity_id=str(self.pk),
            metadata_json={"trainee": str(self.user)},
        )


class RubricCategory(models.TextChoices):
    ANALYSIS = "analysis", _("ניתוח פיננסי")
    RISK = "risk", _("הערכת סיכונים")
    STRUCTURE = "structure", _("מבנה העסקה")
    PRESENTATION = "presentation", _("הצגה ותקשורת")
    CONCLUSION = "conclusion", _("מסקנות והמלצות")


class CapstoneRubricScore(models.Model):
    submission = models.ForeignKey(CapstoneSubmission, on_delete=models.CASCADE, related_name="rubric_scores")
    category = models.CharField(max_length=20, choices=RubricCategory.choices)
    score = models.PositiveSmallIntegerField()
    comment_he = models.TextField(blank=True)
    scored_by = models.ForeignKey("accounts.User", on_delete=models.PROTECT, related_name="rubric_scores_given")
    scored_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _("ציון קריטריון")
        verbose_name_plural = _("ציוני קריטריונים")
        unique_together = [("submission", "category")]

    def __str__(self) -> str:
        return f"{self.submission} / {self.get_category_display()} = {self.score}"
