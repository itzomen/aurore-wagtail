from django.contrib.auth import login
from drf_spectacular.utils import extend_schema
from rest_framework.response import Response
from rest_framework.views import APIView

from aurore.apps.api.mixins import ApiAuthMixin
from aurore.apps.api.pagination import LimitOffsetPagination, get_paginated_response
from aurore.apps.auth.serializers import (
    UserSessionOutputSerializer,
    UserTokenOutputSerializer,
)
from aurore.apps.auth.services import jwt_login

from .selectors import user_get_login_data, user_list
from .serializers import UserFilterSerializer, UserInitSerializer, UserSerializer
from .services import user_create


class UserSessionInitApi(APIView):
    """
    Register a new user and login with session.
    """

    @extend_schema(
        request=UserInitSerializer,
        responses={200: UserSessionOutputSerializer},
    )
    def post(self, request):
        serializer = UserInitSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = user_create(**serializer.validated_data)

        login(request, user)

        data = user_get_login_data(user=user)
        session_key = request.session.session_key

        return Response({"session": session_key, "user": data})


class UserJwtInitApi(APIView):
    """
    Register a new user and login with jwt.
    """

    @extend_schema(
        request=UserInitSerializer,
        responses={200: UserTokenOutputSerializer},
    )
    def post(self, request):
        serializer = UserInitSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = user_create(**serializer.validated_data)

        response = jwt_login(request=request, user=user)

        return response


# TODO: When JWT is resolved, add authenticated version
class UserApi(ApiAuthMixin, APIView):
    class Pagination(LimitOffsetPagination):
        default_limit = 1

    @extend_schema(
        parameters=[UserFilterSerializer],
        responses={200: UserSerializer(many=True)},
    )
    def get(self, request):
        # Make sure the filters are valid, if passed
        filters_serializer = UserFilterSerializer(data=request.query_params)
        filters_serializer.is_valid(raise_exception=True)

        users = user_list(filters=filters_serializer.validated_data)

        return get_paginated_response(
            pagination_class=self.Pagination,
            serializer_class=UserSerializer,
            queryset=users,
            request=request,
            view=self,
        )

    # TODO: update
