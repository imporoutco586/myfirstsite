"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from myfrtsite import views
from django.urls import re_path as url
from myfrtsite.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('myfrtsite/article_detail/<int:article_id>', views.article_detail,name="article_detail"),
    path('', include('myfrtsite.urls')),
    # url(r'^register', register),
    url(r'^save_data/', save_data),

    path('task/',include('myfrtsite.urls'))
   
   
]