""" Events Serializer """

# Django REST Framework
from rest_framework import serializers

# Models
from eventup.events.models import Event


class EventModelSerializer(serializers.HyperlinkedModelSerializer):
    """ Event model serializer """

    class Meta:
        """ Meta class """

        model = Event
        fields = (
            'id',
            'name',
            'date',
            'description',
            'url',
            'banner_img',
            'banner_title',
            # 'template',
            # 'sponsor',
            # 'schedule',
        )

    def validate(self, data):

        response = data
        return response

    def create(self, data):
        return Event.objects.create(**data)

    def update(self, instance, validated_data):
        event_validated_data = validated_data.pop('event', None)

        event = instance.event
        event.name = event_validated_data.get('name', event.name)
        event.date = event_validated_data.get('date', event.date)
        event.description = event_validated_data.get('description', event.description)
        event.url = event_validated_data.get('url', event.url)
        event.banner_img = event_validated_data.get('banner_img', event.banner_img)
        event.banner_title = event_validated_data.get('')

        event.save()

        instance.save()
        return instance
