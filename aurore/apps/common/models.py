import datetime

import pytz
from django.core.validators import MaxLengthValidator
from django.db import models
from django.db.models import Q
from django.utils import timezone


class BaseModel(models.Model):
    """
    BaseModel
    """

    created_at = models.DateTimeField(db_index=True, default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class PublishedQuerySet(models.QuerySet):
    def published(self):
        today = datetime.datetime.now(pytz.UTC)
        return self.filter(
            Q(published_at__lte=today) | Q(published_at__isnull=True),
            is_published=True,
        )


class PublishableModel(models.Model):
    published_at = models.DateTimeField(blank=True, null=True)
    is_published = models.BooleanField(default=False)

    objects = models.Manager.from_queryset(PublishedQuerySet)()

    class Meta:
        abstract = True

    @property
    def is_visible(self):
        return self.is_published and (
            self.published_at is None
            or self.published_at <= datetime.datetime.now(pytz.UTC)
        )


class SeoModel(models.Model):
    seo_title = models.CharField(
        max_length=70, blank=True, null=True, validators=[MaxLengthValidator(70)]
    )
    seo_description = models.CharField(
        max_length=300, blank=True, null=True, validators=[MaxLengthValidator(300)]
    )

    class Meta:
        abstract = True


class Options(models.Model):
    """
    Selectable options with name, type and value
    """

    name = models.CharField(max_length=255, unique=True)
    type = models.CharField(max_length=30)
    value = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Option"
        verbose_name_plural = "Options"

    def __str__(self):
        return self.name
