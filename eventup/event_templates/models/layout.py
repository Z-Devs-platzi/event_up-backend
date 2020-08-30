""" Layout Model """

from django.db import models


# Utils Model
from eventup.utils.models import GeneralModel


class Layout(GeneralModel):
    """ Layout Model """

    comment = models.CharField(max_length=500)

    def __str__(self):
        return str(self.comment)
