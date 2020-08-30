""" Layout Serializer """

# Django REST Framework
from rest_framework import serializers

# Models
from eventup.event_templates.models import Layout


class LayoutModelSerializer(serializers.ModelSerializer):
    """ Layout model serializer """

    class Meta:
        """ Meta class """
        model = Layout
        fields = (
            'commet'
        )


class LayoutCreateSerializer(serializers.Serializer):
    """ Layout create serializer """

    comment = serializers.CharField()

    def create(self, data):
        layout = Layout.objects.create(**data)

        return layout
