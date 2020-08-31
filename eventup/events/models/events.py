''' Events Model '''

import uuid
from django.db import models

# Utils Model
from eventup.utils.models import GeneralModel


class Event(GeneralModel):
    ''' Event Model '''
    # Id
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    # Event data
    name = models.CharField(max_length=100, unique=True)
    date = models.DateTimeField(null=True, blank=True)
    description = models.CharField(max_length=500)
    url = models.URLField()
    banner_img = models.ImageField(
        'banner picture',
        upload_to='banner/pictures/',
        blank=True,
        null=True
    )
    banner_title = models.CharField(max_length=300, blank=True)

    # Event Relations
    template = models.ForeignKey(
        to="event_templates.Template",
        on_delete=models.SET_NULL,
        null=True,
    )
    sponsor = models.ManyToManyField(
        to="Sponsor",
    )

    schedule = models.ManyToManyField(
        to="Schedule",
    )

    def __str__(self):
        return str(self.name)
