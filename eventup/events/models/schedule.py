''' Schedule Model '''

from django.db import models

# Utils Model
from eventup.utils.models import GeneralModel


class Schedule(GeneralModel):

    # Schedule data
    title = models.CharField(max_length=300)
    date = models.DateField()
    hour = models.TimeField()

    # Relations
    expositors = models.ManyToManyField(
        to="Expositor"
    )
