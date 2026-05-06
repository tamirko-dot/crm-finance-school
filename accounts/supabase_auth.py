"""
Supabase Auth integration.

Flow:
  1. POST email+password → try Supabase sign_in_with_password
  2. On success → create/update local User, copy supabase_user_id, return User
  3. If SUPABASE_URL is a placeholder or any error → return None (caller falls back to Django ModelBackend)
"""
from __future__ import annotations

import logging

from django.conf import settings

logger = logging.getLogger(__name__)

_PLACEHOLDER = "placeholder"


def _supabase_available() -> bool:
    url = getattr(settings, "SUPABASE_URL", "")
    return bool(url) and _PLACEHOLDER not in url


def authenticate_with_supabase(email: str, password: str):
    """
    Returns a local User instance on success, None on failure.
    Never raises — all exceptions are caught and logged.
    """
    if not _supabase_available():
        logger.debug("Supabase not configured; skipping Supabase auth.")
        return None

    try:
        from supabase import create_client
        client = create_client(settings.SUPABASE_URL, settings.SUPABASE_ANON_KEY)
        response = client.auth.sign_in_with_password({"email": email, "password": password})
        sb_user = response.user
        if sb_user is None:
            return None
        return _sync_local_user(sb_user)
    except Exception as exc:
        logger.warning("Supabase auth failed for %s: %s", email, exc)
        return None


def _sync_local_user(sb_user):
    """Create or update the local Django user to match the Supabase user record."""
    from accounts.models import User, UserRole

    email = sb_user.email
    sb_id = sb_user.id
    meta = sb_user.user_metadata or {}

    user, created = User.objects.get_or_create(
        email=email,
        defaults={
            "username": email.split("@")[0],
            "supabase_user_id": sb_id,
            "full_name_he": meta.get("full_name_he", ""),
            "full_name_en": meta.get("full_name_en", ""),
            "role": meta.get("role", UserRole.TRAINEE),
        },
    )

    if not created:
        changed = False
        if user.supabase_user_id != sb_id:
            user.supabase_user_id = sb_id
            changed = True
        if changed:
            user.save(update_fields=["supabase_user_id"])

    user.backend = "django.contrib.auth.backends.ModelBackend"
    return user
