from rest_framework import serializers
from .models import User
import re

class UserSerializer(serializers.ModelSerializer):
    """User Serializer Class
    """
    password_1 = serializers.CharField(
        write_only = True,
        required = False,
        style={'input_type' : 'password'}
    )
    class Meta :
        model = User
        fields = ['id','username', 'password' ,'password_1','email', 'bio', 'role' ]
        extra_kwargs = {
            'email' : {'required': False},
            'username': {'required': False},
            'password': {"write_only" : True, 'required': False},
            'role' : {"read_only" : True}
        }

    def validate(self, attrs):
        """Method that validate the inputed value
        """
        
        if self.instance is None :
            if not attrs.get('username'):
                raise serializers.ValidationError({'username': 'Field is Required'})
            if not attrs.get('password'):
                raise serializers.ValidationError({'password' : 'Field is Required'})
            if not attrs.get('email'):
                raise serializers.ValidationError({'email' : 'Field is Required'})
            
        if 'password' in attrs :
            pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&#])[A-Za-z\d@$!%*?&#]{8,}$'
            if not re.fullmatch(pattern , attrs.get('password')):
                raise serializers.ValidationError({'password' : 'Password must contain at least one capital letter symbol and numbers and one small letter'})
            if 'password_1' not in attrs :
                raise serializers.ValidationError({'password_1' : "Field is Required when setting or changing password"})
            if attrs.get('password') != attrs.get('password_1') :
                raise serializers.ValidationError({'password_1': 'Fields dont match'})
        return super().validate(attrs)
    
   
    
    def create(self, validated_data : dict):
        """Method that gets called on creation endpoint
        """
        password = validated_data.pop('password', None)
        _ = validated_data.pop('password_1', None)
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        return user
    
    def update(self, instance : User, validated_data : dict):
        """Method called when making an update to an existing instance
        """
        password = validated_data.pop('password', None)
        _ = validated_data.pop('password_1', None)
        for name , value in validated_data.items():
            setattr(instance , name , value)
        if password is not None :
            instance.set_password(password)
        instance.save()
        return instance
    

    
        


