ABSOLUTE_URL_OVERRIDES = {}
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
FIXTURE_DIRS = ()
INSTALLED_APPS = (
    # Core
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # Packages
    "ninja",
    "whitenoise",
    "psycopg2",

    # Apps
    "account",
    "commons",
    "frontend",
)
