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
            'id',
            'name',
            'social_url',
            'logo'
        )

    def validate(self, data):

        response = data
        return response

    def create(self, data):
        return Organization.objects.create(**data)

    def update(self, instance, validated_data):
        organization_validated_data = validated_data.pop('organization', None)

        organization = instance.organization
        organization.name = organization_validated_data.get('name', organization.name)
        organization.social_url = organization_validated_data.get('social_url', organization.social_url)
        organization.logo = organization_validated_data.get('logo', organization.logo)

        organization.save()

        instance.save()
        return instance
