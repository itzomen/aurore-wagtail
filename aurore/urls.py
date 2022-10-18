"""aurore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
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
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
