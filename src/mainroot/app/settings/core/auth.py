AUTH_PASSWORD_VALIDATORS = (
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",},
)
AUTH_USER_MODEL = 'account.User'
AUTHENTICATION_BACKENDS = ('django.contrib.auth.backends.ModelBackend',)
LOGIN_REDIRECT_URL = "/"
LOGIN_URL = "/"
LOGOUT_REDIRECT_URL = None
PASSWORD_HASHERS = (
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.Argon2PasswordHasher',
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
)
PASSWORD_RESET_TIMEOUT = 259200,
