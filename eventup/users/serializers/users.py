"""Users serializers."""

# Django
from django.conf import settings
from django.contrib.auth import password_validation, authenticate
from django.core.validators import RegexValidator

# Django REST Framework
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework.validators import UniqueValidator

# Models
from eventup.users.models import Users, Profile

# Tasks
from eventup.taskapp.tasks import send_confirmation_email

# Serializers
from eventup.users.serializers.profiles import ProfileModelSerializer

# Utilities
import jwt


class UserModelSerializer(serializers.ModelSerializer):
    """User model serializer."""
    profile = ProfileModelSerializer(read_only=True)

    class Meta:
        """Meta class."""

        model = Users
        fields = (
            'username',
            'name',
            'email',
            'profile'
        )


class UserSignUpSerializer(serializers.Serializer):
    """User sign up serializer.

    Handle sign up data validation and user/profile creation.
    """
    # Name
    name = serializers.CharField(min_length=2, max_length=30)

    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=Users.objects.all())]
    )

    username = serializers.CharField(
        min_length=4,
        max_length=20,
        validators=[UniqueValidator(queryset=Users.objects.all())]
    )

    # Phone number
    phone_regex = RegexValidator(
        regex=r'\+?1?\d{9,15}$',
        message="Phone number must be entered in the format: +999999999. Up to 15 digits allowed."
    )
    phone_number = serializers.CharField(validators=[phone_regex], max_length=17, required=False)

    # Password
    password = serializers.CharField(min_length=8, max_length=64)

    def validate(self, data):
        """Verify passwords match."""
        password_validation.validate_password(data['password'])
        return data

    def create(self, data):
        """Handle user and profile creation."""
        user = Users.objects.create_user(**data, is_verified=False)
        Profile.objects.create(user=user)
        send_confirmation_email.delay(user_pk=user.pk)
        return user


class UserLoginSerializer(serializers.Serializer):
    """User login serializer.

    Handle the login request data.
    """

    email = serializers.EmailField()
    password = serializers.CharField(min_length=8, max_length=64)

    def validate(self, data):
        """Check credentials."""
        user = authenticate(username=data['email'], password=data['password'])
        if not user:
            raise serializers.ValidationError('Invalid credentials')
        if not user.is_verified:
            raise serializers.ValidationError('Account is not active yet :(')
        self.context['user'] = user
        return data

    def create(self, data):
        """Generate or retrieve new token."""
        token, created = Token.objects.get_or_create(user=self.context['user'])
        return self.context['user'], token.key


class AccountVerificationSerializer(serializers.Serializer):
    """Account verification serializer."""

    token = serializers.CharField()

    def validate_token(self, data):
        """Verify token is valid."""
        print(data, settings.SECRET_KEY)
        try:
            payload = jwt.decode(data, settings.SECRET_KEY, algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise serializers.ValidationError('Verification link has expired.')
        except jwt.PyJWTError:
            raise serializers.ValidationError('Invalid token')
        if payload['type'] != 'email_confirmation':
            raise serializers.ValidationError('Invalid token')

        self.context['payload'] = payload
        return data

    def save(self):
        """Update user's verified status."""
        payload = self.context['payload']
        user = Users.objects.get(username=payload['user'])
        user.is_verified = True
        user.save()
