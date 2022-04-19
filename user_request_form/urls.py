from django.urls import path,include
from .import views
from rest_framework.routers import DefaultRouter
# router=DefaultRouter()
# router.register('userrequestform',views.UserRequestFormViewset,basename='userrequestform')
# router.register('ip_port',views.IPPortSerializerViewset,basename='ip_port')
# router.register('tsp',views.TspSerializerViewset,basename='tsp')
urlpatterns =[
    path('userform/',views.UserRequestFormView.as_view()),
]