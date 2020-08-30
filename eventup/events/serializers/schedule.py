""" Events Schedule """

# Django REST Framework
from rest_framework import serializers

# Models
from eventup.events.models import Schedule


class ScheduleModelSerializer(serializers.ModelSerializer):
    """ Schedule model serializer """

    class Meta:
        """ Meta class """
        model = Schedule
        fields = (
            'title',
            'date',
            'description',
            'expostiors',
        )


class ScheduleCreateSerializer(serializers.Serializer):
    """ Schedule create serializer """

    title = serializers.CharField()
    date = serializers.DateTimeField()
    description = serializers.CharField()

    def create(self, data):
        schedule = Schedule.objects.create(**data)

        return schedule
