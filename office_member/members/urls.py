from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('members/', views.members, name='members'),                     #members is function that is called in views.py
     path('members/details/<int:id>', views.details, name='details'),
    
]