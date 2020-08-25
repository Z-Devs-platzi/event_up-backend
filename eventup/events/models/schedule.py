''' Schedule Model '''

from django.db import models


class Schedule(models.Model):

    date = models.DateField()
    hour = models.TimeField()

    # Modify
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
