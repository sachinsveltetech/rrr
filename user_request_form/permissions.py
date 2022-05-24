from rest_framework.permissions import BasePermission,SAFE_METHODS
from account.utils import USER, ADMIN, TSP


OBJECT_METHODS = ['PUT', 'PATCH', 'DELETE']


class UserPermissions(BasePermission):
    
    def has_permission(self, request, view):
        if not request.user.is_authenticated:            
                return False
        if request.user.type == USER:
            return True
        if request.user.type in [ADMIN, TSP]: 
            if request.method in ['POST', 'DELETE','PUT']:
                return False
            else:
                return True
        
        return False
    
    def has_object_permission(self, request, view, obj):
        # print('putututu')
        if request.user.type == USER:
            return obj.user == request.user
        if request.user.type in [ADMIN, TSP] and request.method != 'DELETE':
            return True
        return False