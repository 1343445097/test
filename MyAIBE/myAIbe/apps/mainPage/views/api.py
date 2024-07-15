from django.shortcuts import render
from django.http import HttpRequest,JsonResponse
# Create your views here.
from django.conf import settings
from utils.OSInfo import OSInfo

from mainPage.views.ViewsBase import base_mdeia

def web_behavior(request):
    """获取算法"""
    return JsonResponse({"ok":"True"})

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


def api_getStreams(request):
    code = 0
    msg = "error"
    mediaServerState = False
    data = []
    try:
        streams = base_mdeia.getMediaList()
        mediaServerState = True

        # 将在线视频流按用户分流
        for stream in streams:
            stream_code = stream.get("code")
            stream["ori"] = "推流"
            data.append(stream)

        code = 1000
        msg = "success"
    except Exception as e:
        msg = "服务器内部异常，请检查你的ZLM流媒体服务是否正常启动，端口是否被占用，是否有在线视频流。"

    if mediaServerState:
        serverState = "流媒体服务正常"
    else:
        serverState = "流媒体服务未运行"
    res = {
        "code":code,
        "msg":msg,
        "mediaServerState":mediaServerState,
        "serverState":serverState,
        "data":data
    }
    return JsonResponse(res)