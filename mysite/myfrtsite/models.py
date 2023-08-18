from django.db import models

# Create your models here.
class Article(models.Model):
    title=models.CharField(max_length=50) #字符串类型字段
    content=models.TextField()



# 用户信息表
class SiteUser(models.Model):
    id = models.AutoField(primary_key=True,unique=True)
    gender_choice=(
        (0,"未知"),
        (1,"男"),
        (2,"女"),
    )
    "用户的数据库模型，注册登录需要"
    name=models.CharField(max_length=128,unique=True,verbose_name="用户名")
    ## unique=True，名字唯一
    password=models.CharField(max_length=256,verbose_name="密码")
    email=models.EmailField(verbose_name="电子邮箱",unique=False)
    phone=models.EmailField(max_length=20,verbose_name="phone",blank=True)
    gender=models.IntegerField(choices=gender_choice,default=0,verbose_name="性别")
    # auto_now_add=True为添加时间，更新对象时不会有变化
    create_time=models.DateTimeField(auto_now_add=True,verbose_name="创建时间")
    modify_time=models.DateTimeField(auto_now=True,verbose_name="最后一次修改的时间")
    avatar = models.ImageField(upload_to='user_avatars/', blank=True, verbose_name='头像')
    # null针对数据库层面，blank针对表单的
    last_login_time=models.DateTimeField(null=True,blank=True,verbose_name="最后一次登陆的时间")
    intro = models.TextField(max_length=500, blank=True, verbose_name='个人简介')
    def __str__(self):
        return self.name
    class Meta:
        verbose_name="网站用户管理"
        verbose_name_plural=verbose_name

class SumTask(models.Model):
    x = models.IntegerField()
    y = models.IntegerField() 
    result = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)