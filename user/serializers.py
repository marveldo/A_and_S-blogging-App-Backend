from rest_framework import serializers
from .models import User


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
        fields = ['username', 'password' ,'password_1' 'email', 'bio', 'role' ]
        extra_kwargs = {
            'password': {'write_only':True},
              'role': {'read_only': True},
              '*':{'required': False}
              }
    
    def validate(self, attrs : dict):
        """Validation method to validate serializer Fields
        """
        for key in attrs.items():
            if not self.instance and not attrs.get(f'{key}'):
                raise serializers.ValidationError({f'{key}' : 'Field is Required'})
        if attrs['password'] != attrs['password_1']:
            raise serializers.ValidationError({'password_1': "Passwords dont Match"})
        
       
        return super().validate(attrs)
    
    def create(self, validated_data : dict):
        """Method that gets called on creation endpoint
        """
        password = validated_data.pop('password', None)
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        return user
    
    def update(self, instance : User , validated_data : dict):
        """Method that gets called on Updates
        """
        password = validated_data.pop('password', None)
        for name , value in validated_data.items():
            setattr(instance, name , value)
        if password is not None :
            instance.set_password(password)
        instance.save()
        return instance
        
    

