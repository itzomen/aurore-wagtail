from django.db.models.query import QuerySet

from .filters import UserFilter
from .models import User


def user_get_login_data(*, user: User):
    return {
        "id": user.id,
        "email": user.email,
        "name": user.name,
        "is_active": user.is_active,
        "is_admin": user.is_admin,
        "first_name": user.first_name,
        "last_name": user.last_name,
        "last_login": user.last_login,
    }


def user_get(*, id: int) -> User:
    return User.objects.get(id=id)


def user_list(*, filters=None) -> QuerySet[User]:
    filters = filters or {}

    qs = User.objects.all()

    return UserFilter(filters, qs).qs
