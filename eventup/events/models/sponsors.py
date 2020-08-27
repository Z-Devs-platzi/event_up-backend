''' Sponsors Model '''

from django.db import models

# Utils Model
from eventup.utils.models import GeneralModel


class Sponsor(GeneralModel):
    ''' Sponsors Model '''

    name = models.CharField(max_length=100)
    level = models.CharField(max_length=100)
    web = models.URLField()
    logo = models.CharField(max_length=300)

    def __str__(self):
        return str(self.name)
