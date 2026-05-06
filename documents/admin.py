from django.contrib import admin
from .models import DocumentTag, LearningDocument, DocumentAccessLog, AuditLog, Notification


@admin.register(DocumentTag)
class DocumentTagAdmin(admin.ModelAdmin):
    list_display = ("name_he", "name_en", "slug")
    prepopulated_fields = {"slug": ("name_en",)}


@admin.register(LearningDocument)
class LearningDocumentAdmin(admin.ModelAdmin):
    list_display = ("title_he", "domain", "file_type", "is_active", "created_at")
    list_filter = ("domain", "file_type", "is_active")
    search_fields = ("title_he", "description_he")
    filter_horizontal = ("tags",)
    readonly_fields = ("created_at", "updated_at")
    ordering = ["-created_at"]


@admin.register(DocumentAccessLog)
class DocumentAccessLogAdmin(admin.ModelAdmin):
    list_display = ("user", "document", "accessed_at")
    raw_id_fields = ("user", "document")
    readonly_fields = ("accessed_at",)
    ordering = ["-accessed_at"]

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False


@admin.register(AuditLog)
class AuditLogAdmin(admin.ModelAdmin):
    list_display = ("user", "action", "entity_type", "entity_id", "created_at")
    list_filter = ("action", "entity_type")
    search_fields = ("user__email", "action", "entity_type", "entity_id")
    readonly_fields = ("user", "action", "entity_type", "entity_id", "metadata_json", "created_at")
    ordering = ["-created_at"]

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ("user", "type", "created_at", "sent_at")
    list_filter = ("type",)
    search_fields = ("user__email", "type")
    readonly_fields = ("created_at",)
    ordering = ["-created_at"]
