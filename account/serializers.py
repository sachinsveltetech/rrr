
# from dataclasses import fields
# from unittest.util import _MAX_LENGTH
from common.models import State,District
from django.forms import ValidationError
from rest_framework import serializers
from account.models import User,Tsp
from account.utils import Util

from django.utils.encoding import smart_str,force_bytes,DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode,urlsafe_base64_encode
from django.contrib.auth.tokens import PasswordResetTokenGenerator

class UserRegistrationSerializer(serializers.ModelSerializer):
    password=serializers.CharField(style={'input_type':'password'},write_only=True)
    # password2=serializers.CharField(style={'input_type':'password'},write_only=True)
    class Meta:
        model=User
        fields=['username','phone','district','type','password','tsp_company', 'email','state','dist']
        extra_kwargs={
            'password':{'write_only':True}
        }
    # validating password and confirm password while registration
    # def validate(self, attrs):
    #     password=attrs.get('password')
    #     password2=attrs.get('password2')        
    #     if password != password2:
    #         raise serializers.ValidationError('Password and Confirm Password does not match')        
    #     return attrs
    
    def create(self, validate_data):
        # validate_data.pop('password2')
        return User.objects.create_user(**validate_data)
    
class UserLoginSerializer(serializers.ModelSerializer):
    username=serializers.CharField(max_length=255)
    class Meta:
        model=User
        fields=['username','password']
        
class UserChangePasswordSerializer(serializers.Serializer):
    password=serializers.CharField(style={'input_type':'password'},write_only=True)
    password2=serializers.CharField(style={'input_type':'password'},write_only=True)
    class Meta:
        fields=['password','password2']
    
    def validate(self, attrs):
        password=attrs.get('password')
        password2=attrs.get('password2')
        user=self.context.get('user')
        if password != password2:
            raise ValidationError('Password and Confirm Password does not match')
        user.set_password(password)
        user.save()
        return attrs
    def create(self, validated_data):
        validated_data.pop('password2')
        
        return User.objects.create(**validated_data)
    
    
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields='__all__'
        
        
        
class ResetPasswordEmailSerializer(serializers.Serializer):
    email=serializers.EmailField(max_length=200)
    class Meta:
        fields=['email']
        
    def validate(self, attrs):
        email=attrs.get('email')
        if User.objects.filter(email=email).exists():
            user=User.objects.get(email = email)
            uid=urlsafe_base64_encode(force_bytes(user.id))
            print('Encoded UID',uid)
            token=PasswordResetTokenGenerator().make_token(user)
            print('Password Reset Token',token)
            link='http://localhost:3000/api/account/reset/'+uid+'/'+token+'/'
            print('Password Reset Link',link)
            #send email
            body='Click this link to reset your password '+link
            data={
                'subject':'Reset your password',
                'body':body,
                'to_email':user.email
            }
            Util.send_email(data)
            return attrs
        else:
            raise ValidationError('You are not registered User')
        
class UserPasswordResetSerializer(serializers.Serializer):
    password=serializers.CharField(style={'input_type':'password'},write_only=True)
    password2=serializers.CharField(style={'input_type':'password'},write_only=True)
    class Meta:
        fields=['password','password2']
    
    def validate(self, attrs):
        try:            
            password=attrs.get('password')
            password2=attrs.get('password2')
            uid=self.context.get('uid')
            token=self.context.get('token')
            if password != password2:
                raise ValidationError('Password and Confirm Password does not match')
            id=smart_str(urlsafe_base64_decode(uid))
            user=User.objects.get(id=id)
            if not PasswordResetTokenGenerator().check_token(user,token):
                raise ValidationError('Token is not valid or expired')
            user.set_password(password)
            user.save()
            return attrs
        except DjangoUnicodeDecodeError as identifier:
            PasswordResetTokenGenerator().check_token(user,token)
            raise ValidationError('Token is not valid or expired')