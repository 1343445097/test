from django.shortcuts import render
from django.http import HttpRequest,JsonResponse
# Create your views here.
from django.conf import settings
from utils.OSInfo import OSInfo

def api_getIndex(request):
    code = 0
    msg = "error"
    os_info = {}
    try:
        osSystem = OSInfo()
        os_info = osSystem.info()
        code = 1000
        msg = "success"
    except Exception as e:
        msg = str(e)

    res = {
        "code":code,
        "msg":msg,
        "os_info":os_info
    }
    print(os_info)
    return JsonResponse(res)