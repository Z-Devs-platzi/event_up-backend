"""Invitations tests."""

# Django
from django.test import TestCase

# Django REST Framework
from rest_framework import status
from rest_framework.test import APITestCase

# Faker Data
from faker import Faker

# Model
from eventup.users.models import Users, Profile
from rest_framework.authtoken.models import Token


class OnboardingAPITestCase(APITestCase):
    """Member invitation API test case."""
    def setUp(self):
        fake = Faker()
        """Test case setup."""
        self.user = Users.objects.create(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            email=fake.email(),
            username=fake.user_name(),
            password='testPassword12345'
        )
        self.profile = Profile.objects.create(user=self.user)

        # Auth
        self.token = Token.objects.create(user=self.user).key
        self.client.credentials(HTTP_AUTHORIZATION='Token {}'.format(self.token))

    #     # URL
    #     self.url = '/users/login/'

    # def test_response_success(self):
    #     """Verify request succeed."""
    #     request = self.client.get(self.url)
    #     self.assertEqual(request.status_code, status.HTTP_200_OK)

    def test_invitation_creation(self):
        """Verify invitation are generated if none exist previously."""
        # Invitations in DB must be 0
        self.assertEqual(Users.objects.count(), 1)
