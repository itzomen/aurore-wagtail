import django_filters

from aurore.apps.users.models import User


class UserFilter(django_filters.FilterSet):
    class Meta:
        model = User
        fields = ("id", "email", "is_admin")
