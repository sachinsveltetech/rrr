
# from dataclasses import fields
from common.models import State,District
from django.forms import ValidationError
from rest_framework import serializers
from account.models import User,Tsp


class UserRegistrationSerializer(serializers.ModelSerializer):
    password=serializers.CharField(style={'input_type':'password'},write_only=True)
    password2=serializers.CharField(style={'input_type':'password'},write_only=True)
    class Meta:
        model=User
        fields=['username','phone','district','type','password','password2','tsp_company']
        extra_kwargs={
            'password':{'write_only':True}
        }
    # validating password and confirm password while registration
    def validate(self, attrs):
        password=attrs.get('password')
        password2=attrs.get('password2')        
        if password != password2:
            raise serializers.ValidationError('Password and Confirm Password does not match')        
        return attrs
    
    def create(self, validate_data):
        validate_data.pop('password2')
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
    
    

        