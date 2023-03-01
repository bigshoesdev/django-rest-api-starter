from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('api.urls')),
    url(r'^api/login/$', TokenObtainPairView.as_view(), name='login'),
    url(r'^api/refresh/$', TokenRefreshView.as_view(), name='token_refresh'),
]
