from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(("aurore.apps.api.urls", "api"))),
    # this is placed at the end of the urlpatterns list,
    # so that it does not override more specific URL patterns.
    path("", include(("aurore.apps.cms.urls", ""))),
]


if settings.DEBUG:
    # setting this to view media files from admin panel
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
