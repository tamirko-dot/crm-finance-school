import json

from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django_fsm import FSMField, transition

from content.models import Course, Question


class AttemptStatus(models.TextChoices):
    IN_PROGRESS = "in_progress", _("בתהליך")
    SUBMITTED = "submitted", _("הוגש")
    GRADED = "graded", _("נוקד")


class ConfidenceLevel(models.TextChoices):
    CONFIDENT = "confident", _("בטוח")
    NOT_SURE = "not_sure", _("לא בטוח")


class ExamAttempt(models.Model):
    user = models.ForeignKey("accounts.User", on_delete=models.CASCADE, related_name="exam_attempts")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="exam_attempts")
    attempt_number = models.PositiveSmallIntegerField(default=1)
    status = FSMField(default=AttemptStatus.IN_PROGRESS, choices=AttemptStatus.choices)
    started_at = models.DateTimeField(auto_now_add=True)
    submitted_at = models.DateTimeField(null=True, blank=True)
    score_pct = models.FloatField(null=True, blank=True)
    passed = models.BooleanField(null=True, blank=True)
    time_remaining_seconds_snapshot = models.IntegerField(null=True, blank=True)
    is_locked = models.BooleanField(default=False)

    class Meta:
        verbose_name = _("ניסיון מבחן")
        verbose_name_plural = _("ניסיונות מבחן")
        ordering = ["-started_at"]
        unique_together = [("user", "course", "attempt_number")]

    def __str__(self) -> str:
        return f"{self.user} / {self.course} #{self.attempt_number} [{self.status}]"

    @transition(field=status, source=AttemptStatus.IN_PROGRESS, target=AttemptStatus.SUBMITTED)
    def submit(self) -> None:
        self.submitted_at = timezone.now()
        self.is_locked = True

    @transition(field=status, source=AttemptStatus.SUBMITTED, target=AttemptStatus.GRADED)
    def grade(self, score_pct: float) -> None:
        self.score_pct = score_pct
        self.passed = score_pct >= self.course.passing_score_pct
        from documents.models import AuditLog
        AuditLog.objects.create(
            user=self.user,
            action="exam_graded",
            entity_type="ExamAttempt",
            entity_id=str(self.pk),
            metadata_json={
                "course_slug": self.course.slug,
                "score_pct": score_pct,
                "passed": self.passed,
                "attempt_number": self.attempt_number,
            },
        )

    def deadline_at(self):
        if self.started_at and self.course.exam_duration_minutes:
            from datetime import timedelta
            return self.started_at + timedelta(minutes=self.course.exam_duration_minutes)
        return None


class ExamAttemptQuestion(models.Model):
    attempt = models.ForeignKey(ExamAttempt, on_delete=models.CASCADE, related_name="attempt_questions")
    display_order = models.PositiveSmallIntegerField()
    question = models.ForeignKey(
        Question, on_delete=models.SET_NULL, null=True, related_name="attempt_records"
    )
    question_version_at_attempt = models.PositiveIntegerField()
    stem_html_snapshot = models.TextField()
    options_snapshot_json = models.JSONField()
    correct_option_index_snapshot = models.PositiveSmallIntegerField()
    senior_insight_snapshot_he = models.TextField(blank=True)
    explanation_snapshot_html_he = models.TextField(blank=True)
    user_answer_option_index = models.SmallIntegerField(null=True, blank=True)
    confidence = models.CharField(
        max_length=10, choices=ConfidenceLevel.choices, null=True, blank=True
    )
    answered_at = models.DateTimeField(null=True, blank=True)
    is_correct = models.BooleanField(null=True, blank=True)

    class Meta:
        verbose_name = _("שאלת ניסיון")
        verbose_name_plural = _("שאלות ניסיון")
        ordering = ["display_order"]
        unique_together = [("attempt", "display_order")]

    def __str__(self) -> str:
        return f"{self.attempt} / שאלה {self.display_order}"

    @classmethod
    def snapshot_from_question(cls, attempt: ExamAttempt, question: Question, order: int) -> "ExamAttemptQuestion":
        options = list(question.options.order_by("display_order").values("text_he", "is_correct", "distractor_rationale_he"))
        correct_idx = next((i for i, o in enumerate(options) if o["is_correct"]), 0)
        explanation_html = ""
        if hasattr(question, "explanation"):
            explanation_html = question.explanation.explanation_html_he
        return cls(
            attempt=attempt,
            display_order=order,
            question=question,
            question_version_at_attempt=question.version,
            stem_html_snapshot=question.stem_html_he,
            options_snapshot_json=options,
            correct_option_index_snapshot=correct_idx,
            senior_insight_snapshot_he=question.senior_insight_he,
            explanation_snapshot_html_he=explanation_html,
        )
