from django.utils.translation import gettext_lazy as _

from app.settings.paths import BASE_DIR


gettext = lambda s: s

DATE_FORMAT = "j E Y"
DATE_INPUT_FORMATS = (
    "%Y-%m-%d",  # '2006-10-25'
    "%m/%d/%Y",  # '10/25/2006'
    "%m/%d/%y",  # '10/25/06'
    "%b %d %Y",  # 'Oct 25 2006'
    "%b %d, %Y",  # 'Oct 25, 2006'
    "%d %b %Y",  # '25 Oct 2006'
    "%d %b, %Y",  # '25 Oct, 2006'
    "%B %d %Y",  # 'October 25 2006'
    "%B %d, %Y",  # 'October 25, 2006'
    "%d %B %Y",  # '25 October 2006'
    "%d %B, %Y",  # '25 October, 2006'
)
DATETIME_FORMAT = "j E Y, H:M"
DATETIME_INPUT_FORMATS = (
    "%Y-%m-%d %H:%M:%S",  # '2006-10-25 14:30:59'
    "%Y-%m-%d %H:%M:%S.%f",  # '2006-10-25 14:30:59.000200'
    "%Y-%m-%d %H:%M",  # '2006-10-25 14:30'
    "%m/%d/%Y %H:%M:%S",  # '10/25/2006 14:30:59'
    "%m/%d/%Y %H:%M:%S.%f",  # '10/25/2006 14:30:59.000200'
    "%m/%d/%Y %H:%M",  # '10/25/2006 14:30'
    "%m/%d/%y %H:%M:%S",  # '10/25/06 14:30:59'
    "%m/%d/%y %H:%M:%S.%f",  # '10/25/06 14:30:59.000200'
    "%m/%d/%y %H:%M",  # '10/25/06 14:30'
)
DECIMAL_SEPARATOR = ","
FIRST_DAY_OF_WEEK = 1
FORMAT_MODULE_PATH = None
LANGUAGE_CODE = "ru-RU"
LANGUAGE_COOKIE_AGE = None
LANGUAGE_COOKIE_DOMAIN = None
LANGUAGE_COOKIE_HTTPONLY = False
LANGUAGE_COOKIE_NAME = "language_settings"
LANGUAGE_COOKIE_PATH = "/"
LANGUAGE_COOKIE_SAMESITE = None
LANGUAGE_COOKIE_SECURE = False
LANGUAGES = (
    ("en", gettext("English")),
    ("ru", gettext("Russian")),
    ("pl", gettext("Poland")),
    ("de", gettext("Germany")),
    ("sr", gettext("Srpski")),
)
# LANGUAGES_BIDI
LOCALE_PATHS = (BASE_DIR / "locale",)
MONTH_DAY_FORMAT = "j E"
NUMBER_GROUPING = 3
SHORT_DATE_FORMAT = "d.m.Y"
SHORT_DATETIME_FORMAT = "d.m.Y H:M"
THOUSAND_SEPARATOR = " "
TIME_FORMAT = "H:M:S"
TIME_INPUT_FORMATS = (
    "%H:%M:%S",  # '14:30:59'
    "%H:%M:%S.%f",  # '14:30:59.000200'
    "%H:%M",  # '14:30'
)
TIME_ZONE = "UTC"
# TIME_ZONE = "Europe/Moscow"
# TIME_ZONE = "Asia/Yekaterinburg"
# TIME_ZONE = "Asia/Irkutsk"
USE_TZ = True
USE_I18N = True
USE_L10N = True
USE_THOUSAND_SEPARATOR = True
USE_TZ = True
YEAR_MONTH_FORMAT = "E Y"
