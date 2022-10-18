from django.urls import include, path
from wagtail.admin import urls as wagtailadmin_urls

from aurore.apps.cms.api import api_router

# from wagtail import urls as wagtail_urls
# from wagtail.documents import urls as wagtaildocs_urls


urlpatterns = [
    path("cms/", include(wagtailadmin_urls)),
    # path("documents/", include(wagtaildocs_urls)),
    path("api/pages/v2/", api_router.urls),
    # re_path("", include(wagtail_urls)),
]
