from django.contrib import admin
from .models import User

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    """Admin Manager for the User Model

    Args:
        admin (_type_): _description_
    """
    list_display = ['username' , 'email' , 'id' , 'role']
    list_filter = ['email']
    search_fields = ['email']

admin.site.register(User, UserAdmin)

