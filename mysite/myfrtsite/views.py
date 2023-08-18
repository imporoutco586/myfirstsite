from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse 
from .models import *
import hashlib
from django.contrib import messages
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
            user = SiteUser.objects.get(name=username)
        except SiteUser.DoesNotExist:
            messages.error(request, '用户不存在')
            return render(request, 'login/login.html')

        if user.password == password:
            request.session['is_login']=True
            request.session['user_id']=user.id
            request.session['user_name']=user.name
            
            context = {'user':user,'username': user.name,'id':user.id}
            return render(request,"login/index.html",context=context)
      # 登录成功
        else:
            messages.error(request, '密码错误')
            return render(request, 'login/login.html')

    else:
        return render(request, 'login/login.html')





    #     try:
    #         user=SiteUser.objects.get(name=username)
    #         if user.password==password:
    #             request.session['is_login']=Truereturn render(request,"login/profile.html")
    #             request.session['user_name']=user.name
    #             context = {'user':user,'username': user.name,'id':user.id}
    #             return render(request,"login/index.html",context=context)
    #         else:
    #             messages.error(request, '密码错误!')
    #             return render(request, 'login.html')
    #     except:
    #         return HttpResponse("用户不存在")
    # else:
    #     return render(request,"login/login.html")
    
def register(request):
    return render(request,"register.html")

def logout(request):
    if request.session.get('is_login'):
        request.session.flush()

    context = {'user': None}
    return render(request,'login/index.html', context=context)  


def dprofile(request):
    id = request.session['user_id']
    print('id:',id)
    name=request.session['user_name']
    user= SiteUser.objects.get(id=id)
    print('dpo:',user.name)
    return render(request,'login/profile.html', {'user':user})  


def save_data(request):
    md5 = hashlib.md5()
    username = request.POST.get("username")
    email = request.POST.get('email')  # 初始化默认值
    password = request.POST.get("password")
    # md5.update(request.POST.get("password").encode("utf-8"))
    # password = md5.hexdigest()
    try:
        SiteUser.objects.get(name=username)
        return HttpResponse("用户名已存在！")
    except:
        SiteUser.objects.create(
            name=username,  email=email, password=password)
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


def sum(request):
    records = SumTask.objects.order_by('-timestamp')
    context = {"record_list":records}
    return render(request, "tasklist/sum.html", context=context)


def runsum(request):
    if request.method=="POST":
        x=request.POST.get('x')
        y=request.POST.get('y')
    else:
        x=request.GET.get('x')
        y=request.GET.get('y')
    answer = tasks.sum.delay(int(x),int(y))
    content= {'200': 'success！'}
    answer = answer.get()
    record = SumTask(x=x, y=y, result=answer)
    record.save()
    print(1)
    if SumTask.objects.count() >= 10:
        earliest = SumTask.objects.earliest('timestamp')  
        earliest.delete()
 
    
    return render(request, "tasklist/runsum.html", context={"record": record})
enctype="multipart/form-data" 
import os

def workflow(request):
    return render(request, "tasklist/workflow.html")


def runworkflow(request):
    result = tasks.runworkflow()
    print('1',result)
    return render(request, "tasklist/runworkflow.html", context={"result": result})


def workflowui(request):
    return redirect('http://127.0.0.1:8080/namespaces/default/workflows')



def home(request):
    if request.session.get('is_login',False) != True:
        return redirect("/login/")
    else:
        user_list = SiteUser.objects.all()
        print(user_list)
        context = {"user_list": user_list}
        return render(request, "home.html", context=context)
        

    
def detail(request, id):
    user = SiteUser.objects.get(id=id)
    print(user)
    return render(request, "detail.html", context={"user": user})


def task_list(request):
    if request.session.get('is_login',False) != True:
        return redirect("/login/")
    else:
        return render(request, 'tasklist/tasklist.html')
    

def upload(request):
    return render(request, "tasklist/upload.html")



def upload_file(request):
    if request.method == "POST":    # 请求方法为POST时，进行处理
        myFile =request.FILES.get("myfile", None)    # 获取上传的文件，如果没有文件，则默认为None
        if not myFile:
            return HttpResponse("no files for upload!")
        destination = open(os.path.join("/home/zfym/Desktop/myfirstsite/mysite/myfrtsite/testfile",myFile.name),'wb+')    # 打开特定的文件进行二进制的写操作
        for chunk in myFile.chunks():      # 分块写入文件
            destination.write(chunk)
        destination.close()
        return HttpResponse("upload over!")
    
def run_file(request):
    if request.method == "POST":    # 请求方法为POST时，进行处理
        file = request.POST.get("file")
    else:
        file=request.GET.get('file')
    
    print(file)
    result = tasks.runfile(file)
    print('1',result)
        
    return render(request, "tasklist/runworkflow.html", context={"result": result})




from django.contrib.auth.decorators import login_required


def profile_edit(request):
   
    # 如果为post请求，则获取表单数据
    if request.method == 'POST':
        # 获取当前登录用户才能修改信息
        id = request.session.get('user_id')

        u = SiteUser.objects.get(id=id)
        data = request.POST
        # print(request.FILES)
        avatar = request.FILES.get('avatar')
        # print(avater)
        name = data.get("username")
        email = data.get("email")
        phone = data.get('phone')
        intro = data.get('intro')
        # address = data.get('address')
        # cate = data.get('cate')
        # detail = data.get('detail')
        # 判断用户修改信息时，有没有上传新图片
        # 上传了换头像链接 否则不换
        # 无该判断时，若用户未更换图片，则原图片链接会被赋空值，导致头像丢失
        if avatar:
            u.avatar = avatar
        u.name = name
        u.email = email
        u.phone = phone
        # u.address = address
        # u.cate = cate
        u.intro = intro
        # 可能抛出异常：
        # 如果该用户修改的昵称已存在数据库中，会报错
        # 原因是，在我的设置里。用户名称是惟一的，不可重复的
        # 因此，避免bug，且提供给用户弹窗警告
        try:
            # 如果未获取当前用户，save会新建一个没有密码的用户，操作是错误的
            u.save()
        except:

            messages.error(request, '用户名重复')
            return render(request, 'login/profile.html', {'user': SiteUser.objects.get(id=id)})
        # 和查看用户信息同理，每个用户都有自己的路由，修改后，重定向到新的路由
        # 因为该路由由用户名决定
        context = {'user':u,'username': u.name,'id':u.id}
        return render(request,"login/index.html",context=context)
    else:
        id = request.session.get('user_id')
        user = SiteUser.objects.get(id=id)
        return render(request, 'login/profile.html', {'user': user})