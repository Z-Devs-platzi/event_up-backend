""" Organization Serializer """

# Django REST Framework
from rest_framework import serializers

# Models
from eventup.organization.models import Organization


class OrganizationModelSerializer(serializers.ModelSerializer):
    """ Organization model serializer """

    class Meta:
        """ Meta class """
        model = Organization
        fields = (
            'name',
            'social_url',
            'logo'
        )


class OrganizationCreateSerializer(serializers.Serializer):
    """ Organization create serializer """

    name = serializers.CharField()
    social_url = serializers.URLField()
    logo = serializers.ImageField

    def create(self, data):
        organization = Organization.objects.create(**data)

        return organization
