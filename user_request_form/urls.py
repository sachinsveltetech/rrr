from django.urls import path,include
from .import views
from rest_framework.routers import DefaultRouter
# router=DefaultRouter()
# router.register('userrequestform',views.UserRequestFormViewset,basename='userrequestform')
# router.register('ip_port',views.IPPortSerializerViewset,basename='ip_port')
# router.register('tsp',views.TspSerializerViewset,basename='tsp')
urlpatterns =[
    path('userform/',views.UserRequestFormView.as_view()),
    path('userform/<int:pk>/',views.UserRequestFormView.as_view()),
    path('tsp/',views.TspCreateView.as_view()),        
    path('tsp/<int:pk>/',views.TspCreateView.as_view()),
    path('tsp/replies/',views.TspRequestReplieView.as_view()),
    path('cyberdrome/',views.CyberdromeView.as_view()),
    path('cyberdrome/<int:pk>/',views.CyberdromeView.as_view()),
    path('tspresponse/',views.TspResponseView.as_view()),    
    path('tspresponse/<int:pk>',views.TspResponseView.as_view()),
]