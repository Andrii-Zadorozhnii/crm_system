from django.contrib import admin
from django.urls import path
from .views import client_list, add_client

urlpatterns = [
    path('',client_list,name='client_list'),
    path('add_client/',add_client, name='add_client'),
]
