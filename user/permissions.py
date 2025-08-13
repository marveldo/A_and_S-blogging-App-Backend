from rest_framework.permissions import BasePermission
from rest_framework.request import Request
from .models import Role

class IsOwnerOrAdmin(BasePermission) :
    """Permission class forthe user model viewset
    """

    def has_permission(self, request : Request, view):
        """Function that handles the permission logic
        """
        lookup_field = getattr(view , 'lookup_field', 'pk')
        query_param = view.kwargs.get(lookup_field)
       
       
        return request.user and (str(request.user.id) == str(query_param) or request.user.role == Role.admin)