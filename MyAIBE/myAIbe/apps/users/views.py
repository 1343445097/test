import pdb

from django.shortcuts import render

from .forms import RegisterForm
from django.http import JsonResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate
# Create your views here.
from apps.utils import token_tool

def register(request):
    if request.method=="POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            print("合格")
            form.save()
            return JsonResponse({"code": 1, "msg": "success"})
        print("不合格")
        return JsonResponse({"code":0,"msg":"校验失败 error:"+str(form.errors)})
    return JsonResponse({"code": 0, "msg": "fail"})

def login_view(request):
    if request.method=="POST":
        #pdb.set_trace()
        form = AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username,password=password)
            if user is not None:
                dic = {"username": username, "password": password}
                token = token_tool.encode(dic)
                return JsonResponse({"code": 1, "msg": "登录成功","data":{"token":token}})
        return JsonResponse({"code": 0, "msg": "登录失败，账号或密码错误"})