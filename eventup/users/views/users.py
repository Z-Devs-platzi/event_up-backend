"""Users views."""

# Django REST Framework
from rest_framework import status, viewsets
from rest_framework.decorators import action

# Serializers
from eventup.users.serializers import (
    UserLoginSerializer,
    UserModelSerializer,
    UserSignUpSerializer,
    AccountVerificationSerializer
)

from eventup.utils.interface.responses import CustomActions


class UserViewSet(viewsets.GenericViewSet):
    """User view set.

    Handle sign up, login and account verification
    """

    # customActions = CustomActions()

    # users/login
    @action(detail=False, methods=['post'])
    def login(self, request):
        """Handle HTTP POST request."""
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user, token = serializer.save()
        data = {
            'user': UserModelSerializer(user).data,
            'authToken': token
        }
        return CustomActions().custom_response(status.HTTP_200_OK, True, 'Login Success', data)

    # users/signup
    @action(detail=False, methods=['post'])
    def signup(self, request):
        """Handle HTTP POST request."""
        # Make Serializer and Set Data
        serializer = UserSignUpSerializer(data=request.data)
        # Validate Model
        serializer.is_valid(raise_exception=True)
        # Save Object
        user = serializer.save()
        # Return User
        email = UserModelSerializer(user).data.get('email')
        # Get Status
        return CustomActions().custom_response(status.HTTP_201_CREATED, True, 'Singup Success', {"email": email})

    @action(detail=False, methods=['get'])
    def verify(self, request, *args, **kwargs):
        """Handle HTTP GET request."""
        message = 'Not found data'
        status_custom = False
        token = request.query_params.get('token')
        if token:
            serializer = AccountVerificationSerializer(data={'token': token})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            status_custom = True
            message = 'Congratulation, now go share some rides!'
        return CustomActions().custom_response(status.HTTP_200_OK, status_custom, message)
