from urllib import parse

# from app.env import appsecrets

SESSION_CACHE_ALIAS = "default"
SESSION_COOKIE_AGE = 1209600
# SESSION_COOKIE_DOMAIN = ("127.0.0.1")
SESSION_COOKIE_HTTPONLY = True
SESSION_COOKIE_NAME = "sessionid"
SESSION_COOKIE_PATH = "/"
SESSION_COOKIE_SAMESITE = "Lax"
SESSION_COOKIE_SECURE = True
SESSION_ENGINE = "django.contrib.sessions.backends.db"
# 'django.contrib.sessions.backends.file'
# 'django.contrib.sessions.backends.cache'
# 'django.contrib.sessions.backends.cached_db'
# 'django.contrib.sessions.backends.signed_cookies'
SESSION_EXPIRE_AT_BROWSER_CLOSE = False
SESSION_FILE_PATH = None
SESSION_SAVE_EVERY_REQUEST = False
SESSION_SERIALIZER = "django.contrib.sessions.serializers.JSONSerializer"
