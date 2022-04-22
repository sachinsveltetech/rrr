from django.shortcuts import render
from django.contrib.auth import authenticate

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken

from account.serializers import UserChangePasswordSerializer, UserLoginSerializer, UserRegistrationSerializer
from account.renderers import UserRenderer
from account.permissions import AdminRegistrationPermission
#generate token manually
def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh_token': str(refresh),
        'access_token': str(refresh.access_token),
    }
class UserRegistrationView(APIView):
    renderer_classes=[UserRenderer]
    permission_classes=[AdminRegistrationPermission,]
    def post(self,request,format=None):
        data=request.data        
        serializer=UserRegistrationSerializer(data=data)        
        if serializer.is_valid(raise_exception=True):            
            user=serializer.save()            
            return Response({'msg':'Registration successfully'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class UserLoginView(APIView):
    renderer_classes=[UserRenderer]    
    def post(self,request,format=None):
        data=request.data
        serializer=UserLoginSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            username=serializer.data.get('username')
            password=serializer.data.get('password')
            user=authenticate(username=username,password=password)
            if user is not None:
                token=get_tokens_for_user(user)
                return Response({'token':token,'msg':'Login Successfully'},status=status.HTTP_200_OK)
            else:
                return Response({'errors':{'non_field_errors':['Username or Password is not valid']}},status=status.HTTP_400_BAD_REQUEST)
            
        
class UserChangePasswordView(APIView):
    def post(self,request,format=None):
        data=request.data
        serializer=UserChangePasswordSerializer(data=data,context={'user':request.user})
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'msg':'Password Changed successfully'},status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        