# from tkinter import CASCADE
# from typing import Dict
from distutils.command.upload import upload
from django.db import models
from django.core.validators import RegexValidator
from account.models import User
# Create your models here.

class IPPort(models.Model):
    ip_regex_validator=RegexValidator(regex=r'\b((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)(\.|$)){4}\b',message="Invalid ip address")
    ip=models.CharField(max_length=200,validators=[ip_regex_validator])
    port=models.IntegerField()
    
    

class Tsp(models.Model):
    tsp=models.CharField(max_length=200)
    
    def __str__(self):
        return self.tsp

class UserRequestForm(models.Model):
    mobile_regex_validator=RegexValidator(regex=r"^[6-9]\d{9}$",message="Invalid phone number")
    TARGET_TYPE=(('MOBILE_NUMBER','MOBILE_NUMBER'),('IMEI_NUMBER','IMEI_NUMBER'),('CELL_ID','CELL_ID'),('IP_ADDRESS','IP_ADDRESS'))
    REQUEST_TO_PROVIDE=(('CDR','CDR'),('IPDR','IPDR'),('TOWER_DUMP','TOWER_DUMP'),('SDR','SDR'),('TDR','TDR'))
    FORM_STATUS=(('PENDING','PENDING'),('SUCCESS','SUCCESS'),('REJECT','REJECT'))
    sys_date=models.DateField()
    sys_time=models.TimeField()
    target_type=models.CharField(max_length=200,choices=TARGET_TYPE)
    case_ref=models.CharField(max_length=200)
    case_type=models.CharField(max_length=200)
    request_to_provide=models.CharField(max_length=200,choices=REQUEST_TO_PROVIDE)
    mobile_number=models.BigIntegerField(validators=[mobile_regex_validator])
    cell_id=models.CharField(max_length=200)
    imei=models.CharField(max_length=200)
    date_from=models.DateField(blank=True,null=True)
    date_to=models.DateField(blank=True,null=True)
    time_from=models.TimeField(blank=True,null=True)
    time_to=models.TimeField(blank=True,null=True)
    select_tsp=models.ForeignKey(Tsp,on_delete=models.PROTECT)
    duration_date_from=models.DateField()
    duration_date_to=models.DateField()
    duration_time_from=models.TimeField()
    duration_time_to=models.TimeField()
    file=models.FileField(upload_to='doc',blank=True)
    form_status=models.CharField(max_length=200,choices=FORM_STATUS,blank=True,null=True,default='PENDING')
    reject_msg=models.CharField(max_length=200,blank=True,default='rejected')
    reject_msg_cyberdrome=models.CharField(max_length=200,blank=True,default='Due to incomplete information')
    requested_date=models.DateField(blank=True)
    replied_date=models.DateField(blank=True)
    approval_or_reject_date=models.DateField(blank=True,null=True)
    approval_or_reject_time=models.TimeField(blank=True,null=True)
    tsp_file=models.FileField(upload_to='tsp_doc',blank=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    ip_port=models.ManyToManyField(IPPort)
    
    
    
    class Meta:
        ordering = ('id',)
        
    def __str__(self):
        return str(self.mobile_number)
        