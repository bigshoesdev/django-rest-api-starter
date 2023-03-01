from rest_framework import viewsets
from .models import AppUser
from django.utils import timezone
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from rest_framework import permissions
from .serializers import AppUserSerializer


# Viewset
class AppUserViewSet(viewsets.ModelViewSet):
    queryset = AppUser.objects.all()
    serializer_class = AppUserSerializer

    def get_permissions(self):
        if self.request.method == 'POST':
            return [permissions.AllowAny()]
        else:
            return super().get_permissions()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = request.data.pop("email")
        username = request.data.pop("username")
        password = request.data.pop("password", "")

        if not password:
            raise ValidationError(detail="password is required")

        new_user = AppUser.objects.create(email=email, username=username, is_active=True, )
        new_user.set_password(password)
        new_user.save(update_fields=['password'])

        return Response(self.get_serializer(new_user).data)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset().filter(deleted_at__isnull=True)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        password = request.data.pop("password", "")
        super().update(request, *args, **kwargs)
        instance = self.get_object()

        if password:
            instance.set_password(password)
            instance.save(update_fields=['password'])

        return Response(self.get_serializer(instance).data)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.deleted_at = timezone.now()
        instance.save(update_fields=['deleted_at'])

        return Response(self.get_serializer(instance).data)
