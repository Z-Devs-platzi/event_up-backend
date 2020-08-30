"""Community URLs."""

# Django
from django.urls import include, path

# Django Rest framework
from rest_framework.routers import DefaultRouter

# Views
from eventup.communities.views import community as community_views


router = DefaultRouter()
router.register(r'community', community_views.CommunityViewSet, basename='community')

# router.register(r'users/verify/<str:code>/', user_views.UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
