from django.urls import path, include
from rest_framework import routers
from .api import AppUserViewSet

router = routers.DefaultRouter()
router.register('api/users', AppUserViewSet, 'user')

urlpatterns = [
    path('', include(router.urls)),
]
