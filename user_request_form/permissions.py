from rest_framework.permissions import BasePermission,SAFE_METHODS

class UserPermissions(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            user_type=request.user.type
            print(user_type)
            if user_type == 'ADMIN' or user_type == 'TSP':
                allowed_method=['GET','PATCH',]
                if request.method in allowed_method:
                    return True
                else:
                    return False
            else:
                return True
        return False
            
        # return super().has_permission(request, view)