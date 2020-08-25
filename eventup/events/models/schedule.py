''' Schedule Model '''

from django.db import models


class Schedule(models.Model):

    date = models.DateField()
    hour = models.TimeField()
