from django.contrib import admin
from .models import Tsp,State,District


# Register your models here.
# @admin.register(Tsp)
# class TspAdmin(admin.ModelAdmin):
#     list_display=['id','tsp']

admin.site.register(Tsp)

admin.site.register(State)

admin.site.register(District)