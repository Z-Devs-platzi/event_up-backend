''' Events Model '''

import uuid
from django.db import models


class Event(models.Model):
    ''' Event Model '''
    # Id
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    # Event Relations

    # Event data
    name = models.CharField(max_length=100, unique=True)
    date = models.DateField()
    hour = models.TimeField()
    description = models.TextField()
    url = models.CharField(max_length=300)
    banner = models.CharField(max_length=300)
    logo = models.CharField(max_length=300)
