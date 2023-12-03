"""
URL configuration for app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
# from django.urls import path

# urlpatterns = [
#     path("admin/", admin.site.urls),
# ]
from django.conf import settings
from django.contrib import admin
from django.urls import include, path, URLPattern, URLResolver

# from landing.admin import landing_admin_site
# from landing.api import landing_api

# from vrtour.apiv1 import api as api_v1
# from vrtour.apiv2 import api_v2
# from vrtour.views import show_deeplink_document, show_user_agreement


# Для удобочитаемости и гибкого формирования URLconf разбиваем
# паттерны на блоки. Чтобы не создавать лишних копий в памяти
# и добавить типизацию, упаковываем их в функции. Затем мы их
# распаковываем в `urlpatterns`, соблюдая нужный порядок.
# В итоге избегаем ошибок в порядке объявления и можем,
# при необходимости, формировать паттерны динамически.


def debug_static_urlpatterns() -> tuple[URLPattern, ...]:
    """
    Returns tuple of static url patterns for `MEDIA` and `STATIC` settings
    in DEBUG mode or empty tuple in production runtime.
    """
    if settings.DEBUG:
        from django.conf.urls.static import static

        return (
            *static(settings.STATIC_URL, document_root=settings.STATIC_ROOT),
            *static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT),
        )
    return ()


def admin_site_patterns() -> tuple[URLResolver, ...]:
    """
    Url patterns for admin sites
    """
    return (
        path("admin/", admin.site.urls),
        # path("landing-admin/", landing_admin_site.urls),
    )


def applications_url_patterns() -> tuple[URLResolver, ...]:
    """
    Url patterns for Django apps included
    """
    return (
        # path("", include(landing.urls)),
        # path("process-booking/", include(booking.urls)),
        # path("landmarks/", include(landmarks.urls)),
        # # path("payments/", include(payments.urls)),
        # path("storypoints/", include(heroes.urls)),
        # path("tour360/", include(tour360.urls)),
    )


def standalone_pages_patterns() -> tuple[URLPattern, ...]:
    """
    Url patterns for independent links not related to any app
    """
    return (
        # path("user-agreement/", show_user_agreement),
        # path("link/", show_deeplink_document),
    )


def api_url_patterns() -> tuple:
    """
    Url patterns for Django Ninja API framework endpoints.

    (There is no type hinting in function signature
    because of Ninja framework specifics).
    """
    return (
        # path("api/v1/", api_v1.urls),  # type:ignore
        # path("api/v2/", api_v2.urls),  # type:ignore
        # path("landing-api/", landing_api.urls),  # type:ignore
    )


urlpatterns = [
    *debug_static_urlpatterns(),
    *admin_site_patterns(),
    *applications_url_patterns(),
    *standalone_pages_patterns(),
    *api_url_patterns(),
]
