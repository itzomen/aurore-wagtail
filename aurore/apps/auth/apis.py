from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_jwt.views import ObtainJSONWebTokenView

from aurore.apps.api.mixins import ApiAuthMixin
from aurore.apps.auth.services import auth_logout
from aurore.apps.users.selectors import user_get_login_data

from .serializers import (
    LoginInputSerializer,
    UserSerializer,
    UserSessionOutputSerializer,
    UserTokenOutputSerializer,
)


class UserSessionLoginApi(APIView):
    """
    User login with session.
    Following https://docs.djangoproject.com/en/4.0/topics/auth/default/#how-to-log-a-user-in
    """

    @extend_schema(
        request=LoginInputSerializer,
        responses={200: UserSessionOutputSerializer},
    )
    def post(self, request):
        serializer = LoginInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = authenticate(request, **serializer.validated_data)

        if user is None:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        login(request, user)

        data = user_get_login_data(user=user)
        session_key = request.session.session_key

        return Response({"session": session_key, "user": data})


class UserSessionLogoutApi(APIView):
    """
    User logout with session.
    """

    def get(self, request):
        logout(request)

        return Response()

    def post(self, request):
        logout(request)

        return Response()


class UserJwtLoginApi(ObtainJSONWebTokenView):
    @extend_schema(
        responses={200: UserTokenOutputSerializer},
    )
    def post(self, request, *args, **kwargs):
        # We are redefining post so we can change the response status on success
        # Mostly for consistency with the session-based API
        response = super().post(request, *args, **kwargs)

        if response.status_code == status.HTTP_201_CREATED:
            response.status_code = status.HTTP_200_OK

        return response


class UserJwtLogoutApi(ApiAuthMixin, APIView):
    """
    JWT User logout and delete the JWT cookie. Requires the user to be logged in.
    """

    def post(self, request):
        auth_logout(request.user)

        response = Response()

        if settings.JWT_AUTH["JWT_AUTH_COOKIE"] is not None:
            response.delete_cookie(settings.JWT_AUTH["JWT_AUTH_COOKIE"])

        return response


class UserMeApi(ApiAuthMixin, APIView):
    """
    Get the user's data. Requires the user to be logged in.
    """

    @extend_schema(responses={200: UserSerializer})
    def get(self, request):
        data = user_get_login_data(user=request.user)

        return Response(data)
