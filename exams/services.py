"""Exam business logic: question selection, attempt creation, grading."""
from __future__ import annotations

import random
from typing import TYPE_CHECKING

from django.utils import timezone

from content.models import Question, QuestionType, QuestionUsage
from exams.models import ExamAttempt, ExamAttemptQuestion

if TYPE_CHECKING:
    from accounts.models import User
    from content.models import Course


_TYPE_WEIGHTS = {
    "retrieval": 0.30,
    "calc": 0.30,
    "document": 0.25,
    "scenario": 0.15,
}

_TYPE_MAP = {
    "retrieval": [QuestionType.RETRIEVAL],
    "calc": [QuestionType.SINGLE_CALC, QuestionType.MULTI_CALC],
    "document": [QuestionType.DOCUMENT_ANALYSIS],
    "scenario": [QuestionType.SCENARIO, QuestionType.SYNTHESIS],
}


def select_exam_questions(course: "Course", n: int) -> list[Question]:
    pool = list(
        Question.objects.filter(course=course, usage_context=QuestionUsage.EXAM, is_active=True)
        .prefetch_related("options", "explanation")
    )
    if not pool:
        # For dev/seed: fall back to all active questions for this course
        pool = list(
            Question.objects.filter(course=course, is_active=True)
            .prefetch_related("options", "explanation")
        )
    if len(pool) <= n:
        random.shuffle(pool)
        return pool

    groups = {name: [q for q in pool if q.question_type in types] for name, types in _TYPE_MAP.items()}
    selected: list[Question] = []

    for name, weight in _TYPE_WEIGHTS.items():
        target = max(1, round(n * weight))
        group = groups[name]
        take = min(target, len(group))
        if take:
            selected.extend(random.sample(group, take))

    selected_pks = {q.pk for q in selected}
    shortfall = n - len(selected)
    if shortfall > 0:
        remaining = [q for q in pool if q.pk not in selected_pks]
        selected.extend(random.sample(remaining, min(shortfall, len(remaining))))

    random.shuffle(selected)
    return selected[:n]


def create_exam_attempt(user: "User", course: "Course") -> ExamAttempt:
    last = ExamAttempt.objects.filter(user=user, course=course).order_by("-attempt_number").first()
    attempt_number = (last.attempt_number + 1) if last else 1

    attempt = ExamAttempt.objects.create(user=user, course=course, attempt_number=attempt_number)

    questions = select_exam_questions(course, course.exam_question_count)
    snapshots = [
        ExamAttemptQuestion.snapshot_from_question(attempt, q, idx + 1)
        for idx, q in enumerate(questions)
    ]
    ExamAttemptQuestion.objects.bulk_create(snapshots)

    from documents.models import AuditLog
    AuditLog.objects.create(
        user=user,
        action="exam_started",
        entity_type="ExamAttempt",
        entity_id=str(attempt.pk),
        metadata_json={"course_slug": course.slug, "attempt_number": attempt_number, "question_count": len(snapshots)},
    )
    return attempt


def grade_exam_attempt(attempt: ExamAttempt) -> float:
    questions = attempt.attempt_questions.all()
    if not questions:
        score_pct = 0.0
    else:
        correct = 0
        total_points = 0
        for aq in questions:
            aq.is_correct = (aq.user_answer_option_index == aq.correct_option_index_snapshot)
            aq.save(update_fields=["is_correct"])
            total_points += 1
            if aq.is_correct:
                correct += 1
        score_pct = round((correct / total_points) * 100, 1) if total_points else 0.0

    attempt.submit()
    attempt.save()
    attempt.grade(score_pct=score_pct)
    attempt.save()
    return score_pct


def seconds_remaining(attempt: ExamAttempt) -> int:
    from datetime import timedelta
    deadline = attempt.started_at + timedelta(minutes=attempt.course.exam_duration_minutes)
    remaining = (deadline - timezone.now()).total_seconds()
    return max(0, int(remaining))
