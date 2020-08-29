""" Sponsor Serializer """

# Django REST Framework
from rest_framework import serializers

# Models
from eventup.events.models import Sponsor


class SponsorModelSerializer(serializers.ModelSerializer):
    """ Sponsor model serializer """

    class Meta:
        """ Meta class """
        model = Sponsor
        fields = (
            'name',
            'level',
            'web',
            'logo',
        )
