# from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
# from yaml import serialize
# from yaml import serialize
# from yaml import serialize
from .models import State,District
from .serializers import StateSerializer,DistrictSerializer
# Create your views here.

class StateView(APIView):   
    queryset=State.objects.all()
    serializer=StateSerializer
    def get(self,request,pk=None,format=None):
        id=pk
        if id is not None:
            state=State.objects.get(id=id)
            serializer=StateSerializer(state)
            return Response(serializer.data,status=status.HTTP_200_OK)
        state=State.objects.all()
        serializer=StateSerializer(state,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def post(self,request,format=None):
        data=request.data
        serializer=StateSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            data=serializer.data
            return Response({'detail':'congratulation state has been created successfullly..now party','created_state':data},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
    def put(self,request,pk=None,format=None):
            data=request.data
            id=pk
            if id is not None:
                state=State.objects.get(id=id)
                serializer=StateSerializer(state,data=data)
                if serializer.is_valid(raise_exception=True):
                    serializer.save()
                    data=serializer.data
                    return Response({'detail':'congratulation you state has been updated successfully...party tho banti h','updated_state':data},status=status.HTTP_201_CREATED)
                return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
            return Response({'detail':'Bhai bina id ka kaam nhi hoga..id do..'})
    
    def patch(self,request,pk=None,format=None):
            data=request.data
            id=pk
            if id is not None:
                state=State.objects.get(id=id)
                serializer=StateSerializer(state,data=data,partial=True)
                if serializer.is_valid(raise_exception=True):
                    serializer.save()
                    data=serializer.data
                    return Response({'detail':'congratulation you state has been updated successfully...party tho banti h','updated_state':data},status=status.HTTP_201_CREATED)
                return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
            return Response({'detail':'Bhai bina id ka kaam nhi hoga..id do..'})
        
    def delete(self,request,pk=None,format=None):
        id=pk
        if id is not None:
            state=State.objects.get(id=id)
            state.delete()
            return Response({'detail':'State has been deleted successfully'},status=status.HTTP_200_OK)
        return Response({'detail':'Bhai bina id ka kaam nhi hoga..id do..'})
    
    
class DistrictView(APIView):
    queryset=District.objects.all()
    serializer=DistrictSerializer
    def get(self,request,pk=None,format=None):
        id=pk
        if id is not None:
            district=District.objects.get(id=id)
            serializer=DistrictSerializer(district)
            return Response(serializer.data,status=status.HTTP_200_OK)
        district=District.objects.all()
        serializer=DistrictSerializer(district,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def post(self,request,format=None):
        data=request.data
        serializer=DistrictSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            data=serializer.data
            return Response({'detail':'District has been saved successfully..','created_district':data},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def put(self,request,pk=None,format=None):
        data=request.data
        id=pk
        if id is not None:
            district=District.objects.get(id=id)
            serializer=DistrictSerializer(district,data=data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                data=serializer.data
                return Response({'detail':'District has been updated successfully..','updated_district':data},status=status.HTTP_201_CREATED)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        return Response({'detail':'id is mandatory for performing update operation'})
    
    def patch(self,request,pk=None,format=None):
        data=request.data
        id=pk
        if id is not None:
            district=District.objects.get(id=id)
            serializer=DistrictSerializer(district,data=data,partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                data=serializer.data
                return Response({'detail':'District has been updated successfully..','updated_district':data},status=status.HTTP_201_CREATED)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        return Response({'detail':'id is mandatory for performing update operation'})
        
    
    def delete(self,request,pk=None,format=None):
        id=pk
        if id is not None:
            district=District.objects.get(id=id)
            district.delete()
            return Response({'detail':'district deleted successfully..'},status=status.HTTP_200_OK)
        return Response({'detail':'id is mandatory for delete operation'},status=status.HTTP_400_BAD_REQUEST)