"""Users URLs."""

# Django
from django.urls import include, path

# Django Rest framework
from rest_framework.routers import DefaultRouter

# Views
from eventup.events.views import expositors as expositors_views

router = DefaultRouter()
router.register(r'expositor', expositors_views.ExpositorViewSet, basename='expositor')
# router.register(r'users/verify/<str:code>/', user_views.UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
