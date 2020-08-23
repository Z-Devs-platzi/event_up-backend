"""Users URLs."""

# Django
from django.urls import path

# Views
from eventup.users.views import (
    UserLoginAPIView,
    UserSignUpAPIView,
    AccountVerificationAPIView
)

urlpatterns = [
    path('users/login/', UserLoginAPIView.as_view(), name='login'),
    path('users/signup/', UserSignUpAPIView.as_view(), name='signup'),
    path('users/verify/<str:code>', AccountVerificationAPIView.as_view(), name='verify'),
]
