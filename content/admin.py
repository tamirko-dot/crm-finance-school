from django.contrib import admin
from .models import (
    Domain, Course, Module, ModuleComponent,
    Tag, Question, QuestionOption, QuestionExplanation,
)


@admin.register(Domain)
class DomainAdmin(admin.ModelAdmin):
    list_display = ("name_he", "name_en", "slug", "display_order", "is_active")
    search_fields = ("name_he", "name_en", "slug")
    prepopulated_fields = {"slug": ("name_en",)}
    ordering = ["display_order"]


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("course_number", "title_he", "domain", "phase", "passing_score_pct", "is_capstone", "is_active")
    list_filter = ("domain", "phase", "is_capstone", "is_active")
    search_fields = ("title_he", "slug")
    prepopulated_fields = {"slug": ("course_number", "title_he")}
    ordering = ["course_number"]


class ModuleInline(admin.TabularInline):
    model = Module
    extra = 0
    fields = ("module_number", "title_he", "slug", "estimated_minutes", "is_active")


class ModuleComponentInline(admin.TabularInline):
    model = ModuleComponent
    extra = 0
    fields = ("component_type", "order", "instructions_he", "is_active")


@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    list_display = ("__str__", "course", "module_number", "estimated_minutes", "is_active")
    list_filter = ("course__domain", "course", "is_active")
    search_fields = ("title_he", "slug")
    ordering = ["course__course_number", "module_number"]
    inlines = [ModuleComponentInline]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("name_he", "name_en", "slug")
    prepopulated_fields = {"slug": ("name_en",)}


class QuestionOptionInline(admin.TabularInline):
    model = QuestionOption
    extra = 4
    fields = ("display_order", "text_he", "is_correct", "distractor_rationale_he")


class QuestionExplanationInline(admin.StackedInline):
    model = QuestionExplanation
    extra = 1
    fields = ("explanation_html_he",)


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = (
        "question_id_external", "course", "module", "question_type",
        "difficulty", "usage_context", "points", "version", "is_active",
    )
    list_filter = ("course", "question_type", "difficulty", "usage_context", "is_active")
    search_fields = ("question_id_external", "stem_html_he")
    filter_horizontal = ("topic_tags",)
    readonly_fields = ("version", "created_at", "updated_at")
    inlines = [QuestionOptionInline, QuestionExplanationInline]
    ordering = ["course__course_number", "question_id_external"]
