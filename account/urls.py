from django.urls import path
from .import views
urlpatterns = [
    path('register/',views.UserRegistrationView.as_view()),
    path('login/',views.UserLoginView.as_view()),
        
    path('changepassword/',views.UserChangePasswordView.as_view()),#must be login to change its password      
    path('reset-password-email/',views.SendResetPasswordEmailView.as_view()),#this is for getting uid and token(with email)
    path('resetpassword/<uid>/<token>/',views.UserpasswordResetView.as_view()),#this is for reseting password(with email)  
       
    path('userview/',views.UserList.as_view()),    
    path('cybsearch/',views.CyberdomeSearchView.as_view()),    
]