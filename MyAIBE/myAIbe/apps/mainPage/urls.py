# -*- coding: utf-8 -*-
# @Time    : 2024/7/11 21:35
# @Author  : YangYin
# @File    : urls.py
# @Software: PyCharm
from django.urls import path

from mainPage.views.api import *

urlpatterns = [
    path('behavior', web_behavior), # 数据库中获取算法

    path('getIndex', api_getIndex),  # 获取OS信息
    path('getStreams', api_getStreams),  # 获取视频流

]