''' Schedule Model '''

from django.db import models

# Utils Model
from eventup.utils.models import GeneralModel


class Schedule(GeneralModel):

    date = models.DateField()

    expositors = models.ManyToManyField(
        to="Expositor"
    )
