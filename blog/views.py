from django.shortcuts import render
from .models import Blog
from rest_framework import viewsets, permissions
from .serializers import BlogSerializers

# Create your views here.
class BlogViewsets(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializers

    def get_permissions(self):

        permissions_classes = self.permission_classes

        match self.action:
            case 'create':
                permissions_classes = [permissions.IsAuthenticated]
        
        return (permission() for permission in permissions_classes)