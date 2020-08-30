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


class SponsorCreateSerializer(serializers.Serializer):
    """ Sponsor create serializer """

    name = serializers.CharField()
    level = serializers.CharField()
    web = serializers.URLField()
    logo = serializers.ImageField()

    def create(self, data):
        sponsor = Sponsor.objects.create(**data)

        return sponsor
