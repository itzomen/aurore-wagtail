import uuid

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.models import UserManager as BUM
from django.db import models
from django.db.models import Value
from django.utils.translation import gettext_lazy as _
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField

from aurore.apps.common.choices import Gender
from aurore.apps.common.models import BaseModel, Options

from .validators import validate_possible_number


class PossiblePhoneNumberField(PhoneNumberField):
    """Less strict field for phone numbers written to database."""

    default_validators = [validate_possible_number]


# Taken from here:
# https://docs.djangoproject.com/en/3.0/topics/auth/customizing/#a-full-example
# With some modifications


class UserManager(BUM):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Users must have an email address")

        email = self.normalize_email(email.lower())
        user = self.model(email=email, **extra_fields)

        if password is not None:
            user.set_password(password)
        else:
            user.set_unusable_password()

        user.full_clean()
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_admin", True)
        extra_fields.setdefault("is_active", True)
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")
        return self.create_user(email, password, **extra_fields)


class AddressQueryset(models.QuerySet):
    def annotate_default(self, user):
        # Set default shipping/billing address pk to None
        # if default shipping/billing address doesn't exist
        default_shipping_address_pk, default_billing_address_pk = None, None
        if user.default_shipping_address:
            default_shipping_address_pk = user.default_shipping_address.pk
        if user.default_billing_address:
            default_billing_address_pk = user.default_billing_address.pk

        return user.addresses.annotate(
            user_default_shipping_address_pk=Value(
                default_shipping_address_pk, models.IntegerField()
            ),
            user_default_billing_address_pk=Value(
                default_billing_address_pk, models.IntegerField()
            ),
        )


class Address(models.Model):
    name = models.CharField(_("Name"), max_length=255, blank=True)
    first_name = models.CharField(_("First name"), max_length=255, blank=True)
    last_name = models.CharField(_("Last name"), max_length=255, blank=True)
    company_name = models.CharField(
        _("Company name"), max_length=255, blank=True, default=""
    )
    street_address_1 = models.CharField(
        _("Street address 1"), max_length=255, blank=True
    )
    street_address_2 = models.CharField(
        _("Street address 2"), max_length=255, blank=True
    )
    city = models.CharField(_("City"), max_length=255, blank=True)
    city_area = models.CharField(_("City area"), max_length=255, blank=True, default="")
    country = CountryField(
        _("Country"),
        blank=True,
        default="",
        help_text=_("Country of the address."),
    )
    country_area = models.CharField(
        _("Country area"), max_length=255, blank=True, default=""
    )
    postal_code = models.CharField(
        _("Postal code"), max_length=255, blank=True, default=""
    )
    phone = PossiblePhoneNumberField(
        _("Phone number"),
        blank=True,
        default="",
        help_text=_("In case we need to call you."),
    )

    objects = models.Manager.from_queryset(AddressQueryset)()

    class Meta:
        ordering = ("pk",)
        verbose_name = _("Address")
        verbose_name_plural = _("Addresses")

    @property
    def full_name(self):
        return "%s %s" % (self.first_name, self.last_name)

    def __str__(self):
        if self.company_name:
            return "%s - %s" % (self.company_name, self.full_name)
        return self.full_name

    def __eq__(self, other):
        if not isinstance(other, Address):
            return False
        return self.as_data() == other.as_data()

    __hash__ = models.Model.__hash__

    def get_copy(self):
        """Return a new instance of the same address."""
        return Address.objects.create(**self.as_data())


class UserOptions(models.Model):
    user = models.ForeignKey(
        "User", related_name="useroptions", on_delete=models.CASCADE
    )
    options = models.ForeignKey(
        "common.Options", related_name="useroptions", on_delete=models.CASCADE
    )


class User(BaseModel, AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        verbose_name=_("Email"),
        max_length=255,
        unique=True,
    )

    # Custom fields
    first_name = models.CharField(
        verbose_name=_("First name"), max_length=30, blank=True
    )
    last_name = models.CharField(verbose_name=_("Last name"), max_length=30, blank=True)
    avatar = models.ImageField(
        verbose_name=_("Profile image"),
        upload_to="users/avatars",
        blank=True,
        null=True,
    )
    phone_number = models.CharField(
        verbose_name=_("Phone number"), max_length=30, blank=True
    )
    gender = models.CharField(
        _("Gender"), max_length=2, choices=Gender.choices, default=Gender.M
    )
    date_of_birth = models.DateField(
        verbose_name=_("Date of birth"), blank=True, null=True
    )
    options = models.ManyToManyField(
        Options,
        verbose_name=_("Options"),
        related_name="options",
        through=UserOptions,
        blank=True,
        through_fields=("user", "options"),
    )
    #
    addresses = models.ManyToManyField(
        Address, blank=True, related_name="user_addresses"
    )
    default_shipping_address = models.ForeignKey(
        Address, related_name="+", null=True, blank=True, on_delete=models.SET_NULL
    )
    default_billing_address = models.ForeignKey(
        Address, related_name="+", null=True, blank=True, on_delete=models.SET_NULL
    )

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    # This should potentially be an encrypted field
    jwt_key = models.UUIDField(default=uuid.uuid4)
    #
    social_auth = models.BooleanField(default=False)
    note = models.TextField(null=True, blank=True)

    # payment_method
    # brands 1-*

    objects = UserManager()

    USERNAME_FIELD = "email"
    # REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    def is_staff(self):
        return self.is_admin

    @property
    def name(self):
        if not self.last_name:
            return self.first_name.capitalize()

        return f"{self.first_name.capitalize()} {self.last_name.capitalize()}"
