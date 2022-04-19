from rest_framework import serializers
from.models import UserRequestForm,IPPort,Tsp
from account.models import User

class IPPortSerializer(serializers.ModelSerializer):
    class Meta:
        model=IPPort
        fields=('ip','port')
        
class TspSerializer(serializers.ModelSerializer):
    class Meta:
        model=Tsp
        fields='__all__'

class UserRequestFormSerializer(serializers.ModelSerializer):
    ip_port = IPPortSerializer(many=True)
    #ip_port.set()
    # ip_port = serializers.StringRelatedField(many=True,read_only=True)    
    class Meta:
        model=UserRequestForm
        fields='__all__'
        # fields=['id','case_ref','case_type','tsp','requset_type','target_type','duration_from_date','duration_to_date','duration_from_time','duration_to_time','requested_date','replied_date','form_status','reject_msg']
        read_only_fields=['user']
        
    def create(self, validate_data):
        user=UserRequestForm.objects.create(**validate_data)
        # ip_port=
        return user