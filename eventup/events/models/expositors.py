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
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    bio = models.TextField()
    twitter = models.URLField()
    image = models.URLField()

    # Expositors Relations

    def __str__(self):
        return str(self.first_name)
