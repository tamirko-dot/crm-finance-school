from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect

from core.decorators.roles import trainee_required, manager_required, admin_required, ceo_required


def home(request: HttpRequest) -> HttpResponse:
    if request.user.is_authenticated:
        return redirect("dashboard")
    return redirect("login")


@login_required
def dashboard(request: HttpRequest) -> HttpResponse:
    role = getattr(request.user, "role", None)
    ctx = {}

    if role == "trainee":
        from content.models import Course
        from enrollment.models import CourseEnrollment
        courses = Course.objects.filter(domain__is_active=True, is_active=True).order_by("course_number")
        enrollment_map = {e.course_id: e for e in CourseEnrollment.objects.filter(user=request.user)}
        ctx["course_data"] = [
            {"course": c, "enrollment": enrollment_map.get(c.pk), "status": enrollment_map.get(c.pk, None)}
            for c in courses
        ]
        return render(request, "core/dashboard_trainee.html", ctx)

    if role == "customer_manager":
        from enrollment.models import UnlockRequest, UnlockRequestStatus
        from capstone.models import CapstoneSubmission, CapstoneStatus
        from accounts.models import User, UserRole
        ctx["pending_requests"] = UnlockRequest.objects.filter(status=UnlockRequestStatus.PENDING).count()
        ctx["pending_capstones"] = CapstoneSubmission.objects.filter(status=CapstoneStatus.SUBMITTED).count()
        ctx["trainee_count"] = User.objects.filter(role=UserRole.TRAINEE, is_active=True).count()
        return render(request, "core/dashboard_manager.html", ctx)

    if role == "admin":
        from accounts.models import User
        from content.models import Question, Domain
        ctx["user_count"] = User.objects.filter(is_active=True).count()
        ctx["question_count"] = Question.objects.filter(is_active=True).count()
        ctx["domain_count"] = Domain.objects.filter(is_active=True).count()
        return render(request, "core/dashboard_admin.html", ctx)

    if role == "ceo":
        return render(request, "core/dashboard_ceo.html", ctx)

    return render(request, "core/dashboard_trainee.html", ctx)


def lockout_response(request: HttpRequest, credentials: dict, *args, **kwargs) -> HttpResponse:
    return render(request, "accounts/lockout.html", status=403)


def permission_denied_view(request: HttpRequest, exception=None) -> HttpResponse:
    return render(request, "core/403.html", status=403)
