from django.shortcuts import render
from rest_framework import viewsets ,renderers
from .models import User
from .serializers import UserSerializer
from .permissions import IsOwnerOrAdmin
from rest_framework_simplejwt.views import TokenObtainPairView , TokenRefreshView



# Create your views here.

class UserViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    renderer_classes = [renderers.JSONRenderer]

    def get_permissions(self):
        """Method that handles getting the django Permissions
        """
        permission_classes = self.permission_classes
        match self.action :
          case 'update':
              permission_classes = [IsOwnerOrAdmin]
          case 'delete' :
              permission_classes = [IsOwnerOrAdmin]
        return (permission() for permission in permission_classes)
    
class TokenObtainView(TokenObtainPairView):
    renderer_classes = [renderers.JSONRenderer]

class TokenRefresh(TokenObtainPairView):
    renderer_classes = [renderers.JSONRenderer]
