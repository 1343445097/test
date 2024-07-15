# -*- coding: utf-8 -*-
# @Time    : 2024/7/14 17:00
# @Author  : YangYin
# @File    : Analyzer.py
# @Software: PyCharm

import json
import requests
import time

#算法分析器
class Analyzer():
    def __int__(self,analyzerHost):
        self.analyzerHost = analyzerHost
