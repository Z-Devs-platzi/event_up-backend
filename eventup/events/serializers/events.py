""" Events Serializer """

# Django REST Framework
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

# Models
from eventup.events.models import Event

# Serializers
from eventup.event_templates.serializers.template import TemplateModelSerializer


class EventModelSerializer(serializers.HyperlinkedModelSerializer):
    """ Event model serializer """

    id = serializers.CharField(source='pk', read_only=True)
    template = TemplateModelSerializer(read_only=True)

    class Meta:
        """ Meta class """

        model = Event
        # read_only_fields
        fields = (
            'id',
            'name',
            'date',
            'description',
            'banner_img',
            'banner_title',
            'url',
            'template',
            # 'sponsor',
            # 'schedule',
        )


class CreateUpdateEventSerializer(serializers.HyperlinkedModelSerializer):
    """Create expositor serializer."""

    id = serializers.CharField(source='pk', read_only=True)

    url = serializers.URLField(
        validators=[UniqueValidator(queryset=Event.objects.all())]
    )

    class Meta:
        """ Meta class """

        model = Event
        # read_only_fields
        fields = (
            'id',
            'name',
            'date',
            'description',
            'banner_title',
            'banner_img',
            'url',
            'colors',
            'font',
            'layout_id',
            # 'sponsor',
            # 'schedule',
        )

    # def create(self, data):
    #     CreateUpdateTemplateSerializer
