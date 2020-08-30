"""Profile model."""

# Django
from django.db import models

# Utilities
from eventup.utils.models import GeneralModel


class RoleAdmin(GeneralModel):
    """Role Admin model.

    The role base of the user main.
    """
    name = models.TextField(max_length=500, blank=False, null=False)

    def __str__(self):
        """Return user's str representation."""
        return str(self.name)
