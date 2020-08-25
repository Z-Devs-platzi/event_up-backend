"""Users views."""

# Django REST Framework
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView

# Serializers
from eventup.users.serializers import (
    UserLoginSerializer,
    UserModelSerializer,
    UserSignUpSerializer,
    AccountVerificationSerializer
)

# ViewSet
class UserViewSet(viewsets.GenericViewSet):
    """User view set.

    Handle sign up, login and account verification
    """

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
        return Response(data, status=status.HTTP_201_CREATED)

    # users/signup
    @action(detail=False, methods=['post'])
    def signup(self, request):
        """Handle HTTP POST request."""
        serializer = UserSignUpSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        data = UserModelSerializer(user).data
        return Response(data, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=['get'])
    def verify(self, request, *args, **kwargs):
        """Handle HTTP GET request."""
        message = 'Not found data'
        token = request.query_params.get('token')
        if token:
            serializer = AccountVerificationSerializer(data={'token': token})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            message = 'Congratulation, now go share some rides!'
        return Response({'message': message} , status=status.HTTP_200_OK)
