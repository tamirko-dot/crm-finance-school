import logging

from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.views.decorators.http import require_http_methods

from documents.models import AuditLog
from .supabase_auth import authenticate_with_supabase

logger = logging.getLogger(__name__)


@require_http_methods(["GET", "POST"])
def login_view(request: HttpRequest) -> HttpResponse:
    if request.user.is_authenticated:
        return redirect("dashboard")

    if request.method == "POST":
        email = request.POST.get("email", "").strip().lower()
        password = request.POST.get("password", "")

        if not email or not password:
            messages.error(request, "יש להזין דוא\"ל וסיסמה.")
            return render(request, "accounts/login.html")

        user = None

        # 1. Try Supabase Auth first
        user = authenticate_with_supabase(email, password)

        # 2. Fallback to Django ModelBackend (dev superusers, local test users)
        if user is None:
            user = authenticate(request, username=email, password=password)

        if user is not None and user.is_active:
            login(request, user)
            _audit_login(user)
            logger.info("Login: %s (role=%s)", user.email, getattr(user, "role", "?"))
            next_url = request.GET.get("next") or "dashboard"
            return redirect(next_url)

        messages.error(request, "כתובת דוא\"ל או סיסמה שגויים.")
        logger.warning("Failed login attempt for email: %s", email)

    return render(request, "accounts/login.html")


def logout_view(request: HttpRequest) -> HttpResponse:
    if request.user.is_authenticated:
        logger.info("Logout: %s", request.user.email)
    logout(request)
    return redirect("login")


def _audit_login(user) -> None:
    try:
        AuditLog.objects.create(
            user=user,
            action="login",
            entity_type="User",
            entity_id=str(user.pk),
            metadata_json={"role": user.role},
        )
    except Exception:
        pass
