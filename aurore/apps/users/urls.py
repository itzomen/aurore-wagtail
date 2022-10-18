from django.urls import path

from .apis import UserJwtInitApi, UserApi, UserSessionInitApi

urlpatterns = [
    path("", UserApi.as_view(), name="user"),
    path("session/register", UserSessionInitApi.as_view(), name="session-init"),
    path("jwt/register", UserJwtInitApi.as_view(), name="jwt-init"),
]
