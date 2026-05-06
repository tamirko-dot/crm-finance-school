import os
from .base import *  # noqa: F401, F403

DEBUG = False

# Railway provides the PORT env var — also allow the Railway domain automatically
ALLOWED_HOSTS = env.list("DJANGO_ALLOWED_HOSTS", default=[]) + [
    ".railway.app",
    ".up.railway.app",
]

SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
X_FRAME_OPTIONS = "DENY"

# Trust Railway's proxy headers
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
USE_X_FORWARDED_HOST = True
