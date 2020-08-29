"""User model."""

# Django
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

# Utilities
from eventup.utils.models import GeneralModel


class Users(GeneralModel, AbstractUser):
    """User model.


    Extend from Django's Abstract User, change and add data to your event app - C3 <Z-Devs>
    """

    # Fields
    email = models.EmailField(
        'email address',
        unique=True,
        error_messages={
            'unique': 'A user with that email already exists.'
        }
    )
    name = models.CharField(
        'name of user',
        max_length=100,
        blank=False,
        null=False
    )

    phone_regex = RegexValidator(
        regex=r'\+?1?\d{9,15}$',
        message="Phone number must be entered in the format: +999999999. Up to 15 digits allowed."
    )
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True, null=True)

    is_client = models.BooleanField(
        'client',
        default=True,
        help_text=(
            'Help easily distinguish users and perform queries. '
            'Clients are the main type of user.'
        )
    )

    is_verified = models.BooleanField(
        'verified',
        default=False,
        help_text='Set to true when the user have verified its email address.'
    )

    # Reset data - Model Abstract User
    # Main Object
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'name']

    # ABS Functions
    def __str__(self):
        """Return username."""
        return self.username

    def get_short_name(self):
        """Return username."""
        return self.username
