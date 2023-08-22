from django.contrib import admin
from django.urls import path,include
from django.urls import re_path as url
from myfrtsite import views
from myfrtsite.views import *
from django.urls import path
from django.urls import path,re_path
from django.views.static import serve
from mysite import settings


urlpatterns = [
    path('index/', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
    path('task', views.runtask),
    path('runscheduletask', views.runscheduletask),
    url(r'^home', home),
    url(r'^detail/(\d)+', detail),
    path('tasklist/', views.task_list, name='task_list'),
    path('tasklist/sum/', views.sum, name='sum'),
    path('sum/',views.sum,name='sum'),
    url(r'^runsum/', runsum),
    path('workflow/',views.workflow,name='workflow'),
    url('upload/',views.upload,name='upload'),
    url('profile/',views.profile_edit,name='profile'),
    re_path(r'media/(?P<path>.*)$',serve,{'document_root':settings.MEDIA_ROOT}),
    url(r'^runworkflow/', runworkflow),
    url(r'^runworkflow5/', runworkflow5),
    url(r'^runworker1/', runworker1),
    url(r'^workflowui/', workflowui),
    url(r'uploadFile/',upload_file),
    url(r'runfile/',run_file),
    url(r'^dprofile/', dprofile)
]

