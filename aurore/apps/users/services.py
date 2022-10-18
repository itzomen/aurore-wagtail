from typing import Optional

from django.db import transaction

from aurore.apps.common.services import model_update
from aurore.apps.users.models import User
from aurore.apps.utils.datetime import get_now


def user_create(*, email: str, password: Optional[str] = None, **extra_fields) -> User:
    extra_fields = {"is_active": True, "is_admin": False, **extra_fields}

    user = User.objects.create_user(email=email, password=password, **extra_fields)

    return user


@transaction.atomic
def user_update(*, user: User, data) -> User:
    non_side_effect_fields = ["first_name", "last_name"]

    user, has_updated = model_update(
        instance=user, fields=non_side_effect_fields, data=data
    )

    # Side-effect fields update here (e.g. username is generated based on first & last name)

    # ... some additional tasks with the user ...

    return user


def user_record_login(*, user: User) -> User:
    user.last_login = get_now()
    user.save(update_fields=["last_login"])

    return user
