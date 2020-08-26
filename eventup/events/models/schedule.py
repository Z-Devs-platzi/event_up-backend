''' Schedule Model '''

from django.db import models


class Schedule(models.Model):

    date = models.DateField()
    hour = models.TimeField()

    STATUS_CHOICES = [
        ('active', 'active'),
        ('inactive', 'inactive'),
    ]
    status = models.CharField(
        choices=STATUS_CHOICES,
        null=False,
        default="active"
    )

    # Modify
    created = models.DateTimeField(auto_now=True)
    modified = models.DateTimeField(auto_now=True, null=True)
    deleted = models.DateTimeField(null=True)
