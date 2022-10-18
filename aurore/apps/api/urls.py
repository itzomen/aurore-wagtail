from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView


urlpatterns = [
    path("", SpectacularSwaggerView.as_view(url_name="api:schema"), name="swagger-ui"),
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    #
    path("auth/", include(("aurore.apps.auth.urls", "auth"))),
    path("users/", include(("aurore.apps.users.urls", "users"))),
    path("errors/", include(("aurore.apps.errors.urls", "errors"))),
    path("files/", include(("aurore.apps.files.urls", "files"))),
    #
    # Check main urls in aurore.urls
    # path("cms/v2/", api_router.urls),
]
