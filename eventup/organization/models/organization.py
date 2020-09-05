''' Expositors Model '''

import uuid
from django.db import models

# Utils Model
from eventup.utils.models import GeneralModel


class Organization(GeneralModel):
    ''' Expositor Model '''

    # Id
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    # Expositor data
    name = models.CharField('name of organization', max_length=100)
    social_url = models.URLField(max_length=255, blank=True)
    picture = models.ImageField(
        'picture',
        upload_to='organization/pictures/',
        blank=True,
        null=True
    )

    # Expositors Relations

    def __str__(self):
        return str(self.name)
