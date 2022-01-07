# Create your views here.


from .models import User, Role
from .serializers import RegisterSerializer
from rest_framework import generics, permissions
from rest_framework.views import APIView

from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework import status
from django.db import transaction

from django.contrib.auth.models import Permission
from rest_framework.decorators import api_view, authentication_classes


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = RegisterSerializer


#  get all permisions in a role, add permission to a role, remove permission from a role
class RolePermissionsView(APIView):

    permission_classes = (permissions.IsAuthenticated,)
    renderer_classes = [JSONRenderer, ]

    # Only Super admin can add permissions to a role
    # As permissions are system defined at the moment
    # permission_id,role_id
    #  Admins can also export permissions from other roles they have to their admin roles
    @transaction.atomic
    def post(self, request):
        role = Role.objects.get(id=request.data.role_id)
        if not request.user.is_superuser or request.user.id != role.admin:
            resp = {
                "message": "Please contact your system administrator for this operation"}
            return Response(data=resp, status=status.HTTP_401_UNAUTHORIZED)
        permission = Permission.objects.get(id=request.data.permission_id)
        role.permissions.add(permission)
        role.save()
        resp = {"message": "Permission "+permission.name +
                " added to role "+role.name+" successfully"}
        return Response(data=resp, status=status.HTTP_201_OK)

    def get(self, request):
        if not request.user.is_superuser:
            resp = {
                "message": "Please contact your system administrator for this operation"}
            return Response(data=resp, status=status.HTTP_401_UNAUTHORIZED)
        resp = Permission.objects.all().values("name", "id")
        return Response(data=resp, status=status.HTTP_201_OK)

    # Only superadmin can handle this operation

    # 2 path variables required i.e. role_id and permission
    def delete(self, request, role_id, permission_id):
        if not request.user.is_superuser:
            resp = {
                "message": "Please contact your system administrator for this operation"}
            return Response(data=resp, status=status.HTTP_401_UNAUTHORIZED)
        role = Role.objects.get(id=role_id)
        perm = Permission.objects.get(id=permission_id)
        role.permissions.remove(perm)
        resp = {
            "message" : "Permission "+perm.name + "removed from role "+role.name+"."
        }
        return Response(data=resp, status=status.HTTP_204_NO_CONTENT) 

#  Gets all persmissions that a user has (Both normal and super admin).


class UserPermissionsView(APIView):

    permission_classes = (permissions.IsAuthenticated,)
    renderer_classes = [JSONRenderer, ]

    def get(self, request):
        resp = request.user.roles.all().values('id', 'name', 'admin_id__username',
                                               'permissions__name', 'permissions__id',)
        return Response(data=resp, status=status.HTTP_200_OK)


# Add roles to a user, Get all roles of a user, remove a user from a role.
class UserRolesView(APIView):

    permission_classes = (permissions.IsAuthenticated,)
    renderer_classes = [JSONRenderer, ]

    @transaction.atomic
    def post(self, request):
        # userid, roleid, check if poster is the admin of the role
        logged_in_user = request.user
        role = Role.objects.get(id=request.data["role_id"])
        print(request.data)
        if logged_in_user.id != role.admin.id:
            resp = {"message": "User "+logged_in_user.username +
                    " not authorized to perform this action on role "+role.name}
            return Response(data=resp, status=status.HTTP_401_UNAUTHORIZED)

        user = User.objects.get(id=request.data["user_id"])
        user.roles.add(role)
        user.save()
        resp = {"message": "user "+user.username +
                " added to role "+role.name+" successfully"}
        return Response(data=resp, status=status.HTTP_200_OK)

    def get(self, request):
        resp = request.user.roles.all().values('id', 'name', 'admin_id__username',
                                               'created_at', 'created_by__username', 'modified_at', 'modified_by__username')
        return Response(data=resp, status=status.HTTP_200_OK)

    @transaction.atomic
    def delete(self, request, role_id):
        role = Role.objects.get(id=role_id)
        request.user.roles.remove(role)
        resp = {
            "message" : "Role "+role.name + "removed from user "+request.user.username+" profile."
        }
        return Response(data=resp, status=status.HTTP_204_NO_CONTENT)

@authentication_classes(permissions.IsAuthenticated,)
@api_view(['GET'])
def get_permissions_per_role(request, role_id):
    resp =  Role.objects.get(id=role_id).values('permissions__name', 'permissions__id')
    return Response(data=resp,status=status.HTTP_200_OK)
