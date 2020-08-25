"""Users URLs."""

# Django
from django.urls import include, path

# Django Rest framework
from rest_framework.routers import DefaultRouter

# Views
from eventup.users.views import users as user_views

router = DefaultRouter()
router.register(r'users', user_views.UserViewSet, basename='users')
# router.register(r'users/verify/<str:code>/', user_views.UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
