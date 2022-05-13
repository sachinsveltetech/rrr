from rest_framework.permissions import BasePermission

class AdminRegistrationPermission(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            user_type=request.user.type
            if user_type == 'ADMIN' or user_type == 'SUPER_USER':
                return True
            else:
                return False
        return False
        # return super().has_permission(request, view)
      
    def has_object_permission(self, request, view, obj):
        return super().has_object_permission(request, view, obj)    
class AdminCrudTspPermission(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            user=request.user.type
            if user == 'ADMIN' or user == 'SUPER_USER':
                return True
            else:
                return False
        # return super().has_permission(request, view)
    
        