""" Templates Model """

from django.db import models

# Utils Model
from eventup.utils.models import GeneralModel


class Template(GeneralModel):
    """ Template Model """

    name = models.CharField(max_length=100, unique=True, blank=True)
    colors = models.TextField()
    banner = models.URLField()
    font = models.CharField(max_length=100, blank=True)

    # Templates Relations
    layout_id = models.ManyToManyField(
        to="Layout"
    )
