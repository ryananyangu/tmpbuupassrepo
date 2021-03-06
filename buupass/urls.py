"""buupass URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from accessctrl.views import (
    RegisterView, 
    UserRolesView, 
    UserPermissionsView,
    RolePermissionsView,
    get_permissions_per_role
)
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_jwt.views import refresh_jwt_token
from rest_framework_jwt.views import verify_jwt_token

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api-auth/', include('rest_framework.urls')),
    path('api-token-auth/', obtain_jwt_token),
    path('api-token-verify/', verify_jwt_token),
    path('api-token-refresh/', refresh_jwt_token),
    path('register/', RegisterView.as_view(), name='auth_register'),
    path('user/roles/', UserRolesView.as_view(), name='get_post_user_roles'),
    path('user/roles/<int:role_id>/',
         UserRolesView.as_view(), name='delete_user_roles'),
    path('user/permissions/', UserPermissionsView.as_view(),
         name='get_all_user_permissions'),
    path('role/permissions/', RolePermissionsView.as_view(),
         name='get_post_role_permissions'),
    path('role/permissions/<int:role_id>/<int:permission_id>/', RolePermissionsView.as_view(),
         name='delete_role_permissions'),
    path('role/permissions/<int:role_id>/', get_permissions_per_role,
         name='delete_role_permissions'),
]
