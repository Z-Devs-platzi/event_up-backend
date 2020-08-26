''' Schedule Model '''

from django.db import models

# Utils Model
from eventup.utils.models import GeneralModel


class Schedule(GeneralModel):

    # Schedule data
    title = models.CharField(max_length=300, blank=True)
    date = models.DateField()
    hour = models.TimeField(null=True, blank=True)

    # Relations
    expositors = models.ManyToManyField(
        to="Expositor"
    )

    def __str__(self):
        return str(self.title)
