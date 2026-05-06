"""Phase 6 tests: import_questions and import_documents management commands."""
import json
import tempfile
from pathlib import Path

import pytest
from django.core.management import call_command
from django.core.management.base import CommandError
from io import StringIO

from accounts.models import User, UserRole
from content.models import Course, Domain, Module, Question, QuestionOption, QuestionExplanation
from documents.models import LearningDocument, DocumentTag


# ─── fixtures ─────────────────────────────────────────────────────────────────

@pytest.fixture
def domain(db):
    return Domain.objects.create(name_he="Test", name_en="Test", slug="test-domain-p6")


@pytest.fixture
def course(db, domain):
    return Course.objects.create(
        domain=domain, title_he="קורס", slug="c97-test-p6",
        phase="A", course_number=97, passing_score_pct=75,
    )


@pytest.fixture
def module(db, course):
    return Module.objects.create(
        course=course, title_he="מודול", slug="test-mod-p6", module_number=1,
    )


@pytest.fixture
def valid_question_json(course, module):
    return [
        {
            "question_id_external": "P6-Q01",
            "course_number": course.course_number,
            "module_number": module.module_number,
            "question_type": 1,
            "difficulty": "basic",
            "usage_context": "exam",
            "stem_html_he": "<p>שאלת בדיקה</p>",
            "image_url": "",
            "points": 1,
            "avg_time_seconds": 60,
            "senior_insight_he": "תובנה",
            "topic_tags": [],
            "options": [
                {"text_he": "תשובה נכונה", "is_correct": True, "distractor_rationale_he": ""},
                {"text_he": "תשובה שגויה", "is_correct": False, "distractor_rationale_he": "הסבר"},
            ],
            "explanation_html_he": "<p>הסבר מפורט</p>",
        }
    ]


# ─── import_questions ─────────────────────────────────────────────────────────

@pytest.mark.django_db
class TestImportQuestionsJSON:
    def test_creates_question_from_json(self, course, module, valid_question_json):
        with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False, encoding="utf-8") as f:
            json.dump(valid_question_json, f, ensure_ascii=False)
            tmp = f.name
        out = StringIO()
        call_command("import_questions", tmp, stdout=out)
        assert Question.objects.filter(question_id_external="P6-Q01").exists()

    def test_creates_options(self, course, module, valid_question_json):
        with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False, encoding="utf-8") as f:
            json.dump(valid_question_json, f, ensure_ascii=False)
            tmp = f.name
        call_command("import_questions", tmp, stdout=StringIO())
        q = Question.objects.get(question_id_external="P6-Q01")
        assert q.options.count() == 2
        assert q.options.filter(is_correct=True).count() == 1

    def test_creates_explanation(self, course, module, valid_question_json):
        with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False, encoding="utf-8") as f:
            json.dump(valid_question_json, f, ensure_ascii=False)
            tmp = f.name
        call_command("import_questions", tmp, stdout=StringIO())
        q = Question.objects.get(question_id_external="P6-Q01")
        assert hasattr(q, "explanation")
        assert "<p>הסבר מפורט</p>" in q.explanation.explanation_html_he

    def test_dry_run_does_not_save(self, course, module, valid_question_json):
        with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False, encoding="utf-8") as f:
            json.dump(valid_question_json, f, ensure_ascii=False)
            tmp = f.name
        call_command("import_questions", tmp, dry_run=True, stdout=StringIO())
        assert not Question.objects.filter(question_id_external="P6-Q01").exists()

    def test_skip_existing_without_update_flag(self, course, module, valid_question_json):
        with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False, encoding="utf-8") as f:
            json.dump(valid_question_json, f, ensure_ascii=False)
            tmp = f.name
        call_command("import_questions", tmp, stdout=StringIO())
        # Run again — should skip
        out = StringIO()
        call_command("import_questions", tmp, stdout=out)
        assert "skip" in out.getvalue()
        assert Question.objects.filter(question_id_external="P6-Q01").count() == 1

    def test_update_flag_replaces_options(self, course, module, valid_question_json):
        with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False, encoding="utf-8") as f:
            json.dump(valid_question_json, f, ensure_ascii=False)
            tmp = f.name
        call_command("import_questions", tmp, stdout=StringIO())
        # Modify and re-import with --update
        valid_question_json[0]["options"].append(
            {"text_he": "תשובה שלישית", "is_correct": False, "distractor_rationale_he": ""}
        )
        with open(tmp, "w", encoding="utf-8") as f:
            json.dump(valid_question_json, f, ensure_ascii=False)
        call_command("import_questions", tmp, update=True, stdout=StringIO())
        q = Question.objects.get(question_id_external="P6-Q01")
        assert q.options.count() == 3

    def test_error_on_missing_course(self, domain):
        data = [{"question_id_external": "BAD-Q01", "course_number": 999,
                  "question_type": 1, "difficulty": "basic", "usage_context": "exam",
                  "stem_html_he": "<p>x</p>", "points": 1,
                  "options": [{"text_he": "a", "is_correct": True, "distractor_rationale_he": ""}]}]
        with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False, encoding="utf-8") as f:
            json.dump(data, f)
            tmp = f.name
        out = StringIO()
        call_command("import_questions", tmp, stdout=out, stderr=StringIO())
        assert not Question.objects.filter(question_id_external="BAD-Q01").exists()

    def test_error_on_no_correct_option(self, course, module):
        data = [{"question_id_external": "BAD-Q02", "course_number": course.course_number,
                  "question_type": 1, "difficulty": "basic", "usage_context": "exam",
                  "stem_html_he": "<p>x</p>", "points": 1,
                  "options": [{"text_he": "a", "is_correct": False, "distractor_rationale_he": ""}]}]
        with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False, encoding="utf-8") as f:
            json.dump(data, f)
            tmp = f.name
        call_command("import_questions", tmp, stdout=StringIO(), stderr=StringIO())
        assert not Question.objects.filter(question_id_external="BAD-Q02").exists()

    def test_raises_on_missing_file(self):
        with pytest.raises(CommandError, match="not found"):
            call_command("import_questions", "/nonexistent/file.json", stdout=StringIO())


@pytest.mark.django_db
class TestImportQuestionsCSV:
    def test_creates_question_from_csv(self, course, module):
        csv_content = (
            "question_id_external,course_number,module_number,question_type,difficulty,"
            "usage_context,stem_html_he,points,avg_time_seconds,senior_insight_he,"
            "opt1_text,opt1_correct,opt1_rationale,opt2_text,opt2_correct,opt2_rationale,"
            "explanation_html_he\n"
            f"P6-CSV-Q01,{course.course_number},{module.module_number},1,basic,exam,"
            "<p>שאלת CSV</p>,1,60,תובנה,"
            "תשובה נכונה,true,,תשובה שגויה,false,הסבר,"
            "<p>הסבר</p>\n"
        )
        with tempfile.NamedTemporaryFile(mode="w", suffix=".csv", delete=False, encoding="utf-8") as f:
            f.write(csv_content)
            tmp = f.name
        call_command("import_questions", tmp, stdout=StringIO())
        assert Question.objects.filter(question_id_external="P6-CSV-Q01").exists()
        q = Question.objects.get(question_id_external="P6-CSV-Q01")
        assert q.options.count() == 2


# ─── import_documents ─────────────────────────────────────────────────────────

@pytest.mark.django_db
class TestImportDocuments:
    def test_creates_document_from_json(self, domain):
        data = [{
            "title_he": "מסמך בדיקה",
            "description_he": "תיאור",
            "file_url": "https://example.com/doc.pdf",
            "file_type": "pdf",
            "domain_slug": domain.slug,
            "tags": [],
        }]
        with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False, encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False)
            tmp = f.name
        call_command("import_documents", tmp, stdout=StringIO())
        assert LearningDocument.objects.filter(title_he="מסמך בדיקה").exists()

    def test_dry_run_does_not_save(self, domain):
        data = [{"title_he": "לא נשמר", "description_he": "", "file_url": "https://x.com/x.pdf",
                  "file_type": "pdf", "domain_slug": domain.slug, "tags": []}]
        with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False, encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False)
            tmp = f.name
        call_command("import_documents", tmp, dry_run=True, stdout=StringIO())
        assert not LearningDocument.objects.filter(title_he="לא נשמר").exists()

    def test_error_on_invalid_domain(self):
        data = [{"title_he": "X", "description_he": "", "file_url": "https://x.com/x.pdf",
                  "file_type": "pdf", "domain_slug": "no-such-domain", "tags": []}]
        with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False, encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False)
            tmp = f.name
        call_command("import_documents", tmp, stdout=StringIO(), stderr=StringIO())
        assert not LearningDocument.objects.filter(title_he="X").exists()
