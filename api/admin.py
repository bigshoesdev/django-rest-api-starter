from django.contrib import admin
from .models import AppUser


class AppUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'info', 'created_at', 'deleted_at',)
    readonly_fields = ('password', 'groups', 'user_permissions')


admin.site.register(AppUser, AppUserAdmin)
