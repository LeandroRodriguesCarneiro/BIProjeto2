from django.urls import path
from . import views

urlpatterns = [
    path('data_load/', views.data_load, name= 'load'),
    path('data_delete/', views.data_delete, name= 'delete'),
    
]