from django.contrib import admin
from django.urls import path
from .views import client_list, add_client, add_deals

urlpatterns = [
    path('',client_list,name='client_list'),
    path('add_client/',add_client, name='add_client'),
    path('add_deal/',add_deals, name='add_deals'),
]
