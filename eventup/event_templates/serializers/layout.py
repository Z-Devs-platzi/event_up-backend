""" Layout Serializer """

# Django REST Framework
from rest_framework import serializers

# Models
from eventup.event_templates.models import Layout


class LayoutModelSerializer(serializers.HyperlinkedModelSerializer):
    """ Layout model serializer """

    class Meta:
        """ Meta class """
        model = Layout
        fields = (
            'id',
            'comment',
        )

    def validate(self, data):

        response = data
        return response

    def create(self, data):
        return Layout.objects.create(**data)

    def update(self, instance, validated_data):
        layout_validated_data = validated_data.pop('layout', None)

        layout = instance.layout
        layout.comment = layout_validated_data.get('comment', layout.comment)

        layout.save()
        instance.save()
        return instance
