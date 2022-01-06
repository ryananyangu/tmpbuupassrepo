from django.contrib import admin
from django.contrib.auth.models import Permission
from .models import (
    Role,
    User
)


@admin.register(Permission)
class PermissionAdmin(admin.ModelAdmin):
    empty_value_display = '-empty-'
    list_display = ('name', 'content_type', 'codename',)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    empty_value_display = '-empty-'
    list_display = ('username', 'email', 'first_name', 'last_name',
                    'date_joined', 'is_active', 'is_superuser', 'last_login',)


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    empty_value_display = '-empty-'
    list_display = ('name', 'admin', 'created_at',
                    'created_by', 'modified_at', 'modified_by',) 
