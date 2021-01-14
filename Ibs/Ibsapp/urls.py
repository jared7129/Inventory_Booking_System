from rest_framework import routers
from Ibsapp import views
from django.urls import path,include,re_path
from  Ibsapp.views import *

# app_name ='Ibsapp'

urlpatterns = [
    path('inventory/',api_inventory_list_view,name='inventory-objects'),
    path('member/',api_member_list_view,name='member-objects'),
    path('booking/',api_booking_list_view,name='booking-objects'),
    path('booking_details/<pk>',booking_details, name='booking-details')
]
