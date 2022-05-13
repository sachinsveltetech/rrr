from django.http import QueryDict
from django.shortcuts import render
from django.contrib.auth import authenticate
# from html5lib import serialize

from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView

from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
# from yaml import serialize
# from yaml import serialize

from account.serializers import (UserChangePasswordSerializer, UserLoginSerializer,
                                 UserRegistrationSerializer,UserSerializer)
from account.renderers import UserRenderer
from account.permissions import AdminRegistrationPermission
from user_request_form.models import UserRequestForm
from account.models import User
from rest_framework import permissions

from user_request_form.serializers import UserRequestFormSerializer


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh_token': str(refresh),
        'access_token': str(refresh.access_token),
    }


class UserRegistrationView(GenericAPIView):
    renderer_classes=[UserRenderer]
    permission_classes=[AdminRegistrationPermission,]
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
    
    def post(self,request,format=None):
        data=request.data        
        serializer=UserRegistrationSerializer(data=data)        
        if serializer.is_valid(raise_exception=True):            
            user=serializer.save()            
            return Response({'msg':'Registration successfully'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class UserLoginView(GenericAPIView):
    renderer_classes=[UserRenderer] 
    queryset = User.objects.all()
    serializer_class = UserLoginSerializer 
    permission_classes = [permissions.AllowAny]
      
    def post(self,request,format=None):
        data=request.data
        serializer=UserLoginSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            username=serializer.data.get('username')
            password=serializer.data.get('password')
            user=authenticate(username=username,password=password)
            if user is not None:
                user_data = UserSerializer(user).data
                user_data['token'] =token=get_tokens_for_user(user) 
                return Response({'data':user_data,'msg':'Login Successfully'},status=status.HTTP_200_OK)
            else:
                return Response({'errors':{'non_field_errors':['Username or Password is not valid']}},status=status.HTTP_400_BAD_REQUEST)
            
        
class UserChangePasswordView(GenericAPIView):   
    
    serializer_class = UserChangePasswordSerializer
    
    def post(self,request,format=None):
        data=request.data
        serializer=UserChangePasswordSerializer(data=data,context={'user':request.user})
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'msg':'Password Changed successfully'},status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
  
   
class UserList(GenericAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer
    
    def get_queryset(self):
        query = {}
        if user_type:= self.request.query_params.get('user_type', None):
            query['type'] = user_type
        return self.queryset.filter(**query)
    
    def get(self,request,format=None):  
        serializer=self.get_serializer(self.get_queryset(),many=True)      
        return Response(serializer.data,status=status.HTTP_200_OK)
    