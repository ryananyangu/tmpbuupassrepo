# Create your views here.


from .models import User
from .serializers import RegisterSerializer
from rest_framework import generics, permissions


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = RegisterSerializer

    # def post(self, request, *args, **kwargs):
    #     # FIXME: Confirm if registration is done by an authenticated user
    #     return super().post(request, *args, **kwargs)
