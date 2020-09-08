""" Organizations Serializer """

# Libs
import random

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

        # fields = '__all__'
        model = Organization
        # read_only_fields
        fields = (
            'id',
            'name',
            'social_url',
            'code'
            # 'picture'
        )


class CreateUpdateOrganizationSerializer(OrganizationModelSerializer):
    """Create organization serializer."""

    social_url = serializers.CharField(
        validators=[UniqueValidator(queryset=Organization.objects.all())]
    )

    def validate(self, data):
        """Verify passwords match."""
        # Check Organization Name
        if 'name_organization' in data and Organization.objects.filter(name=data):
            raise serializers.ValidationError("Another user already has this organization name.")

    def create(self, data):
        # return Organization.objects.create(**data, code=random.randrange(1000, 9999))
        return Organization.objects.create(name=data, code=random.randrange(1000, 9999))
