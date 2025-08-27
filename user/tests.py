from django.test import TestCase
from rest_framework import status, test
from unittest.mock import patch
from .models import User
import uuid
from django.forms.models import model_to_dict

# Create your tests here.

class TestUser(TestCase):
   
    def setUp(self):
        self.client = test.APIClient()
        self.user =  User(id=uuid.uuid4(),
                                       email = "utibesolomon6@gmail.com",
                                       bio = "I love cheese",
                                       username = "Johnnn"
                                       )
        self.create_parameter =  {
             'username': 'johndoe',
             'email': 'john@example.com',
             'bio' : "I love cheese",
             'password': 'Winner174#',
             'password_1' : "Winner174#",
              
         }
        self.update_parameter = {}
        return super().setUp()
    def test_create_user(self) :
         response = self.client.post('/auth/register/', self.create_parameter)
         self.assertEqual(response.status_code , 201)
         self.assertEqual(response.data['statusCode'], 201)

    
    def test_validation_errors(self) :
        self.create_parameter.pop('username')
        response = self.client.post('/auth/register/', self.create_parameter) 
        self.assertEqual(response.status_code , 400)
    
    @patch('rest_framework.viewsets.ModelViewSet.get_object')
    def test_update_user(self, mock_query) :
        with self.settings(REST_FRAMEWORK={
            'DEFAULT_AUTHENTICATION_CLASSES': [
                'tests.test_auth.MockAuthentication'
            ]
        }):
            self.client.force_authenticate(self.user)
            mock_query.return_value = self.user
            data = {
          "username" : "John Doe"
           }

        response = self.client.put(f'/auth/update/{self.user.id}/', data)
        self.assertEqual(response.status_code, 200)
    
    @patch('user.models.User.objects.get')
    def test_login_user(self, mock_service):
        
        self.user.set_password('Winner174#')
        self.user.save()

        mock_service.return_value = self.user
        
        data = {
            'email' : f'{self.user.email}',
            'password': 'Winner174#'
        }
        
        response = self.client.post('/auth/login/', data)

        self.assertEqual(response.status_code, 200)
    @patch('user.models.User.objects.get')
    def test_authentication_failed(self, mock_service):
        self.user.set_password('Winner174#')
        self.user.save()

        mock_service.return_value = self.user

        data = {
            'email' : f'{self.user.email}',
            'password' : 'Winner174'
        }
        response = self.client.post('/auth/login/', data)

        self.assertEqual(response.status_code, 401)

    @patch('rest_framework.viewsets.ModelViewSet.get_object')
    def test_get_user(self, mock_service):
        mock_service.return_value = self.user

        response = self.client.get(f'/auth/user/{self.user.id}/')

        self.assertEqual(response.status_code, 200)



        

        



    
    
    



     

    
    

    



    
    


    


    
     