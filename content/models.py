from django.db import models
from django.utils.translation import gettext_lazy as _


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Domain(TimeStampedModel):
    name_he = models.CharField(max_length=200)
    name_en = models.CharField(max_length=200)
    description_he = models.TextField(blank=True)
    slug = models.SlugField(max_length=100, unique=True)
    display_order = models.PositiveSmallIntegerField(default=0)

    class Meta:
        verbose_name = _("תחום")
        verbose_name_plural = _("תחומים")
        ordering = ["display_order"]

    def __str__(self) -> str:
        return self.name_he


class CoursePhase(models.TextChoices):
    A = "A", "שלב א'"
    B = "B", "שלב ב'"
    C = "C", "שלב ג'"
    D = "D", "שלב ד'"
    E = "E", "שלב ה'"


class Course(TimeStampedModel):
    domain = models.ForeignKey(Domain, on_delete=models.PROTECT, related_name="courses")
    title_he = models.CharField(max_length=300)
    description_he = models.TextField(blank=True)
    slug = models.SlugField(max_length=150, unique=True)
    phase = models.CharField(max_length=1, choices=CoursePhase.choices)
    course_number = models.PositiveSmallIntegerField()
    passing_score_pct = models.PositiveSmallIntegerField(default=75)
    exam_question_count = models.PositiveSmallIntegerField(default=20)
    exam_duration_minutes = models.PositiveSmallIntegerField(default=60)
    is_capstone = models.BooleanField(default=False)

    class Meta:
        verbose_name = _("קורס")
        verbose_name_plural = _("קורסים")
        ordering = ["course_number"]
        unique_together = [("domain", "course_number")]

    def __str__(self) -> str:
        return f"C{self.course_number:02d} — {self.title_he}"


class Module(TimeStampedModel):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="modules")
    title_he = models.CharField(max_length=300)
    slug = models.SlugField(max_length=150)
    module_number = models.PositiveSmallIntegerField()
    estimated_minutes = models.PositiveSmallIntegerField(default=30)

    class Meta:
        verbose_name = _("מודול")
        verbose_name_plural = _("מודולים")
        ordering = ["module_number"]
        unique_together = [("course", "slug"), ("course", "module_number")]

    def __str__(self) -> str:
        return f"{self.course} / M{self.module_number:02d} — {self.title_he}"


class ComponentType(models.TextChoices):
    READING = "reading", _("קריאה")
    COMPREHENSION = "comprehension", _("בדיקת הבנה")
    EXERCISES = "exercises", _("תרגילים")
    SUMMARY = "summary", _("סיכום")


class ModuleComponent(TimeStampedModel):
    module = models.ForeignKey(Module, on_delete=models.CASCADE, related_name="components")
    component_type = models.CharField(max_length=20, choices=ComponentType.choices)
    order = models.PositiveSmallIntegerField()
    body_html_he = models.TextField(blank=True)
    instructions_he = models.TextField(blank=True)

    class Meta:
        verbose_name = _("רכיב מודול")
        verbose_name_plural = _("רכיבי מודול")
        ordering = ["order"]
        unique_together = [("module", "order")]

    def __str__(self) -> str:
        return f"{self.module} / {self.get_component_type_display()}"


class Tag(models.Model):
    name_he = models.CharField(max_length=100)
    name_en = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        verbose_name = _("תג")
        verbose_name_plural = _("תגים")

    def __str__(self) -> str:
        return self.name_he


class QuestionType(models.IntegerChoices):
    RETRIEVAL = 1, _("אחזור מידע")
    SINGLE_CALC = 2, _("חישוב חד-שלבי")
    MULTI_CALC = 3, _("חישוב רב-שלבי")
    DOCUMENT_ANALYSIS = 4, _("ניתוח מסמך")
    SCENARIO = 5, _("תרחיש")
    SYNTHESIS = 6, _("סינתזה")


class QuestionDifficulty(models.TextChoices):
    BASIC = "basic", _("בסיסי")
    INTERMEDIATE = "intermediate", _("בינוני")
    ADVANCED = "advanced", _("מתקדם")


class QuestionUsage(models.TextChoices):
    COMPREHENSION = "comprehension", _("בדיקת הבנה")
    PRACTICE = "practice", _("תרגול")
    EXAM = "exam", _("מבחן")


class Question(TimeStampedModel):
    module = models.ForeignKey(
        Module, on_delete=models.SET_NULL, null=True, blank=True, related_name="questions"
    )
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, related_name="questions"
    )
    question_id_external = models.CharField(max_length=50, unique=True, blank=True)
    question_type = models.IntegerField(choices=QuestionType.choices)
    difficulty = models.CharField(max_length=20, choices=QuestionDifficulty.choices)
    stem_html_he = models.TextField()
    image_url = models.URLField(blank=True)
    points = models.PositiveSmallIntegerField(default=1)
    avg_time_seconds = models.PositiveSmallIntegerField(default=60)
    usage_context = models.CharField(max_length=20, choices=QuestionUsage.choices)
    topic_tags = models.ManyToManyField(Tag, blank=True)
    senior_insight_he = models.TextField(blank=True)
    created_by = models.ForeignKey(
        "accounts.User", on_delete=models.SET_NULL, null=True, blank=True, related_name="questions_created"
    )
    reviewed_by = models.ForeignKey(
        "accounts.User", on_delete=models.SET_NULL, null=True, blank=True, related_name="questions_reviewed"
    )
    last_calibrated_at = models.DateTimeField(null=True, blank=True)
    version = models.PositiveIntegerField(default=1)

    class Meta:
        verbose_name = _("שאלה")
        verbose_name_plural = _("שאלות")

    def __str__(self) -> str:
        return f"{self.question_id_external or self.pk} — {self.stem_html_he[:60]}"

    def save(self, *args, **kwargs):
        if self.pk:
            self.version += 1
        super().save(*args, **kwargs)


class QuestionOption(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="options")
    text_he = models.TextField()
    is_correct = models.BooleanField(default=False)
    display_order = models.PositiveSmallIntegerField()
    distractor_rationale_he = models.TextField(blank=True)

    class Meta:
        verbose_name = _("תשובה אפשרית")
        verbose_name_plural = _("תשובות אפשריות")
        ordering = ["display_order"]
        unique_together = [("question", "display_order")]

    def __str__(self) -> str:
        marker = "✓" if self.is_correct else "✗"
        return f"{marker} {self.text_he[:80]}"


class QuestionExplanation(models.Model):
    question = models.OneToOneField(Question, on_delete=models.CASCADE, related_name="explanation")
    explanation_html_he = models.TextField()

    class Meta:
        verbose_name = _("הסבר לשאלה")
        verbose_name_plural = _("הסברים לשאלות")

    def __str__(self) -> str:
        return f"הסבר — {self.question}"
