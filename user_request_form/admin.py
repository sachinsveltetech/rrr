from django.contrib import admin
from .models import UserRequestForm,IPPort,RejectionTable,Tsp
# Register your models here.

@admin.register(UserRequestForm)
class UserRequestFormAdmin(admin.ModelAdmin):
    list_display=['id','sys_date','sys_time','target_type','case_ref','case_type','request_to_provide','mobile_number','cell_id','imei','select_tsp','duration_date_from','duration_date_to','duration_time_from','duration_time_to','user']
    
    
@admin.register(IPPort)
class IPPortAdmin(admin.ModelAdmin):
    list_display=['id','ip','port','date_from','date_to','time_from','time_to']
    
@admin.register(RejectionTable)
class RejectionTableAdmin(admin.ModelAdmin):
    list_display=['id','rejection_time','rejection_reason','user_form','reject_by']