# -*- coding: utf-8 -*-
# @Time    : 2024/7/14 16:53
# @Author  : YangYin
# @File    : ViewsBase.py
# @Software: PyCharm
import json
import pdb

import django.conf

from utils.ZLMediaKit import ZLMediaKit
from utils.Djangosql import DjangoSql
# from django.conf import settings
debug = False
if debug:
    import importlib
    spec = importlib.util.spec_from_file_location("np_test",r'..\..\..\myAIbe\settings.py')
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    settings = module
    django.conf.settings.configure(settings)
    print(settings.CONFIGOBJ)

base_mdeia = ZLMediaKit(settings.CONFIGOBJ)

base_djangoSql = DjangoSql()
base_behaviors = base_djangoSql.select("select * from av_behavior")
# print(base_behaviors)


