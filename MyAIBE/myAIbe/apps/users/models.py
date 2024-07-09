from django.db import models

# Create your models here.
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User,AbstractUser
from django.db import models
# class RegisterForm(UserCreationForm)

# class MyUser(AbstractUser):
#
#     mobile = models.CharField(max_length=11,unique=True,verbose_name='手机号')
#
#     class Meta:
#         db_table = 'tb_user'
#         verbose_name = '用户'  #模型在站点显示中文名
#         verbose_name_plural = verbose_name
#
#     def __str__(self):
#         return self.username

class RegisterForm(UserCreationForm):
    # email = forms.EmailField(required=True)
    # name = forms.CharField()
    # age = forms.IntegerField()
    # password1 = forms.CharField()
    # password2 = forms.CharField()
    class Meta:
        model = User
        fields = ["username","email","password1","password2",]
        # db_table = 'myuser'