from django.contrib import admin
from .models import ExamAttempt, ExamAttemptQuestion


class ExamAttemptQuestionInline(admin.TabularInline):
    model = ExamAttemptQuestion
    extra = 0
    fields = ("display_order", "question", "user_answer_option_index", "is_correct", "confidence", "answered_at")
    readonly_fields = (
        "display_order", "question", "stem_html_snapshot", "options_snapshot_json",
        "correct_option_index_snapshot", "user_answer_option_index", "is_correct",
        "confidence", "answered_at", "question_version_at_attempt",
    )
    can_delete = False

    def has_add_permission(self, request, obj=None):
        return False


@admin.register(ExamAttempt)
class ExamAttemptAdmin(admin.ModelAdmin):
    list_display = ("user", "course", "attempt_number", "status", "score_pct", "passed", "started_at", "submitted_at")
    list_filter = ("status", "passed", "course__domain", "course")
    search_fields = ("user__email", "user__full_name_he", "course__title_he")
    raw_id_fields = ("user", "course")
    readonly_fields = ("started_at", "submitted_at", "score_pct", "passed", "is_locked")
    ordering = ["-started_at"]
    inlines = [ExamAttemptQuestionInline]

    def has_change_permission(self, request, obj=None):
        if obj and obj.is_locked:
            return False
        return super().has_change_permission(request, obj)
