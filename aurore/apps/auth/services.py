import uuid

from django.http import HttpRequest, HttpResponse
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED
from rest_framework_jwt.compat import set_cookie_with_token
from rest_framework_jwt.settings import api_settings
from rest_framework_jwt.utils import unix_epoch

from aurore.apps.users.models import User
from aurore.apps.users.selectors import user_get_login_data


def jwt_login(*, request: HttpRequest, user: User) -> HttpResponse:
    jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
    jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
    jwt_create_response_payload = api_settings.JWT_RESPONSE_PAYLOAD_HANDLER

    payload = jwt_payload_handler(user)
    token = jwt_encode_handler(payload)
    issued_at = payload.get("iat", unix_epoch())

    data = jwt_create_response_payload(token, user, request, issued_at)

    response = Response(data, status=HTTP_201_CREATED)
    # Ref: https://github.com/Styria-Digital/django-rest-framework-jwt/blob/master/src/rest_framework_jwt/compat.py#L43
    if api_settings.JWT_AUTH_COOKIE:
        set_cookie_with_token(response, api_settings.JWT_AUTH_COOKIE, token)

    return response


def auth_user_get_jwt_secret_key(user: User) -> str:
    return str(user.jwt_key)


def auth_jwt_response_payload_handler(token, user=None, request=None, issued_at=None):
    """
    Default implementation. Add whatever suits you here.
    """
    return {
        "token": token,
        "user": user_get_login_data(user=user),
        "issued_at": issued_at,
    }


def auth_logout(user: User) -> User:
    user.jwt_key = uuid.uuid4()
    user.full_clean()
    user.save(update_fields=["jwt_key"])

    return user
