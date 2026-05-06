from django.db import models
from django.utils.translation import gettext_lazy as _

from content.models import Domain


class DocumentTag(models.Model):
    name_he = models.CharField(max_length=100)
    name_en = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        verbose_name = _("תג מסמך")
        verbose_name_plural = _("תגי מסמך")

    def __str__(self) -> str:
        return self.name_he


class FileType(models.TextChoices):
    PDF = "pdf", "PDF"
    DOCX = "docx", "Word"
    XLSX = "xlsx", "Excel"
    IMAGE = "image", _("תמונה")


class LearningDocument(models.Model):
    title_he = models.CharField(max_length=300)
    description_he = models.TextField(blank=True)
    file_url = models.URLField(max_length=500)
    file_key = models.CharField(max_length=500, blank=True)
    file_type = models.CharField(max_length=10, choices=FileType.choices)
    domain = models.ForeignKey(Domain, on_delete=models.PROTECT, related_name="documents")
    tags = models.ManyToManyField(DocumentTag, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("מסמך לימוד")
        verbose_name_plural = _("מסמכי לימוד")
        ordering = ["-created_at"]

    def __str__(self) -> str:
        return self.title_he


class DocumentAccessLog(models.Model):
    user = models.ForeignKey("accounts.User", on_delete=models.CASCADE, related_name="document_accesses")
    document = models.ForeignKey(LearningDocument, on_delete=models.CASCADE, related_name="access_logs")
    accessed_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _("גישה למסמך")
        verbose_name_plural = _("גישות למסמכים")
        ordering = ["-accessed_at"]

    def __str__(self) -> str:
        return f"{self.user} / {self.document} @ {self.accessed_at}"


class AuditAction(models.TextChoices):
    COURSE_UNLOCKED = "course_unlocked", _("קורס נפתח")
    EXAM_STARTED = "exam_started", _("מבחן התחיל")
    EXAM_SUBMITTED = "exam_submitted", _("מבחן הוגש")
    EXAM_GRADED = "exam_graded", _("מבחן נוקד")
    CAPSTONE_SUBMITTED = "capstone_submitted", _("פרויקט גמר הוגש")
    CAPSTONE_GRADED = "capstone_graded", _("פרויקט גמר נוקד")
    QUESTION_UPDATED = "question_updated", _("שאלה עודכנה")
    ROLE_CHANGED = "role_changed", _("תפקיד שונה")
    REQUEST_UNLOCK = "request_unlock", _("בקשת פתיחה")
    APPROVE_UNLOCK = "approve_unlock", _("אישור פתיחה")
    DENY_UNLOCK = "deny_unlock", _("דחיית פתיחה")
    START_COURSE = "start_course", _("התחלת קורס")
    MARK_PASSED = "mark_passed", _("סומן כעבר")
    MARK_FAILED = "mark_failed", _("סומן כנכשל")
    ADMIN_REOPEN = "admin_reopen", _("פתיחה מחדש")
    CAPSTONE_REVIEW_STARTED = "capstone_review_started", _("בדיקת פרויקט גמר התחילה")
    CAPSTONE_PASSED = "capstone_passed", _("פרויקט גמר עבר")
    CAPSTONE_FAILED = "capstone_failed", _("פרויקט גמר נכשל")


class AuditLog(models.Model):
    user = models.ForeignKey(
        "accounts.User", on_delete=models.SET_NULL, null=True, related_name="audit_logs"
    )
    action = models.CharField(max_length=50)
    entity_type = models.CharField(max_length=100)
    entity_id = models.CharField(max_length=100, blank=True)
    metadata_json = models.JSONField(default=dict)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _("רשומת ביקורת")
        verbose_name_plural = _("רשומות ביקורת")
        ordering = ["-created_at"]

    def __str__(self) -> str:
        return f"{self.user} / {self.action} / {self.entity_type}:{self.entity_id}"


class Notification(models.Model):
    user = models.ForeignKey("accounts.User", on_delete=models.CASCADE, related_name="notifications")
    type = models.CharField(max_length=100)
    payload_json = models.JSONField(default=dict)
    created_at = models.DateTimeField(auto_now_add=True)
    sent_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name = _("התראה")
        verbose_name_plural = _("התראות")
        ordering = ["-created_at"]

    def __str__(self) -> str:
        return f"{self.user} / {self.type} @ {self.created_at}"
