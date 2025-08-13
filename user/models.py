from django.db import models
from django.contrib.auth.models import BaseUserManager , AbstractBaseUser , PermissionsMixin
import uuid

# Create your models here.

class UserManager(BaseUserManager):

    """Custom User Model Manager to manage communication with the database
    """

    def create_user(self, email, password=None , **extra_fields):
        """Function to create a user

        Args:
            email (_type_): user email
            password (_type_, optional): user password

        Raises:
            ValueError: field based errors

        Returns:
            _type_: user Instance created
        """
        if not email :
            raise ValueError({'email' : 'Email must be provided'})
        user_email = self.normalize_email(email)
        user : User = self.model(email=user_email , **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    
    def create_superuser(self, email , password=None , **extra_fields):

        """Creates a super user to manage the django Admin Block

        Raises:
            ValueError: field based errors

        Returns:
            _type_: created user model instance
        """
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault("role", Role.admin)
        extra_fields.setdefault('is_staff', True)
        if extra_fields.get('is_superuser') is not True :
            raise ValueError({'is_superuser': 'Must be set to True'})
        if extra_fields.get("role") is not Role.admin :
            raise ValueError({"role": "User role must be admin"})
        if extra_fields.get('is_staff') is not True:
            raise ValueError({"is_staff": "is_staff must be True"})
        
        user : User = self.create_user(email, password , **extra_fields)
      
        return user
    
class Role (models.TextChoices):
    """Enum for model choices

    Args:
        models (_type_): "
    """
    admin = "ADMIN",
    user = "USER"

class User(AbstractBaseUser , PermissionsMixin):
    """User Model 

    Args:
        AbstractBaseUser (_type_): Base User Model Django Provides
        PermissionsMixin (_type_): Group of Permissions A user use on the django admin
    """

    id = models.UUIDField(default=uuid.uuid4, editable=False , primary_key=True , unique=True)
    username = models.CharField(max_length=250, unique=True)
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=250 , choices=Role.choices , default=Role.user)
    bio = models.TextField(null=True , blank=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.email}'
    
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']








