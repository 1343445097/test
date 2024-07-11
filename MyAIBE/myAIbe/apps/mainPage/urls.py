# -*- coding: utf-8 -*-
# @Time    : 2024/7/11 21:35
# @Author  : YangYin
# @File    : urls.py
# @Software: PyCharm
from django.urls import path

from .views import *

urlpatterns = [
    path('getIndex', api_getIndex),
]