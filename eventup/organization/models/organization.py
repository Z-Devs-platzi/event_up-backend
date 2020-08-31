""" Organization Model """

from django.db import models


# Utils Model
from eventup.utils.models import GeneralModel


class Organization(GeneralModel):

    name = models.CharField(max_length=100)
    social_url = models.URLField(max_length=255, blank=True)
    logo = models.ImageField(
        'logo',
        upload_to='organization_logo/pictures/',
        blank=True,
        null=True
    )

    def __str__(self):
        return str(self.name)
