from urllib import parse

ALLOWED_HOSTS = (
    "127.0.0.1",
    "localhost",
    "0.0.0.0",
    # parse.urlsplit(appsecrets.cors_origin).hostname
)
CSRF_COOKIE_DOMAIN = ("127.0.0.1", "localhost")
    # host := parse.urlsplit(appsecrets.cors_origin).hostname
# ) and (
    # host
    # if host.replace(".", "").isdigit()
    # else ".{}.{}".format(*host.split(".")[-2:])
# )
CSRF_COOKIE_NAME = "csrftoken"
CSRF_COOKIE_PATH = "/"
CSRF_COOKIE_SAMESITE = "Lax"
CSRF_COOKIE_SECURE = True
CSRF_FAILURE_VIEW = "django.views.csrf.csrf_failure"
CSRF_HEADER_NAME = "HTTP_X_CSRFTOKEN"
CSRF_TRUSTED_ORIGINS = (
      tuple(f"http://{host}"  for host in ALLOWED_HOSTS)
    + tuple(f"https://{host}" for host in ALLOWED_HOSTS)
)
CSRF_USE_SESSIONS = False
SECRET_KEY = "django-insecure-0_w*fot_@fexxy71y_14iwx%w!mw)vbsm&b0j(@shf5@8+ivg3"
SECRET_KEY_FALLBACKS = []
X_FRAME_OPTIONS = "DENY"
CSRF_COOKIE_HTTPONLY = False
