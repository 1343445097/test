# -*- coding: utf-8 -*-
# @Time    : 2024/7/14 15:41
# @Author  : YangYin
# @File    : ZLMediaKit.py
# @Software: PyCharm

import requests
import inspect

class ZLMediaKit():
    def __init__(self,ConfigObj):
        self.mediaApiHost = ConfigObj["mediaApiHost"]
        self.secrect = "035c73f7-bb6b-4889-a715-d9eb2d1925cc"

        self.mediaHttpHost = ConfigObj["mediaHttpHost"]
        self.mediaRtmpHost = ConfigObj["mediaRtmpHost"]
        self.mediaRtspHost = ConfigObj["mediaRtspHost"]

        self.timeout = 1


    def __byteFormat(self,bytes, suffix="bps"):

        factor = 1024
        for unit in ["", "K", "M", "G"]:
            if bytes < factor:
                return f"{bytes:.2f}{unit}{suffix}"
            bytes /= factor

    def get_flvUrl(self,app,name):

        return "{}/{}/{}.live.flv".format(self.mediaHttpHost,app,name)

    def get_hlsUrl(self, app, name):

        return "%s/%s/%s.hls.m3u8" % (self.mediaHttpHost, app, name)

    def getMediaList(self):
        """获取媒体列表"""
        __data = []
        url = "{host}/index/api/getMediaList?secrect={secrect}".format(
            host = self.mediaApiHost,
            secrect = self.secrect
        )
        res = requests.get(url,timeout = self.timeout)

        res_json = res.json()
        if res_json["code"] == 0:
            data = res_json["data"]
            __data_group = {}  # 视频流按照流名分组
            for d in data:
                app = d.get("app")
                name = d.get("stream")
                schema = d.get("schema")
                code = "{}_{}".format(app,name)

                v = __data_group.get(code)
                if not v:
                    v = {}
                v[schema] = d
                __data_group[code] = v

            print(__data_group.keys())
            for code,v in __data_group.items():
                schemas_clients = []
                index = 0
                d = None
                for __schema,__d in v.items():
                    schemas_clients.append({
                        "schema":__schema,
                        "readerCount":__d.get("readerCount")
                    })
                    if index == 0:
                        d = __d
                    index += 1

                if d:
                    video_str = "无"
                    audio_str = "无"
                    tracks = d.get("tracks",None)
                    if tracks:
                        for track in tracks:
                            codec_id = track.get("codec_id")
                            codec_id_name = track.get("codec_id_name")
                            codec_type = track.get("codec_type", -1)  # Video = 0, Audio = 1
                            ready = track.get("ready")

                            if 0 == codec_type:
                                fps = track.get("fps")
                                height = track.get("height")
                                width = track.get("width")

                                video_str = "%s/%d/%dx%d" % (codec_id_name, fps, width, height)
                            elif 1 == codec_type:
                                channels = track.get("channels")

                                sample_bit = track.get("sample_bit")
                                sample_rate = track.get("sample_rate")

                                audio_str = "%s/%d/%d/%d" % (
                                    codec_id_name, channels, sample_rate, sample_bit)
                    produce_speed = self.__byteFormat(d.get("bytesSpeed"))

                    app = d.get("app")
                    name = d.get("stream")

                    __data.append({
                        "active":True,
                        "code":code,
                        "app":app,
                        "name":name,
                        "produce_speed":produce_speed,
                        "video":video_str,
                        "audio":audio_str,
                        "originUrl":d.get("originUrl"),
                        "originType":d.get("originType"),
                        "clients":d.get("totalReaderCount"), #客户端数量
                        "scheams_clients":schemas_clients,
                        "flvUrl":self.get_flvUrl(app,name),
                        "hlsUrl":self.get_hlsUrl(app,name)

                    })
        return __data
        # print(res.json())

if __name__=='__main__':
    ip = "127.0.0.1"
    ConfigObj = {
        "mediaApiHost": f"http://{ip}:80",
        "mediaHttpHost": f"http://{ip}:80",
        "mediaRtmpHost": f"rtmp://{ip}:1935",
        "mediaRtspHost": f"rtsp://{ip}:554",
        "analyzerApiHost": f"http://{ip}:9002",
    }
    zlm = ZLMediaKit(ConfigObj)
    ans = zlm.getMediaList()
    print(ans)