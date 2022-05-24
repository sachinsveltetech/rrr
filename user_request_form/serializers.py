# from xml.etree.ElementInclude import include
# from attr import validate

# from wsgiref.validate import validator
# from attr import validate
# from pyrsistent import T
from datetime import datetime
from rest_framework import serializers
# from zmq import NULL
from.models import RejectionTable, UserRequestForm,IPPort
from common.models import Tsp
from account.utils import ADMIN, TSP,USER
from account.models import User
import json
# from zmq import NULL
# from account.models import User


class RejectionTableSerializer(serializers.ModelSerializer):
    class Meta:
        model=RejectionTable
        fields='__all__'


class IPPortSerializer(serializers.ModelSerializer):
    ip_port_id = serializers.IntegerField(source='id', required=False)    
    class Meta:
        model=IPPort
        fields='__all__'

        
class TspSerializer(serializers.ModelSerializer):
    class Meta:
        model=Tsp
        fields='__all__'


import json
def validate_ip_port_data(data):
    detail = json.loads(data)
      

class UserRequestFormSerializer(serializers.ModelSerializer):
    ip_port = serializers.CharField(required=False)    
    district=serializers.CharField(source='user.district',read_only=True)
    dist=serializers.CharField(source='user.dist',read_only=True)
    class Meta:
        model=UserRequestForm
        fields='__all__'        
        read_only_fields=['user','district', 'ip_port','dist']
    
    def validate_ip_port(self, data):
        detail = json.loads(data)
  
        for d in detail:
            test = IPPortSerializer(data=d)
            if test.is_valid(raise_exception=True):
                continue
        return data
    
    def to_representation(self, instance):
        data = super().to_representation(instance)
        if instance.form_status == "REJECT":
            data['rejection_data'] = RejectionTableSerializer(instance.rejectiontable_set.last()).data
        if instance.ip_port:
            data['ip_port'] = IPPortSerializer(instance.ip_port, many=True).data
        if instance.user_file:
            data['user_file'] = instance.user_file.url
        return data
    
        
    def create(self, validated_data):
        ipport=json.loads(validated_data.pop('ip_port')) if validated_data.get('ip_port', None) else []
        user=UserRequestForm.objects.create(**validated_data)
        if ipport:
            ls=[]
            for i in ipport:
                ls.append(IPPort.objects.create(**i))
            user.ip_port.set(ls)            
        return user
    
    def update(self,instance,validate_data):
        request = self.context.get('request')        
        
        validate_data['observer_account_type'] = request.user.type        
                
        if request.user.type in [ADMIN,TSP]:
            validate_data['decision_taken_by'] = request.user        
            
        if instance.user.type == 'USER':
            if instance.form_status == 'REJECT':
                validate_data['form_status']= 'PENDING'
                validate_data['admin_status']='PENDING'
                validate_data['reject_msg_admin']=""
                validate_data['reject_msg_tsp']=""      
                validate_data['updated_by_tsp']=""      
                
        if request.user.type == 'TSP':            
                validate_data['updated_by_tsp']=datetime.now()
        
        if validate_data.get('admin_status', None) and validate_data['admin_status'] == 'REJECT':
            validate_data['form_status'] = 'REJECT'        
        
        if not validate_data.get('user_file',None) or not validate_data.get('user_file'):
            validate_data['user_file']=instance.user_file
        
        ip_port = json.loads(validate_data.pop('ip_port')) if validate_data.get('ip_port') else []
        
        for ip_obj in ip_port:
            if ip_obj.get('id', None):
                instance.ip_port.filter(id=ip_obj['id']).update(**ip_obj)
            else:
                instance.ip_port.add(IPPort.objects.create(**ip_obj))
        
        return super().update(instance, validate_data)
 
 
 
        
# class UserRequestReplieSerializer(serializers.ModelSerializer):
    
#     class Meta:
#         model=UserRequestForm
#         fields=['id','requested_date','case_ref','case_type','select_tsp','request_to_provide','duration_date_from','duration_date_to','duration_time_from','duration_time_to','target_type','replied_date','form_status']
        
#     def to_representation(self, instance):
#         data = super().to_representation(instance)
#         if instance.form_status == "REJECT":
#             data['rejection_data'] = RejectionTableSerializer(instance.rejectiontable_set.last()).data