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

    admin = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='+')


class User(AbstractUser):

    class Meta:
        db_table = 'User'
        managed = True
        verbose_name = 'User'
        verbose_name_plural = 'Users'
    groups = models.ManyToManyField(Role, related_name='+')
    user_permissions = models.ManyToManyField(Permission, related_name='+')


