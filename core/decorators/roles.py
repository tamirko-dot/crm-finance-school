from functools import wraps

from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied


def _role_required(*roles):
    def decorator(view_func):
        @wraps(view_func)
        @login_required
        def _wrapped(request, *args, **kwargs):
            if not hasattr(request.user, "role") or request.user.role not in roles:
                raise PermissionDenied
            return view_func(request, *args, **kwargs)
        return _wrapped
    return decorator


trainee_required = _role_required("trainee")
manager_required = _role_required("customer_manager")
admin_required = _role_required("admin")
ceo_required = _role_required("ceo")
manager_or_ceo_required = _role_required("customer_manager", "ceo")
admin_or_ceo_required = _role_required("admin", "ceo")
staff_required = _role_required("customer_manager", "admin", "ceo")
