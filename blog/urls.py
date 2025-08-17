
from django.urls import path
from .views import BlogViewsets


urlpatterns = [
    path('', BlogViewsets.as_view({'post' : 'create'})),
    path('<str:pk>/', BlogViewsets.as_view({'put': 'update'})),
    path('<str:pk>/' , BlogViewsets.as_view({'get':'retrieve'})),

]