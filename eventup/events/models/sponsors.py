''' Sponsors Model '''

from django.db import models


class Sponsor(models.Model):
    ''' Sponsors Model '''

    name = models.CharField(max_length=100)
    level = models.CharField(max_length=100)
    logo = models.CharField(max_length=300)

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
