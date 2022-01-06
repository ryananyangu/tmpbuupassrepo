from django.db import models
from django.contrib.auth.models import(
    Group,
    AbstractUser,
    Permission,
)
from django.conf import settings

# Create your models here.


class Role(Group):
    class Meta:
        db_table = 'Role'
        managed = True
        verbose_name = 'Role'
        verbose_name_plural = 'Roles'

    admin = models.ForeignKey(settings.AUTH_USER_MODEL,
                              related_name='+', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name="+")
    modified_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name="+")


class User(AbstractUser):

    class Meta:
        db_table = 'User'
        managed = True
        verbose_name = 'User'
        verbose_name_plural = 'Users'
    roles = models.ManyToManyField(Role, related_name='+',blank=False)
    user_permissions = models.ManyToManyField(Permission, related_name='+',blank=True)
