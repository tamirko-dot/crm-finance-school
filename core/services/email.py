from __future__ import annotations

import logging

from django.utils import timezone

logger = logging.getLogger(__name__)

_STUB_PREFIX = "[EMAIL_STUB]"


def _stub(method: str, user, **kwargs) -> None:
    from documents.models import Notification  # avoid circular import

    log_msg = f"{_STUB_PREFIX} would send '{method}' to {getattr(user, 'email', user)}"
    for k, v in kwargs.items():
        log_msg += f" | {k}={v}"
    logger.info(log_msg)

    Notification.objects.create(
        user=user,
        type=method,
        payload_json=kwargs,
    )


class EmailService:
    @staticmethod
    def send_welcome(user) -> None:
        _stub("welcome", user)

    @staticmethod
    def send_unlock_approved(user, course) -> None:
        _stub("unlock_approved", user, course_slug=course.slug)

    @staticmethod
    def send_unlock_denied(user, course, reason: str = "") -> None:
        _stub("unlock_denied", user, course_slug=course.slug, reason=reason)

    @staticmethod
    def send_exam_passed(user, course, score: float) -> None:
        _stub("exam_passed", user, course_slug=course.slug, score=score)

    @staticmethod
    def send_exam_failed(user, course, score: float, attempts_remaining: int) -> None:
        _stub("exam_failed", user, course_slug=course.slug, score=score, attempts_remaining=attempts_remaining)

    @staticmethod
    def send_capstone_received(user) -> None:
        _stub("capstone_received", user)

    @staticmethod
    def send_capstone_graded(user, passed: bool) -> None:
        _stub("capstone_graded", user, passed=passed)

    @staticmethod
    def send_manager_unlock_request(manager, unlock_request) -> None:
        _stub("manager_unlock_request", manager, request_id=unlock_request.pk)
