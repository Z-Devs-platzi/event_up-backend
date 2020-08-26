""" Layout Model """

from django.db import models


# Utils Model
from eventup.utils.models import GeneralModel


class Layout(GeneralModel):
    """ Layout Model """

    comment = models.TextField()

    def __str__(self):
        return str(self.comment)
