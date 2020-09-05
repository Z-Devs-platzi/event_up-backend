""" Organizations Serializer """

# Django REST Framework
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

# Models
from eventup.organization.models import Organization


class OrganizationModelSerializer(serializers.ModelSerializer):
    """ Organization model serializer """

    id = serializers.CharField(source='pk', read_only=True)

    class Meta:
        """Meta class."""

        fields = '__all__'
        model = Organization
        # read_only_fields
        fields = (
            'id',
            'name',
            'social_url',
            # 'picture'
        )


class CreateUpdateOrganizationSerializer(OrganizationModelSerializer):
    """Create organization serializer."""

    social_url = serializers.CharField(
        validators=[UniqueValidator(queryset=Organization.objects.all())]
    )
