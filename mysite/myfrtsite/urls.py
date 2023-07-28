from django.contrib import admin
from django.urls import path,include
from django.urls import re_path as url
from myfrtsite import views
from django.urls import path



urlpatterns = [
    path('index/', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
    path('task', views.runtask),
    path('runscheduletask', views.runscheduletask),
    
]

