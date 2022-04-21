from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserRequestFormSerializer,TspSerializer,IPPortSerializer,UserRequestReplieSerializer
from .models import UserRequestForm,Tsp,IPPort
from django.http import Http404




        
class UserRequestFormView(APIView):
    def get_object(self,id):
        try:
            user= UserRequestForm.objects.get(id=id)
        except UserRequestForm.DoesNotExist:
            user= None
        return user    
    
    def get(self,request,pk=None,format=None):
        data=request.data
        id=pk        
        if id is not None:
            user=self.get_object(id=id)
            if user is not None:                
                # user=UserRequestForm.objects.get(id=id)
                serializer=UserRequestFormSerializer(user)
                return Response(serializer.data,status=status.HTTP_200_OK)
            return Response({'detail':'No record found with matched id'},status=status.HTTP_404_NOT_FOUND)
        user=UserRequestForm.objects.all()
        serializer=UserRequestFormSerializer(user,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
        
    def post(self,request,format=None):
        data=request.data   
        serializer=UserRequestFormSerializer(data=data)
        # breakpoint()
        if serializer.is_valid(raise_exception=True):
            # breakpoint()
            serializer.save(user=self.request.user)
            # print(serializer.data)
            sdata=serializer.data
            return Response({'detail':'User Request Form created successfully','created_data':sdata},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def put(self,request,pk=None,format=None):
        data=request.data
        id=pk        
        if id is not None:
            user=self.get_object(id=id)
            if user is not None:                
                user=UserRequestForm.objects.get(id=id)           
                serializer=UserRequestFormSerializer(user,data=data)
                if serializer.is_valid(raise_exception=True):
                    serializer.save(user=self.request.user)
                    sdata=serializer.data
                    return Response({'detail':'User Request Form updated successfully','updated_data':sdata},status=status.HTTP_201_CREATED)
                return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
            return Response({'detail':'No record found with matched id for update'})
        return Response({"detail":"id is required for update operation please provide id"},status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self,request,pk=None,format=None):
        data=request.data
        id=pk        
        if id is not None:
            user=self.get_object(id=id)
            if user is not None:                
                user=UserRequestForm.objects.get(id=id)           
                serializer=UserRequestFormSerializer(user,data=data,partial=True)
                if serializer.is_valid(raise_exception=False):
                    serializer.save(user=self.request.user)
                    sdata=serializer.data
                    return Response({'detail':'User Request Form updated successfully','updated_data':sdata},status=status.HTTP_201_CREATED)
                return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
            return Response({'detail':'No record found with the matched id for Partial update'})
        return Response({'detail':'id is required for patch operation please provide id'},status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self,request,pk=None,format=None):
        data=request.data
        id=pk
        if id is not None:
            user=self.get_object(id=id)
            if user is not None:                
                user=UserRequestForm.objects.get(id=id)
                user.delete()
                return Response({'detail':'User form data has been deleted'},status=status.HTTP_200_OK)
            return Response({'detail':'No record found with matched id for delete operation'},status=status.HTTP_404_NOT_FOUND)
        return Response({'detail':'id is required for delete operation please provide id'},status=status.HTTP_400_BAD_REQUEST)
    
class TspCreateView(APIView):
    def get(self,request,pk=None,form=None):
        data=request.data
        id=pk
        if id is not None:
            tsp=Tsp.objects.get(id=id)
            serializer=TspSerializer(tsp)
            return Response(serializer.data,status=status.HTTP_200_OK)
        tsp=Tsp.objects.all()
        serializer=TspSerializer(tsp,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def post(self,request,form=None):
        data=request.data
        serializer=TspSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'detail':'TSP created successfully'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
class TspRequestReplieView(APIView):
    def get(self,request,format=None):
        user=UserRequestForm.objects.exclude(form_status="PENDING")
        serializer=UserRequestReplieSerializer(user,many=True)
        return Response(serializer.data)
            