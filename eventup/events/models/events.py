''' Events Model '''

import uuid
from django.db import models


class Event(models.Model):
    ''' Event Model '''
    # Id
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    # Event data
    name = models.CharField(max_length=100, unique=True)
    date = models.DateField()
    hour = models.TimeField()
    description = models.TextField()
    url = models.URLField()
    banner = models.URLField()
    logo = models.URLField()

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

    # Event Relations
