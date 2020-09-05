""" Expositors Serializer """

# Django REST Framework
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

# Models
from eventup.events.models import Expositor


class ExpositorModelSerializer(serializers.ModelSerializer):
    """ Expositor model serializer """

    id = serializers.CharField(source='pk', read_only=True)

    class Meta:
        """Meta class."""

        fields = '__all__'
        model = Expositor
        # read_only_fields
        fields = (
            'id',
            'name',
            'email_expositor',
            'biography',
            'twitter',
            'picture'
        )


class CreateExpositorSerializer(ExpositorModelSerializer):
    """Create expositor serializer."""

    email_expositor = serializers.EmailField(
        validators=[UniqueValidator(queryset=Expositor.objects.all())]
    )
