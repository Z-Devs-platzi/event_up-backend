""" Communities Serializer """

# Django REST Framework
from rest_framework import serializers

# Models
from eventup.communities.models import Community


class CommunityModelSerializer(serializers.ModelSerializer):
    """ Community model serializer """

    class Meta:
        """ Meta class """
        model = Community
        fields = (
            'name',
            'social_url',
            'logo'
        )


class CommunityCreateSerializer(serializers.Serializer):
    """ Community create serializer """

    name = serializers.CharField()
    social_url = serializers.URLField()
    logo = serializers.ImageField

    def create(self, data):
        community = Community.objects.create(**data)

        return community
