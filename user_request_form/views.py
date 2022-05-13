
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from account.utils import ADMIN, TSP
from account import permissions
from user_request_form.utils import APPROVE, IPDR, REJECT, TDR, PENDING
from .serializers import RejectionTableSerializer,  UserRequestFormSerializer,TspSerializer,IPPortSerializer
from .models import RejectionTable, UserRequestForm,Tsp,IPPort
from django.http import Http404
from .permissions import UserPermissions
from rest_framework.permissions import IsAdminUser, AllowAny
from account.permissions import AdminCrudTspPermission
from account.renderers import UserRenderer
from django.db.models import Q
from django_filters import rest_framework as filters
from rest_framework.filters import SearchFilter 
        
        
class UserRequestFormView(GenericAPIView):
    renderer_classes=[UserRenderer]
    permission_classes=[UserPermissions,]
    queryset = UserRequestForm.objects.all()
    serializer_class = UserRequestFormSerializer
    filter_backends = [SearchFilter]
    search_fields = ['request_to_provide']
    # ordering_fields = ['id']
    # filter_backends=[filters.DjangoFilterBackend]
    # filterset_fields=('district__name','request_to_provide',)
    
    def get_object(self,id, queryset=None):
        if queryset is None:
            queryset = self.get_queryset()            
        try:
            user= queryset.get(id=id)           
        except UserRequestForm.DoesNotExist:
            user= None
        return user
        
    def get_queryset(self):
        if self.request.user.is_authenticated:
            query = {}
            
            queryset = self.queryset
            if self.request.user.type == 'USER':
                queryset= self.queryset.filter(user=self.request.user)
            if self.request.user.type == 'TSP':
                queryset= self.queryset.filter(select_tsp__name=self.request.user.tsp_company.name).exclude(request_to_provide__in=[IPDR, TDR], admin_status__in=[REJECT, PENDING])
            if self.request.user.type == 'ADMIN':
                if user := self.request.query_params.get('user', None):
                    query['user__id'] = user
                if decision_taken_by := self.request.query_params.get('decision_taken_by', None):
                    query['decision_taken_by__id'] = decision_taken_by
                if decision_taken_by_type := self.request.query_params.get('decision_taken_by_type', None):
                    query['decision_taken_by__type'] = decision_taken_by_type
                if select_tsp := self.request.query_params.get('select_tsp', None):
                    query['select_tsp__name'] = select_tsp
                
            if request_to_provide := self.request.query_params.get('request_to_provide', None):
                query['request_to_provide'] = request_to_provide
            if district := self.request.query_params.get('district', None):
                query['district__name'] = district
                
            sys_date_from = self.request.query_params.get('sys_date_from', None)
            sys_date_to = self.request.query_params.get('sys_date_to', None)
            if sys_date_from and sys_date_to:
                query['sys_date__range'] = [sys_date_from, sys_date_to]
            return queryset.filter(**query)

    
    def get(self,request,*args, **kwargs):
        serializer=UserRequestFormSerializer(self.queryset ,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def get(self,request,pk=None,format=None):
        queryset = self.get_queryset()
        # print('First:',self.request.user.district)
        id=pk
        if id is not None:
            user=self.get_object(id, queryset)
            # breakpoint()
            if user is not None:                
                # user=UserRequestForm.objects.get(id=id)
                # print(self.request.user.district)
                serializer=UserRequestFormSerializer(user)
                return Response(serializer.data,status=status.HTTP_200_OK)
            return Response({'detail':'No record found with matched id'},status=status.HTTP_404_NOT_FOUND)
        user=queryset
        serializer=UserRequestFormSerializer(user,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def post(self,request,format=None):
        data=request.data   
        serializer=UserRequestFormSerializer(data=data)
        
        if serializer.is_valid(raise_exception=True):
            # breakpoint()
            serializer.save(user=self.request.user)
            # print(serializer.data)
            sdata=serializer.data
            return Response({'detail':'User Request Form created successfully','created_data':sdata},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def put(self,request,pk=None,format=None):
        id=pk        
        if id is not None:
            user=self.get_object(id=id)
            if user is not None:                
                user=UserRequestForm.objects.get(id=id)           
                serializer=UserRequestFormSerializer(user,data=request.data,context={'request':request})
                if serializer.is_valid(raise_exception=True):
                    serializer.save()
                    sdata=serializer.data
                    return Response({'detail':'User Request Form updated successfully','updated_data':sdata},status=status.HTTP_201_CREATED)
                return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
            return Response({'detail':'No record found with matched id for update'})
        return Response({"detail":"id is required for update operation please provide id"},status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self,request,pk=None,format=None):
        id=pk        
        
        if id is not None:
            user=self.get_object(id=id)
            if user is not None:                
                user=UserRequestForm.objects.get(id=id)           
                serializer=UserRequestFormSerializer(user,data=request.data,partial=True,context={'request':request})
                if serializer.is_valid(raise_exception=False):
                    serializer.save()
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
    
class TspCreateView(GenericAPIView):
    
    renderer_classes=[UserRenderer]
    permission_classes=[AdminCrudTspPermission,]
    queryset=Tsp.objects.all()
    serializer_class=TspSerializer
    
    
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

class RejectionTableView(GenericAPIView):
    serializer_class = RejectionTableSerializer
    queryset = RejectionTable.objects.all()
    
    def get(self,request,pk=None,format=None):
        id=pk
        if id is not None:
            rt=RejectionTable.objects.get(id=id)
            serializer=RejectionTableSerializer(rt)
            return Response(serializer.data,status=status.HTTP_200_OK)
        rt=RejectionTable.objects.all()
        serializer=RejectionTableSerializer(rt,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def post(self,request,format=None):
        data=request.data
        serializer=RejectionTableSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            data=serializer.data
            return Response({'detail':'rejection table created successfully','rjection_table_data':data},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
    def put(self,request,pk=None,format=None):
        data=request.data
        id=pk
        if id is not None:
            rt=RejectionTable.objects.get(id=id)
            serializer=RejectionTableSerializer(rt,data=data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                rt_data=serializer.data
                return Response({'detail':'Rejection table updated successfully','updated_rejection_table_data':rt_data},status=status.HTTP_201_CREATED)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        return Response({'detail':'Id is required for update operation'},status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self,request,pk=None,format=None):
        data=request.data
        id=pk
        if id is not None:            
            rt=RejectionTable.objects.get(id=id)
            serializer=RejectionTableSerializer(rt,data=data,partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                rt_data=serializer.data
                return Response({'detail':'Rejection table updated successfully','updated_rejection_table_data':rt_data},status=status.HTTP_201_CREATED)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        return Response({'detail':'Id is required for update operation'},status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk=None,format=None):
        id=pk
        if id is not None:
            rt=RejectionTable.objects.get(id=id)
            rt.delete()
            return Response({'detail':'Rejection table has been deleted successfully'},status=status.HTTP_200_OK)
        return Response({'detail':'id is required for deletion operation'})

