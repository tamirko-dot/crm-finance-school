from django.contrib import admin
from .models import CapstoneSubmission, CapstoneRubricScore


class CapstoneRubricScoreInline(admin.TabularInline):
    model = CapstoneRubricScore
    extra = 0
    fields = ("category", "score", "comment_he", "scored_by", "scored_at")
    readonly_fields = ("scored_at",)
    raw_id_fields = ("scored_by",)


@admin.register(CapstoneSubmission)
class CapstoneSubmissionAdmin(admin.ModelAdmin):
    list_display = ("user", "course", "status", "submitted_at")
    list_filter = ("status",)
    search_fields = ("user__email", "user__full_name_he")
    raw_id_fields = ("user", "course")
    readonly_fields = ("submitted_at",)
    ordering = ["-submitted_at"]
    inlines = [CapstoneRubricScoreInline]
