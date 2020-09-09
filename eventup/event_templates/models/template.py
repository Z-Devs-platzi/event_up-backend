""" Templates Model """

from django.db import models

# Utils Model
from eventup.utils.models import GeneralModel


class Template(GeneralModel):
    """ Template Model """
    # # Id
    # id = models.BigAutoField(primary_key=True, editable=False)
    # Data
    colors = models.CharField(max_length=255)
    font = models.CharField(max_length=300, blank=True)

    # Relations
    # Templates Relations
    layout = models.ForeignKey('event_templates.Layout', on_delete=models.SET_NULL, null=True)
