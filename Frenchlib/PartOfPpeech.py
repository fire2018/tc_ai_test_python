# 作者: Frnech
# 描述: 词性分析
# 时间: 2018年08月17日
# QQ: 1109527533
# 邮箱: 1109527533@hoime.cn
import time
import random
import hashlib
import requests
from urllib import parse


class PartOfPpeech(object):
    # 初始化方法
    def __init__(self, ids, keys):
        """
        基础文本分析_词性
        :param app_id: Appid  (Str)
        :param app_key: Appkey  (Str)
        """
        # 设置请求地址
        self.request_url = "https://api.ai.qq.com/fcgi-bin/nlp/nlp_wordpos"
        # 设置AppID以及AppKey
        self.me_data = {
            "app_id": ids,
            "app_key": keys
        }

    # 计算sign
    def calculate_sign(self, req_dict, app_key):
        # 获取列表化升序字典
        sort_list = sorted(req_dict.items())
        url_data = parse.urlencode(sort_list)
        url_data = url_data + "&" + "app_key" + "=" + app_key
        url_data = self.calculate_md5(url_data).upper()
        return url_data

    # 计算md5
    @staticmethod
    def calculate_md5(url_data):
        me_md5 = hashlib.md5()
        # 拼接数据
        me_md5.update(url_data.encode("utf-8"))
        # 将拼接好的数据转换成MD5
        secure = me_md5.hexdigest()
        return secure

    # 计算秒级时间戳
    @staticmethod
    def calculate_time_stamp():
        stamp = time.time()
        return int(stamp)

    # 计算note_str
    @staticmethod
    def calculate_note_str():
        examples = "fa577ce340859f9fe"
        note_str = ""
        data = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789"
        for i in range(len(examples)):
            note_str += data[random.randint(0, len(data)-1)]
        return note_str

    def start(self, string):
        # 发送请求字典
        request_AI_PartOfPpeech = {
            "app_id": self.me_data["app_id"],
            "time_stamp": self.calculate_time_stamp(),
            "nonce_str": self.calculate_note_str(),
            "text": string.encode("gbk")
        }
        request_AI_PartOfPpeech["sign"] = self.calculate_sign(request_AI_PartOfPpeech, self.me_data["app_key"])
        req_data = sorted(request_AI_PartOfPpeech.items())
        response = requests.post(self.request_url, req_data)
        response.encoding = "gbk"
        return response.text
