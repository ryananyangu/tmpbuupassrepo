# Create your views here.


from .models import User,Role
from .serializers import RegisterSerializer
from rest_framework import generics, permissions
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework import status
from django.db import transaction


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = RegisterSerializer


#  get all permisions in a role, add permission to a role, remove permission from a role 
class RolePermissionsView(APIView):

    permission_classes = (permissions.IsAuthenticated,)
    renderer_classes = [JSONRenderer,]

    def post(self, request):
        pass
    def get(self, request):
        pass
    def delete(self, request):
        pass

#  Gets all persmissions that a user has.
class UserPermissionsView(APIView):

    permission_classes = (permissions.IsAuthenticated,)
    renderer_classes = [JSONRenderer,]

    def get(self, request):
        pass


# Add roles to a user, Get all roles of a user, remove a user from a role.
class UserRolesView(APIView):

    permission_classes = (permissions.IsAuthenticated,)
    renderer_classes = [JSONRenderer,]

    @transaction.atomic
    def post(self,request):
        # userid, roleid, check if poster is the admin of the role
        logged_in_user = request.data.user
        role = Role.objects.get(id=request.data.role_id)
        if logged_in_user.id != role.admin:
            return Response(data={"message" : "User not authorized to perform this action"}, status=status.HTTP_401_UNAUTHORIZED)

        user = User.objects.get(id=request.data.user_id)
        user.roles.add(role)
        user.save()
        return Response(data=role.objects.all().values('id', 'name','admin_id__username','created_at','created_by__username','modified_at','modified_by__username'), status=status.HTTP_201_OK)

    def get(self, request):
        resp = request.user.roles.all().values('id', 'name','admin_id__username','created_at','created_by__username','modified_at','modified_by__username')
        return Response(data=resp, status=status.HTTP_200_OK)

    @transaction.atomic    
    def delete(self, request,role_id):
        role = Role.objects.get(id=role_id)
        request.user.role.remove(role)
        return Response(data=role, status=status.HTTP_204_NO_CONTENT)

# <QuerySet [{'id': 1, 'name': 'rashiruma', 'group_ptr_id': 1, 'admin_id': 1, 'created_at': datetime.datetime(2022, 1, 6, 7, 8, 33, 815437, tzinfo=<UTC>), 'modified_at': datetime.datetime(2022, 1, 6, 7, 8, 33, 832000, tzinfo=<UTC>), 'created_by_id': 1, 'modified_by_id': 1}]>