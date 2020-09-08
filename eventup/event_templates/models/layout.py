""" Layout Model """

# Django Library
from django.db import models

# Utils Model
from eventup.utils.models import GeneralModel


class Layout(GeneralModel):
    """ Layout Model """
    # # Id
    # id = models.BigAutoField(primary_key=True, editable=False)

    # Organization data
    comment = models.CharField('description of the component/layout base to the event', max_length=500)

    def __str__(self):
        return str(self.comment)
