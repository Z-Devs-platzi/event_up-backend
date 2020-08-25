''' Sponsors Model '''

from django.db import models


class Sponsor(models.Model):
    ''' Sponsors Model '''

    name = models.CharField(max_length=100)
    level = models.CharField(max_length=100)
    logo = models.CharField(max_length=300)
