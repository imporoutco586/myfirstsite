import os
import django
from celery import Celery
from django.conf import settings

# 设置系统环境变量，否则在启动celery时会报错
# taskproject 是当前项目名
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()

celery_app = Celery('mysite')
celery_app.config_from_object('django.conf:settings')
celery_app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
