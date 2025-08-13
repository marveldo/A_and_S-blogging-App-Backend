from django.urls import path
from .views import UserViewset, TokenObtainView , TokenRefresh


urlpatterns = [
    path('register/', UserViewset.as_view({'post' : 'create'})),
    path('update/<str:pk>/', UserViewset.as_view({'put': 'update'})),
    path('user/<str:pk>/' , UserViewset.as_view({'get':'retrieve'})),
    path('login/', TokenObtainView.as_view()),
    path('refresh/', TokenRefresh.as_view())
]