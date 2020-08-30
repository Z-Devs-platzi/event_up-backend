"""Users views."""

# Django REST Framework
from rest_framework import mixins, status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

# Permissions
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated
)
from eventup.users.permissions import IsAccountOwner

# Serializers
from eventup.users.serializers.profiles import ProfileModelSerializer
from eventup.users.serializers import (
    AccountVerificationSerializer,
    UserLoginSerializer,
    UserModelSerializer,
    UserSignUpSerializer
)

# Complements
from eventup.utils.interface.responses import CustomActions

# Models
from eventup.users.models import User


class UserViewSet(mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  viewsets.GenericViewSet):
    """User view set.

    Handle sign up, login and account verification.
    """

    queryset = User.objects.filter(is_active=True, is_client=True)
    serializer_class = UserModelSerializer
    lookup_field = 'username'

    def get_permissions(self):
        """Assign permissions based on action."""
        if self.action in ['signup', 'login', 'verify']:
            permissions = [AllowAny]
        elif self.action in ['retrieve', 'update', 'partial_update', 'profile']:
            permissions = [IsAuthenticated, IsAccountOwner]
        else:
            permissions = [IsAuthenticated]
        return [p() for p in permissions]


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



    @action(detail=True, methods=['put', 'patch'])
    def profile(self, request, *args, **kwargs):
        """Update profile data."""
        user = self.get_object()
        profile = user.profile
        partial = request.method == 'PATCH'
        serializer = ProfileModelSerializer(
            profile,
            data=request.data,
            partial=partial
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        data = UserModelSerializer(user).data
        return Response(data)
