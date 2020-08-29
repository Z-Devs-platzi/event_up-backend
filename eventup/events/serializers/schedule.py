""" Events Schedule """

# Django REST Framework
from rest_framework import serializers

# Models
from eventup.events.models import Schedule


class ScheduleModelSerializer(serializers.ModelSerializer):
    """ Schedule model serializer """

    model = Schedule
    fields = (
        'title',
        'data',
        'description',
        'expostiors',
    )
