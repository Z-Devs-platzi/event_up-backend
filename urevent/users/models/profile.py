"""Profile model."""

# Django
from django.db import models

# Utilities
from urevent.utils.models import GeneralModel

class Profile(GeneralModel):
    """Profile model.

    A profile holds a user's public data like biography, picture,
    and statistics.
    """

    # Extend data from User table
    users = models.OneToOneField('users.Users', on_delete=models.CASCADE)

    # Fields
    biography = models.TextField(max_length=500, blank=True)
    picture = models.ImageField(
        'profile picture',
        upload_to='users/pictures/',
        blank=True,
        null=True
    )

    # Stats
    events_taken = models.PositiveIntegerField(default=0)
    reputation = models.FloatField(
        default=5.0,
        help_text="User's reputation based on the rides taken and offered."
    )

    def __str__(self):
        """Return user's str representation."""
        return str(self.user)
