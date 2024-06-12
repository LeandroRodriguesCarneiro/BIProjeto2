from django.urls import path
from . import views

urlpatterns = [
    path('data_load/', views.data_load, name= 'load'),
]