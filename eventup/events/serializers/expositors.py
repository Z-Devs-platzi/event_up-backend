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

    # def validate(self, data):
    #     """Validate.

    #     Verify that the person who offers the expositor is real.
    #     """
    #     # expositor = self.context['expositor']
    #     return data

    # def create(self, data):
    #     """Create expositor and update stats."""
    #     # expositor = self.context['expositor']
    #     print(data)
    #     expositor = Expositor.objects.create(**data)
    #     expositor.save()

    #     return expositor
