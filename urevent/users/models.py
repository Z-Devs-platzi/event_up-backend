"""User model"""

# Django
from django.db import models
from django.contrib.auth.models import AbstractUser

# Utilities
from urevent.utils.models import GeneralModel


class User(GeneralModel, AbstractUser):
    """User model

    Extend from Django's Abstract User, change and add data to your event app - C3 <Z-Devs>
    """

    # Fields
    email = models.EmailField(
        'email address',
        unique=True,
        error_messages={
            'unique': 'This email already exist in the database'
        }
    )

    phone_regex = RegexValidator(
        regex=r'\+?1?\d{9,15}$',
        message="Phone number must be entered in the format: +999999999. Up to 15 digits allowed."
    )
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)

    is_client = models.BooleanField(
        'client status'
        default=False,
        help_text=(
            'Help easily distinguish users and perform queries. '
            'Clients are the main type of user.'
        )
    )

    is_verfied = models.BooleanField(
        'verified',
        default=False,
        help_text='Set to true when the user have verified its email address.'
    )

    # Reset data - Model Abstract User
    USERNAME_FIELD = 'email' # main
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    # ABS Functions
    def __str__(self):
        """Return username."""
        return self.username

    def get_short_name(self):
        """Return username."""
        return self.username
