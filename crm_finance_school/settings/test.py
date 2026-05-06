from .base import *  # noqa: F401, F403

DEBUG = True
ALLOWED_HOSTS = ["localhost", "127.0.0.1"]

# Fast in-memory SQLite for tests — never hits Supabase
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
    }
}

# Skip axes rate limiting in tests
AXES_ENABLED = False

# Skip Supabase auth in tests (placeholder triggers fallback)
SUPABASE_URL = "https://placeholder.supabase.co"
SUPABASE_ANON_KEY = "placeholder"
SUPABASE_SERVICE_KEY = "placeholder"
SUPABASE_STORAGE_BUCKET = "test-bucket"
