""" Expositors Serializer """

# Django REST Framework
from rest_framework import serializers

# Models
from eventup.events.models import Expositor


class ExpositorModelSerializer(serializers.ModelSerializer):

    class Meta:
        """ Meta class """

        model = Expositor
        fields = (
            'name',
            'bio',
            'twitter',
            'image',
        )
