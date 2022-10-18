from django.db import models
from django.utils.translation import gettext_lazy as _


class Gender(models.TextChoices):
    M = "M", _("Male")
    F = "F", _("Female")
