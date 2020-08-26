""" Communities Model """

from django.db import models


# Utils Model
from eventup.utils.models import GeneralModel


class Community(GeneralModel):

    name = models.CharField(max_length=100, blank=True)
    social_url = models.URLField()
    logo = models.URLField()

    def __str__(self):
        return str(self.name)
