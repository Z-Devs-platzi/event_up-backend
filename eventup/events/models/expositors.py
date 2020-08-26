''' Expositors Model '''

import uuid
from django.db import models


class Expositor(models.Model):
    ''' Expositor Model '''

    # Id
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    # Expositor data
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    bio = models.TextField()
    twitter = models.URLField()
    image = models.URLField()

    STATUS_CHOICES = [
        ('active', 'active'),
        ('inactive', 'inactive'),
    ]
    status = models.CharField(
        choices=STATUS_CHOICES,
        null=False,
        default="active"
    )

    # Modify
    created = models.DateTimeField(auto_now=True)
    modified = models.DateTimeField(auto_now=True, null=True)
    deleted = models.DateTimeField(null=True)

    # Expositors Relations
