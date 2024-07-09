# -*- coding: utf-8 -*-
# @Time    : 2024/7/9 13:09
# @Author  : YangYin
# @File    : urls.py
# @Software: PyCharm


from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register),
    path('login/', views.login_view),
]