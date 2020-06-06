#login App url file
from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('',views.home,name='login-home'),
   # path('', include(login.url))
]
