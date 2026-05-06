"""
Import questions from a JSON or CSV file.

JSON format (preferred — supports full fidelity):
  See data/examples/questions_sample.json for a complete example.

CSV format (simplified — up to 6 options per question):
  Columns: question_id_external, course_number, module_number,
           question_type, difficulty, usage_context, stem_html_he,
           points, avg_time_seconds, senior_insight_he,
           opt1_text, opt1_correct, opt1_rationale,
           opt2_text, opt2_correct, opt2_rationale, ... (up to opt6_*),
           explanation_html_he

Flags:
  --dry-run   Preview what would be created/updated without saving.
  --update    Update existing questions (by question_id_external).
              Without this flag, existing questions are skipped.
"""
import csv
import json
from pathlib import Path

from django.core.management.base import BaseCommand, CommandError
from django.db import transaction

from content.models import (
    Course, Module, Question, QuestionOption, QuestionExplanation,
    QuestionType, QuestionDifficulty, QuestionUsage, Tag,
)


class Command(BaseCommand):
    help = "Import questions from JSON or CSV — see command docstring for format details"

    def add_arguments(self, parser):
        parser.add_argument("path", type=str, help="Path to JSON or CSV file")
        parser.add_argument("--dry-run", action="store_true", help="Preview without saving")
        parser.add_argument("--update", action="store_true", help="Update existing questions")

    def handle(self, *args, **options):
        path = Path(options["path"])
        if not path.exists():
            raise CommandError(f"File not found: {path}")

        dry_run = options["dry_run"]
        allow_update = options["update"]

        if path.suffix.lower() == ".json":
            rows = self._load_json(path)
        elif path.suffix.lower() == ".csv":
            rows = self._load_csv(path)
        else:
            raise CommandError("File must be .json or .csv")

        self.stdout.write(f"Loaded {len(rows)} questions from {path.name}")
        if dry_run:
            self.stdout.write(self.style.WARNING("DRY RUN — nothing will be saved"))

        created = updated = skipped = errors = 0

        for i, row in enumerate(rows, 1):
            try:
                result = self._process_row(row, dry_run=dry_run, allow_update=allow_update)
                if result == "created":
                    created += 1
                elif result == "updated":
                    updated += 1
                elif result == "skipped":
                    skipped += 1
            except Exception as exc:
                errors += 1
                ext_id = row.get("question_id_external", f"row {i}")
                self.stderr.write(f"  [ERROR] {ext_id}: {exc}")

        self.stdout.write("")
        self.stdout.write(f"  Created:  {created}")
        self.stdout.write(f"  Updated:  {updated}")
        self.stdout.write(f"  Skipped:  {skipped}")
        self.stdout.write(f"  Errors:   {errors}")
        if errors:
            self.stdout.write(self.style.WARNING(f"Completed with {errors} error(s)."))
        else:
            self.stdout.write(self.style.SUCCESS("Import complete."))

    # ─── loaders ──────────────────────────────────────────────────────────────

    def _load_json(self, path: Path) -> list[dict]:
        with path.open(encoding="utf-8") as f:
            data = json.load(f)
        if not isinstance(data, list):
            raise CommandError("JSON root must be an array of question objects.")
        return data

    def _load_csv(self, path: Path) -> list[dict]:
        rows = []
        with path.open(encoding="utf-8-sig", newline="") as f:
            reader = csv.DictReader(f)
            for row in reader:
                options = []
                for n in range(1, 7):
                    text = row.get(f"opt{n}_text", "").strip()
                    if not text:
                        break
                    options.append({
                        "text_he": text,
                        "is_correct": row.get(f"opt{n}_correct", "").strip().lower() in ("1", "true", "yes", "כן"),
                        "distractor_rationale_he": row.get(f"opt{n}_rationale", "").strip(),
                    })
                rows.append({
                    "question_id_external": row.get("question_id_external", "").strip(),
                    "course_number": int(row.get("course_number", 0)),
                    "module_number": int(row.get("module_number", 0)) if row.get("module_number") else None,
                    "question_type": int(row.get("question_type", 1)),
                    "difficulty": row.get("difficulty", "basic").strip(),
                    "usage_context": row.get("usage_context", "exam").strip(),
                    "stem_html_he": row.get("stem_html_he", "").strip(),
                    "image_url": row.get("image_url", "").strip(),
                    "points": int(row.get("points", 1)),
                    "avg_time_seconds": int(row.get("avg_time_seconds", 60)),
                    "senior_insight_he": row.get("senior_insight_he", "").strip(),
                    "topic_tags": [t.strip() for t in row.get("topic_tags", "").split(",") if t.strip()],
                    "options": options,
                    "explanation_html_he": row.get("explanation_html_he", "").strip(),
                })
        return rows

    # ─── processor ────────────────────────────────────────────────────────────

    @transaction.atomic
    def _process_row(self, row: dict, dry_run: bool, allow_update: bool) -> str:
        ext_id = row.get("question_id_external", "").strip()
        if not ext_id:
            raise ValueError("question_id_external is required")

        course_number = row.get("course_number")
        if not course_number:
            raise ValueError("course_number is required")

        try:
            course = Course.objects.get(course_number=course_number)
        except Course.DoesNotExist:
            raise ValueError(f"Course {course_number} not found")

        module = None
        module_number = row.get("module_number")
        if module_number:
            try:
                module = Module.objects.get(course=course, module_number=module_number)
            except Module.DoesNotExist:
                raise ValueError(f"Module {module_number} not found in Course {course_number}")

        options = row.get("options", [])
        if not options:
            raise ValueError("At least one option is required")
        if not any(o.get("is_correct") for o in options):
            raise ValueError("At least one option must be marked as correct")

        existing = Question.objects.filter(question_id_external=ext_id).first()

        if existing and not allow_update:
            self.stdout.write(f"  [skip] {ext_id}")
            return "skipped"

        defaults = {
            "course": course,
            "module": module,
            "question_type": row.get("question_type", QuestionType.RETRIEVAL),
            "difficulty": row.get("difficulty", QuestionDifficulty.BASIC),
            "usage_context": row.get("usage_context", QuestionUsage.EXAM),
            "stem_html_he": row.get("stem_html_he", ""),
            "image_url": row.get("image_url", ""),
            "points": row.get("points", 1),
            "avg_time_seconds": row.get("avg_time_seconds", 60),
            "senior_insight_he": row.get("senior_insight_he", ""),
        }

        action = "updated" if existing else "created"
        self.stdout.write(f"  [{action}] {ext_id}")

        if dry_run:
            return action

        if existing:
            for field, value in defaults.items():
                setattr(existing, field, value)
            existing.save()
            question = existing
            question.options.all().delete()
            if hasattr(question, "explanation"):
                question.explanation.delete()
        else:
            question = Question.objects.create(question_id_external=ext_id, **defaults)

        for idx, opt in enumerate(options):
            QuestionOption.objects.create(
                question=question,
                text_he=opt.get("text_he", ""),
                is_correct=bool(opt.get("is_correct", False)),
                display_order=idx,
                distractor_rationale_he=opt.get("distractor_rationale_he", ""),
            )

        explanation_html = row.get("explanation_html_he", "").strip()
        if explanation_html:
            QuestionExplanation.objects.create(question=question, explanation_html_he=explanation_html)

        for tag_slug in row.get("topic_tags", []):
            tag = Tag.objects.filter(slug=tag_slug).first()
            if tag:
                question.topic_tags.add(tag)

        return action
