from rest_framework import serializers
from.models import UserRequestForm,IPPort,Tsp
from account.models import User
import json


class IPPortSerializer(serializers.ModelSerializer):
    ip_port_id = serializers.IntegerField(source='id', required=False)    
    class Meta:
        model=IPPort
        fields=('ip_port_id','ip','port')
        
class TspSerializer(serializers.ModelSerializer):
    class Meta:
        model=Tsp
        fields='__all__'

class UserRequestFormSerializer(serializers.ModelSerializer):
    ip_port = IPPortSerializer(many=True)    
    # ip_port = serializers.StringRelatedField(many=True,read_only=True)    
    class Meta:
        model=UserRequestForm
        fields='__all__'
        # fields=['id','case_ref','case_type','tsp','requset_type','target_type','duration_from_date','duration_to_date','duration_from_time','duration_to_time','requested_date','replied_date','form_status','reject_msg']
        read_only_fields=['user']
        
    def create(self, validated_data):
        ipport=validated_data.pop('ip_port')
        user=UserRequestForm.objects.create(**validated_data)
        if ipport:
            ls=[]
            for i in ipport:
                ls.append(IPPort.objects.create(**i))
            user.ip_port.set(ls)            
        return user
    
    def update(self,instance,validate_data):
        request = self.context.get('request')
        print(instance.form_status)
        print(request.data.get('form_status'))
        # if instance.form_status == 'reject' and request.data.get('form_status',"") !='success':
        #     validate_data['form_status'] = 'pending'
        if instance.form_status == 'REJECT':
            validate_data['form_status']='PENDING'
        
        # ip port update
        ip_port = validate_data.pop('ip_port',[])
                
        for ip_obj in ip_port:
            if ip_obj.get('id', None):
                instance.ip_port.filter(id=ip_obj['id']).update(**ip_obj)
            else:
                instance.ip_port.add(IPPort.objects.create(**ip_obj))
        
        
            
        # if not validate_data.get('file',None) or not validate_data.get('file'):
        #     validate_data['file']=instance.file
        return super().update(instance, validate_data)
        
        # instance.save()
        # return instance
        
class UserRequestReplieSerializer(serializers.ModelSerializer):
    class Meta:
        model=UserRequestForm
        fields=['id','requested_date','case_ref','case_type','select_tsp','request_to_provide','duration_date_from','duration_date_to','duration_time_from','duration_time_to','target_type','replied_date','form_status','reject_msg']