from rest_framework import serializers
from api.models import AppUser


class AppUserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)
    password = serializers.CharField(write_only=True, required=False)
    created_at = serializers.DateTimeField(read_only=True)
    deleted_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = AppUser
        fields = ("id", "email", "username", "password", "info", "created_at", "deleted_at")
