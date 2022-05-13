from django.urls import path
from .import views
urlpatterns = [
    path('register/',views.UserRegistrationView.as_view()),
    path('login/',views.UserLoginView.as_view()),    
    path('changepassword/',views.UserChangePasswordView.as_view()),    
    # path('userformlist/',views.CyberdomeRegisterTSP.as_view()),    
    # path('districtuserlist/',views.CyberdomeRegisterUSER.as_view()),    
    path('userview/',views.UserList.as_view()),    
]