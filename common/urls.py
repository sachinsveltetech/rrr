from django.urls import path
from .import views

urlpatterns = [
    path('state/',views.StateView.as_view()),
    path('state/<int:pk>/',views.StateView.as_view()),
    path('district/',views.DistrictView.as_view()),
    path('district/<int:pk>/',views.DistrictView.as_view()),
]