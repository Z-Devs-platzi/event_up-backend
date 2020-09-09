''' Expositors Model '''

import uuid
from django.db import models

# Utils Model
from eventup.utils.models import GeneralModel


class Expositor(GeneralModel):
    ''' Expositor Model '''

    # Id
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    # Expositor data
    name = models.CharField('name of expositor', max_length=100)
    email_expositor = models.EmailField(
        'email address',
        unique=True,
        error_messages={
            'unique': 'A expositor with that email already exists.'
        }
    )
    biography = models.CharField(max_length=500, blank=True)
    twitter = models.URLField(max_length=255, blank=True)
    picture = models.ImageField(
        'profile picture',
        upload_to='expositors/pictures/',
        blank=True,
        null=True
    )

    # Expositors Relations

    def __str__(self):
        return str(self.name)
