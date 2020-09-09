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
    name = models.CharField('name of event', max_length=100, unique=True)
    date = models.DateTimeField('date of event', null=True, blank=True)
    description = models.CharField('description of event', max_length=500)
    url = models.URLField('autogenerate url of event', )
    banner_title = models.CharField(
        'title to search in dashboard about of the specific event', max_length=300, blank=True)
    banner_img = models.ImageField(
        'banner of event',
        upload_to='event/banner/',
        blank=True,
        null=True
    )
    code = models.BigIntegerField('code of the party (Share and more)', editable=False, unique=True)

    # Event Relations
    template = models.ForeignKey(
        to="event_templates.Template",
        on_delete=models.SET_NULL
    )
    sponsor = models.ManyToManyField(
        to="Sponsor",
    )
    schedule = models.ManyToManyField(
        to="Schedule",
    )

    def __str__(self):
        return str(self.name)
