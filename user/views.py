from django.shortcuts import render
from rest_framework import viewsets ,renderers, status
from .models import User
from .serializers import UserSerializer
from .permissions import IsOwnerOrAdmin
from rest_framework_simplejwt.views import TokenObtainPairView , TokenRefreshView
from .utils import success_response , error_validation
from drf_spectacular.utils import extend_schema, OpenApiResponse, OpenApiExample


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
    
    @extend_schema(
        responses={
        status.HTTP_200_OK: OpenApiResponse(
            response=UserSerializer,
            description='User Retrieved Successfully',
            examples=[
                OpenApiExample(
                    'Success Example',
                    value={
                        'statusCode': status.HTTP_201_CREATED,
                        'message': 'User Retrieved Successfully',
                        'data': {
                            'id': 1,
                            'username': 'johndoe',
                            'email': 'john@example.com'
                            # ... other fields from UserSerializer
                        }
                    },
                    status_codes=['200'],
                    ) 
                ])
            }
    )
    def retrieve(self, request, *args, **kwargs):
        user = self.get_object()
        serializer = self.get_serializer(user , many=False)
        return success_response(
            statusCode=status.HTTP_200_OK ,
            message="User Retrueved Successfully",
            data=serializer.data
        )
    

    @extend_schema(
      request=UserSerializer,
      responses={
        status.HTTP_201_CREATED: OpenApiResponse(
            response=UserSerializer,
            description='User Created Successfully',
            examples=[
                OpenApiExample(
                    'Success Example',
                    value={
                        'statusCode': status.HTTP_201_CREATED,
                        'message': 'User Created Successfully',
                        'data': {
                            'id': 1,
                            'username': 'johndoe',
                            'email': 'john@example.com'
                            # ... other fields from UserSerializer
                        }
                    },
                    status_codes=['201'],
                    ) 
                ]),
        status.HTTP_400_BAD_REQUEST: OpenApiResponse(
            response={
                'statusCode': status.HTTP_400_BAD_REQUEST,
                'message': 'Couldnt Create User',
                'data': []
            },
            description='Could not Create User',
            examples=[
                OpenApiExample(
                    'Error Example',
                    value={
                        'statusCode': status.HTTP_400_BAD_REQUEST,
                        'message': 'Couldnt Create User',
                        'data': [
                            {
                                'field': 'username',
                                'message': 'This field is required.'
                            },
                            {
                                'field': 'email',
                                'message': 'Enter a valid email address.'
                            }
                        ]
                    },
                    status_codes=['400'],
                )]
        ) }
    )
    def create(self, request, *args, **kwargs):
        """method that handles the post request to create user
        """
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer=serializer)
            return success_response(statusCode=status.HTTP_201_CREATED,
                                    message='User Created Successfully',
                                    data= serializer.data
                                    )
        else :
            return error_validation(serializer=serializer ,
                                    message= "Couldnt Create User",
                                    statusCode=status.HTTP_400_BAD_REQUEST
                                    )
        
    @extend_schema(
     request=UserSerializer,
      responses={
        status.HTTP_200_OK: OpenApiResponse(
            response=UserSerializer,
            description='User Created Successfully',
            examples=[
                OpenApiExample(
                    'Success Example',
                    value={
                        'statusCode': status.HTTP_200_OK,
                        'message': 'User Updated Successfully',
                        'data': {
                            'id': 1,
                            'username': 'johndoe',
                            'email': 'john@example.com'
                            # ... other fields from UserSerializer
                        }
                    },
                    status_codes=['200'],
                    ) 
                ]),
        status.HTTP_400_BAD_REQUEST: OpenApiResponse(
            response={
                'statusCode': status.HTTP_400_BAD_REQUEST,
                'message': 'Couldnt Update User',
                'data': []
            },
            description='Could not Update User',
            examples=[
                OpenApiExample(
                    'Error Example',
                    value={
                        'statusCode': status.HTTP_400_BAD_REQUEST,
                        'message': 'Couldnt Create User',
                        'data': [
                            {
                                'field': 'username',
                                'message': 'This field is required.'
                            },
                            {
                                'field': 'email',
                                'message': 'Enter a valid email address.'
                            }
                        ]
                    },
                    status_codes=['400'],
                )]
        ) } 
    )
    def update(self, request, *args, **kwargs):
        user = self.get_object()
        serializer = self.get_serializer(user , request.data, partial=True)
        if serializer.is_valid():
            self.perform_create(serializer=serializer)
            return success_response(statusCode=status.HTTP_200_OK ,
                                    message="User Updated Successfully",
                                    data = serializer.data
                                    )
        else :
            return error_validation(serializer , message="Couldnt Update User", statusCode=status.HTTP_400_BAD_REQUEST)

    
class TokenObtainView(TokenObtainPairView):
    renderer_classes = [renderers.JSONRenderer]

class TokenRefresh(TokenObtainPairView):
    renderer_classes = [renderers.JSONRenderer]
