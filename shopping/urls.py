from django.urls import path
from shopping.views import *
app_name='sh'
urlpatterns=[
    path('clothes/',clothes,name='clothes'),
]