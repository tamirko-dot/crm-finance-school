from django.contrib import admin
from .models import CourseEnrollment, UnlockRequest, ModuleProgress, ComponentProgress


@admin.register(CourseEnrollment)
class CourseEnrollmentAdmin(admin.ModelAdmin):
    list_display = ("user", "course", "status", "unlocked_by", "unlocked_at", "completed_at")
    list_filter = ("status", "course__domain", "course")
    search_fields = ("user__email", "user__full_name_he", "course__title_he")
    raw_id_fields = ("user", "course", "unlocked_by")
    readonly_fields = ("status", "created_at", "updated_at")
    ordering = ["-created_at"]


@admin.register(UnlockRequest)
class UnlockRequestAdmin(admin.ModelAdmin):
    list_display = ("user", "course", "status", "requested_at", "responded_by", "responded_at")
    list_filter = ("status", "course__domain")
    search_fields = ("user__email", "user__full_name_he", "course__title_he")
    raw_id_fields = ("user", "course", "responded_by")
    readonly_fields = ("status", "requested_at", "responded_at", "responded_by")
    ordering = ["-requested_at"]


@admin.register(ModuleProgress)
class ModuleProgressAdmin(admin.ModelAdmin):
    list_display = ("user", "module", "is_completed", "practice_score_pct", "started_at", "completed_at")
    list_filter = ("is_completed",)
    search_fields = ("user__email", "module__title_he")
    raw_id_fields = ("user", "module")
    ordering = ["-started_at"]


@admin.register(ComponentProgress)
class ComponentProgressAdmin(admin.ModelAdmin):
    list_display = ("user", "component", "is_completed", "completed_at")
    list_filter = ("is_completed",)
    raw_id_fields = ("user", "component")
