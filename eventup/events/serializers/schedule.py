""" Events Schedule """

# Django REST Framework
from rest_framework import serializers

# Models
from eventup.events.models import Schedule


class ScheduleModelSerializer(serializers.HyperlinkedModelSerializer):
    """ Schedule model serializer """

    class Meta:
        """ Meta class """
        model = Schedule
        fields = (
            'pk',
            'title',
            'date',
            'description',
            # 'expostiors',
        )

    def validate(self, data):
        response = data
        return response

    def create(self, data):
        return Schedule.objects.create(**data)

    def update(self, instance, validated_data):
        schedule_validate_data = validated_data.get('schedule', None)

        schedule = instance.schedule
        schedule.title = schedule_validate_data.get('title', schedule.title)
        schedule.date = schedule_validate_data.get('date', schedule.date)
        schedule.description = schedule_validate_data.get('description', schedule.description)

        schedule.save()

        instance.save()
        return instance
