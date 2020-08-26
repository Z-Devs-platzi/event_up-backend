"""Django models utilities."""

# Django
from django.db import models


class GeneralModel(models.Model):
    """Event Up base model.
    GeneralModel acts as an abstract base class from which every
    other model in the project will inherit. This class provides
    every table with the following attributes:

        + created (DateTime): Store the datetime the object was created.
        + modified (DateTime): Store the last datetime the object was modified.
    """

    STATUS_CHOICES = [
        ('active', 'active'),
        ('inactive', 'inactive'),
    ]
    status = models.CharField(
        choices=STATUS_CHOICES,
        max_length=15,
        null=False,
        default="active"
    )

    created = models.DateTimeField(
        'created at',
        auto_now_add=True,
        help_text='Date time on which the object was created.'
    )
    modified = models.DateTimeField(
        'modified at',
        auto_now=True,
        help_text='Date time on which the object was last modified.'
    )
    deleted = models.DateTimeField(
        'deleted at',
        auto_now=True,
        help_text='Date time on which the object was delete.'
    )

    class Meta:
        """Meta option."""
        # Allow in al models/contrlores/etc...
        abstract = True
        # Config
        get_latest_by = 'created'
        ordering = ['-created', '-modified']
