""" Sponsor Serializer """

# Django REST Framework
from rest_framework import serializers

# Models
from eventup.events.models import Sponsor


class SponsorModelSerializer(serializers.HyperlinkedModelSerializer):
    """ Sponsor model serializer """

    class Meta:
        """ Meta class """
        model = Sponsor
        fields = (
            'id',
            'name',
            'level',
            'web',
            'logo',
        )

    def validate(self, data):

        response = data
        return response

    def create(self, data):
        return Sponsor.objects.create(**data)

    def update(self, instance, validated_data):
        sponsor_validated_data = validated_data.pop('sponsor', None)

        sponsor = instance.sponsor
        sponsor.name = sponsor_validated_data.get('name', sponsor.name)
        sponsor.level = sponsor_validated_data.get('level', sponsor.level)
        sponsor.web = sponsor_validated_data.get('web', sponsor.web)
        sponsor.logo = sponsor_validated_data.get('logo', sponsor.logo)

        sponsor.save()

        instance.save()
        return instance
