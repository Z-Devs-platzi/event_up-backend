""" Templates Model """

from django.db import models

# Utils Model
from eventup.utils.models import GeneralModel


class Template(GeneralModel):
    """ Template Model """

    name = models.CharField(max_length=100, unique=True, blank=True)
    colors = models.CharField(max_length=255)
    banner = models.URLField()
    font = models.CharField(max_length=100, blank=True)

    # Templates Relations
    layout = models.ForeignKey(
        to="Layout",
        on_delete=models.SET_NULL,
        null=True,
    )

    def __str__(self):
        return str(self.name)
