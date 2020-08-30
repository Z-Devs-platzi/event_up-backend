""" Organization Model """

from django.db import models


# Utils Model
from eventup.utils.models import GeneralModel


class Organization(GeneralModel):

    name = models.CharField(max_length=100, blank=True)
    social_url = models.URLField(max_length=255)
    logo = models.ImageField(
        'banner picture',
        upload_to='banner/pictures/',
        blank=True,
        null=True
    )

    def __str__(self):
        return str(self.name)
