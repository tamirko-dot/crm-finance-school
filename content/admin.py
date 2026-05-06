import json

from django.contrib import admin, messages
from django.http import HttpResponse
from django.utils.html import format_html

from .models import (
    Domain, Course, Module, ModuleComponent,
    Tag, Question, QuestionOption, QuestionExplanation,
)


# ─── domain ───────────────────────────────────────────────────────────────────

@admin.register(Domain)
class DomainAdmin(admin.ModelAdmin):
    list_display = ("name_he", "name_en", "slug", "course_count", "display_order", "is_active")
    search_fields = ("name_he", "name_en", "slug")
    prepopulated_fields = {"slug": ("name_en",)}
    ordering = ["display_order"]

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related("courses")

    @admin.display(description="קורסים")
    def course_count(self, obj):
        return obj.courses.filter(is_active=True).count()


# ─── course ───────────────────────────────────────────────────────────────────

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = (
        "course_number", "title_he", "domain", "phase",
        "passing_score_pct", "module_count", "question_count", "is_capstone", "is_active",
    )
    list_filter = ("domain", "phase", "is_capstone", "is_active")
    search_fields = ("title_he", "slug", "course_number")
    ordering = ["course_number"]
    readonly_fields = ("slug",)

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related("modules", "questions")

    @admin.display(description="מודולים")
    def module_count(self, obj):
        return obj.modules.filter(is_active=True).count()

    @admin.display(description="שאלות")
    def question_count(self, obj):
        return obj.questions.filter(is_active=True).count()


# ─── module ───────────────────────────────────────────────────────────────────

class ModuleComponentInline(admin.TabularInline):
    model = ModuleComponent
    extra = 0
    fields = ("component_type", "order", "instructions_he", "is_active")
    ordering = ["order"]


@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    list_display = ("__str__", "course", "module_number", "component_count", "question_count", "estimated_minutes", "is_active")
    list_filter = ("course__domain", "course", "is_active")
    search_fields = ("title_he", "slug", "course__title_he")
    ordering = ["course__course_number", "module_number"]
    inlines = [ModuleComponentInline]

    def get_queryset(self, request):
        return super().get_queryset(request).select_related("course__domain").prefetch_related("components", "questions")

    @admin.display(description="רכיבים")
    def component_count(self, obj):
        return obj.components.count()

    @admin.display(description="שאלות")
    def question_count(self, obj):
        return obj.questions.filter(is_active=True).count()


# ─── tag ──────────────────────────────────────────────────────────────────────

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("name_he", "name_en", "slug")
    prepopulated_fields = {"slug": ("name_en",)}
    search_fields = ("name_he", "name_en")


# ─── question ─────────────────────────────────────────────────────────────────

class QuestionOptionInline(admin.TabularInline):
    model = QuestionOption
    extra = 4
    fields = ("display_order", "text_he", "is_correct", "distractor_rationale_he")
    ordering = ["display_order"]


class QuestionExplanationInline(admin.StackedInline):
    model = QuestionExplanation
    extra = 1
    fields = ("explanation_html_he",)


def _export_questions_json(modeladmin, request, queryset):
    """Admin action: export selected questions as importable JSON."""
    data = []
    for q in queryset.prefetch_related("options", "explanation", "topic_tags"):
        options = [
            {
                "text_he": opt.text_he,
                "is_correct": opt.is_correct,
                "distractor_rationale_he": opt.distractor_rationale_he,
            }
            for opt in q.options.order_by("display_order")
        ]
        explanation = ""
        if hasattr(q, "explanation"):
            explanation = q.explanation.explanation_html_he
        data.append({
            "question_id_external": q.question_id_external,
            "course_number": q.course.course_number,
            "module_number": q.module.module_number if q.module else None,
            "question_type": q.question_type,
            "difficulty": q.difficulty,
            "usage_context": q.usage_context,
            "stem_html_he": q.stem_html_he,
            "image_url": q.image_url,
            "points": q.points,
            "avg_time_seconds": q.avg_time_seconds,
            "senior_insight_he": q.senior_insight_he,
            "topic_tags": [t.slug for t in q.topic_tags.all()],
            "options": options,
            "explanation_html_he": explanation,
        })
    response = HttpResponse(
        json.dumps(data, ensure_ascii=False, indent=2),
        content_type="application/json; charset=utf-8",
    )
    response["Content-Disposition"] = "attachment; filename=questions_export.json"
    return response

_export_questions_json.short_description = "ייצוא שאלות נבחרות כ-JSON"


def _activate_questions(modeladmin, request, queryset):
    updated = queryset.update(is_active=True)
    messages.success(request, f"{updated} שאלות הופעלו.")

_activate_questions.short_description = "הפעלת שאלות נבחרות"


def _deactivate_questions(modeladmin, request, queryset):
    updated = queryset.update(is_active=False)
    messages.success(request, f"{updated} שאלות הושבתו.")

_deactivate_questions.short_description = "השבתת שאלות נבחרות"


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = (
        "question_id_external", "course", "module", "type_badge",
        "difficulty", "usage_context", "points", "option_count", "version", "is_active",
    )
    list_filter = ("course__domain", "course", "question_type", "difficulty", "usage_context", "is_active")
    search_fields = ("question_id_external", "stem_html_he", "course__title_he")
    filter_horizontal = ("topic_tags",)
    readonly_fields = ("version", "created_at", "updated_at")
    inlines = [QuestionOptionInline, QuestionExplanationInline]
    ordering = ["course__course_number", "question_id_external"]
    actions = [_export_questions_json, _activate_questions, _deactivate_questions]
    list_per_page = 50

    def get_queryset(self, request):
        return super().get_queryset(request).select_related("course", "module").prefetch_related("options")

    @admin.display(description="סוג")
    def type_badge(self, obj):
        labels = {1: "אחזור", 2: "חישוב פשוט", 3: "חישוב מורכב", 4: "ניתוח מסמך", 5: "תרחיש", 6: "סינתזה"}
        return labels.get(obj.question_type, str(obj.question_type))

    @admin.display(description="אפשרויות")
    def option_count(self, obj):
        count = obj.options.count()
        color = "#2e7d32" if count >= 4 else "#b71c1c"
        return format_html('<span style="color:{}">{}</span>', color, count)
