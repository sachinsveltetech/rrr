from asyncio import streams
import io
from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserRequestFormSerializer,TspSerializer,IPPortSerializer
from .models import UserRequestForm,Tsp,IPPort

# from r2dashboard.user_request_form import serializers


        
class UserRequestFormView(APIView):
    def get(self,request,pk=None,format=None):
        data=request.data
        id=pk
        if id is not None:
            user=UserRequestForm.objects.get(id=id)
            serializer=UserRequestFormSerializer(user)
            return Response(serializer.data,status=status.HTTP_200_OK)
        user=UserRequestForm.objects.all()
        serializer=UserRequestFormSerializer(user,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
        
    def post(self,request,format=None):
        data=request.data
        #save_ip_port(request.body)
        #stream = io.BytesIO(request.data)
        py_data = request.data
        s1 = IPPort()
        s1.ip = int(py_data['ip_port']["ip"])
        s1.port = int(py_data["ip_port"]['port'])
        s1.save()
        serializer=UserRequestFormSerializer(data=data)
        # breakpoint()
        if serializer.is_valid(raise_exception=True):
            #breakpoint()
            serializer.save()
            print(serializer.data)
            return Response({'msg':'User Request Form created successfully'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)