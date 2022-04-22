from django.contrib.auth.backends import BaseBackend
from django.conf import settings
from django.contrib.auth.hashers import check_password
from django.contrib.auth import get_user_model

User=get_user_model()

class PhoneAuthenticationBackend(BaseBackend):
    def authenticate(self, request,username=None,password=None):
        try:
            user=User.objects.get(phone=username)
        except User.DoesNotExist:
            return None
        return user if user.check_password(password) else None
        
    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
        