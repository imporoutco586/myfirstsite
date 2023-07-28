from django.shortcuts import render,redirect
from django.http import HttpResponse 
from .models import SiteUser
import hashlib

from . import models

# Create your views here.

def article_detail(request,article_id):
    try:
        article=models.Article.objects.get(pk=article_id)  #获取pk=1，2，3的文章
        # 需要将获取的对象存成字典的形式，即context
        context={}
        context['article_obj']=article
         # html文件识别字典对象，将数据展示到前端页面
        return render(request,"articleDetail.html" , context) 
    except:
        return HttpResponse("没有这篇文章")
    


def index(request):
    pass
    return render(request,"login/index.html")

def login(request):
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        try:
            user=SiteUser.objects.get(name=username)
            if user.password==password:
                request.session['is_login']=True
                request.session['user_id']=user.id
                request.session['user_name']=user.name
                return redirect("/index/")
            else:
                return HttpResponse("密码错误")
        except:
            return HttpResponse("用户不存在")
    else:
        return render(request,"login/login.html")
    
def register(request):
    return render(request,"register.html")

def logout(request):
    if request.session.get('is_login'):
        request.session.flush()
    return redirect('/login/')



def save_data(request):
    md5 = hashlib.md5()
    username = request.POST.get("username")
    phoneNum = ""  # 初始化默认值
    password = request.POST.get("password")
    # md5.update(request.POST.get("password").encode("utf-8"))
    # password = md5.hexdigest()
    try:
        SiteUser.objects.get(name=username)
        return HttpResponse("用户名已存在！")
    except:
        SiteUser.objects.create(
            name=username,  password=password)
    return HttpResponse("数据保存成功！")



from django.http import JsonResponse
from . import tasks
# Create your views here.


def runtask(request):
    x=request.GET.get('x')
    tasks.task1.delay(x)
    content= {'200': 'run task1 success!---'+str(x)}
    return JsonResponse(content)


def runscheduletask(request):
    tasks.scheduletask1.delay()
    content= {'200': 'success！'}
    return JsonResponse(content)

def runsum(request):
    x=request.GET.get('x')
    y=request.GET.get('y')
    tasks.sum.delay(x,y)
    content= {'200': 'success！'}
    return JsonResponse(content)