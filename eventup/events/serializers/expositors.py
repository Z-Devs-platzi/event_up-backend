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


class ExpositorCreateSerializer(serializers.Serializer):
    """ Expositor create serializer """

    name = serializers.CharField()

    def create(self, data):
        expositor = Expositor.objects.create(**data)

        return expositor
