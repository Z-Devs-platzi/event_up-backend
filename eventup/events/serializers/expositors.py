""" Expositors Serializer """

# Django REST Framework
from rest_framework import serializers

# Models
from eventup.events.models import Expositor


class ExpositorModelSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.CharField(source='pk', read_only=True)

    class Meta:
        model = Expositor
        fields = (
            'id',
            'name',
            'bio',
            'twitter',
            'picture'
        )

    def validate(self, data):
        """Verify rating hasn't been emitted before."""
        # expositor = self.context['request'].expositor
        # if not expositor.exists():
        #     raise serializers.ValidationError('User is not a passenger')
        response = data
        return response

    def create(self, data):
        return Expositor.objects.create(**data)

    def update(self, instance, validated_data):
        user_validated_data = validated_data.pop('user', None)

        user = instance.user
        user.username = user_validated_data.get('username', user.username)
        user.email = user_validated_data.get('email', user.email)
        user.first_name = user_validated_data.get('first_name', user.first_name)
        user.last_name = user_validated_data.get('last_name', user.last_name)
        if user_validated_data.get('last_name'):
            user.set_password(user_validated_data.get('last_name'))
        user.save()

        instance.points = validated_data.get('points', instance.points)
        instance.last_login_date = validated_data.get('last_login_date', instance.last_login_date)
        instance.save()
        return instance

