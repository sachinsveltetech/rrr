# from tkinter import CASCADE
# from typing import Dict
# from distutils.command.upload import upload
from django.db import models
from django.contrib.auth import get_user_model
from common.models import Tsp
from account.utils import ACCOUNT_TYPE
from .validators import mobile_regex_validator,ip_regex_validator
from .utils import TARGET_TYPE, REQUEST_TO_PROVIDE, FORM_STATUS

User = get_user_model() 


class IPPort(models.Model):    
    ip=models.CharField(max_length=200,validators=[ip_regex_validator],blank=True,null=True)
    port=models.IntegerField(blank=True,null=True)
    date_from=models.DateField(blank=True,null=True)
    date_to=models.DateField(blank=True,null=True)
    time_from=models.TimeField(blank=True,null=True)
    time_to=models.TimeField(blank=True,null=True)
    def __str__(self) -> str:
        return f'{self.ip}{self.port}'
        
    

class UserRequestForm(models.Model):
    #All Foreign keys:
    observer_account_type = models.CharField(max_length=200, choices=ACCOUNT_TYPE, blank=True,default='USER')
    decision_taken_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='userrequestform_decision_taken_by',blank=True,null=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    ip_port=models.ManyToManyField(IPPort,blank=True)
    
    #To be filled by system:
    
    updated_at=models.DateTimeField(auto_now=True)
    updated_by_tsp=models.CharField(max_length=200,blank=True,null=True)
    #to be filled by the user:
    sys_date=models.DateField(blank=True,null=True)
    sys_time=models.TimeField(blank=True,null=True)    
    target_type=models.CharField(max_length=200,choices=TARGET_TYPE)
    case_ref=models.CharField(max_length=200)
    case_type=models.CharField(max_length=200)
    request_to_provide=models.CharField(max_length=200,choices=REQUEST_TO_PROVIDE)
    mobile_number=models.BigIntegerField(validators=[mobile_regex_validator])
    cell_id=models.CharField(max_length=200)
    imei=models.CharField(max_length=200)    
    select_tsp=models.ForeignKey(Tsp,on_delete=models.PROTECT)
    duration_date_from=models.DateField()
    duration_date_to=models.DateField()
    duration_time_from=models.TimeField()
    duration_time_to=models.TimeField()
    user_file=models.FileField(upload_to='user_doc',blank=True,null=True)
    
    #to be filled by TSP and CYBERDOME
    form_status=models.CharField(max_length=200,choices=FORM_STATUS,blank=True,null=True,default='PENDING')
    admin_status=models.CharField(max_length=200,choices=FORM_STATUS,blank=True,null=True,default='PENDING')
    
    #for tsp replie
    requested_date=models.DateField(blank=True,null=True)
    replied_date=models.DateField(blank=True,null=True)
    #for cyberdome view
    approval_or_reject_date=models.DateField(blank=True,null=True)
    approval_or_reject_time=models.TimeField(blank=True,null=True)
    
    #For TSP to upload file after approval
    tsp_file=models.FileField(upload_to='tsp_doc',blank=True)
    
    reject_msg_admin=models.CharField(max_length=200,blank=True,null=True)  
    reject_msg_tsp=models.CharField(max_length=200,blank=True,null=True)  
    
    class Meta:
        ordering = ('id',)
        
    def __str__(self):
        return str(self.mobile_number)
        
#For CYBERDOME and TSP after rejection of form       
class RejectionTable(models.Model):
    rejection_time=models.DateTimeField(auto_now_add=True)
    rejection_reason=models.CharField(max_length=500,blank=True,null=True)
    user_form=models.ForeignKey(UserRequestForm,on_delete=models.CASCADE)
    reject_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='rejection_table_rejected_by', null=True, blank=True)
    
    def __str__(self):
        return f'{self.user_form}'
            
