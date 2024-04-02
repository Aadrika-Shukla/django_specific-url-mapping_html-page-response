from django.urls import path
from food.views import *
app_name='pp'
urlpatterns=[
    path('panipuri/',panipuri,name='panipuri'),
]