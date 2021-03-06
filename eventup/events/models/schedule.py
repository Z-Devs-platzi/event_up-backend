''' Schedule Model '''

from django.db import models

# Utils Model
from eventup.utils.models import GeneralModel


class Schedule(GeneralModel):

    # Schedule data
    title = models.CharField(max_length=300, blank=True)
    date = models.DateTimeField(null=True, blank=True)
    description = models.CharField(max_length=500, null=True, blank=True)

    # Relations
    expositors = models.ManyToManyField(
        to="Expositor"
    )

    def __str__(self):
        return str(self.title)
