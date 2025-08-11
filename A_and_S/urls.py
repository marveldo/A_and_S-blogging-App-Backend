"""
URL configuration for A_and_S project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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



from django.contrib import admin
from django.urls import path
from drf_spectacular.views import SpectacularSwaggerView, SpectacularAPIView
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework import status, renderers


class Hello(GenericAPIView):
    renderer_classes = [renderers.JSONRenderer]
    def get(self , request , *args , **kwargs):
        data = {'message': "Hello World"}
        return Response(data, status=status.HTTP_200_OK)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path("docs/", SpectacularSwaggerView.as_view(), name='swagger-ui'),
    path('', Hello.as_view() )
]


