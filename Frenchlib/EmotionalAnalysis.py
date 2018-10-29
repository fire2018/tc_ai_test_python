# - * - coding:utf-8 - * -
import time
import hashlib
import random
import requests
from urllib import parse


class EmotionalAnalysis(object):
    def __init__(self, ids, keys):
        """
        情感分析
        :param app_id: Appid  (Str)
        :param app_key: Appkey  (Str)
        """
        # 调用的接口地址
        self.request_url = "https://api.ai.qq.com/fcgi-bin/nlp/nlp_textpolar"
        # 设置账号和密匙
        self.me_data = {
            "app_id": ids,
            "app_key": keys
        }

    def calculate_sign(self, req_dict, app_keys):
        # 获取列表化升序字典
        sort_list = sorted(req_dict.items())
        url_data = parse.urlencode(sort_list)
        url_data = url_data + "&" + "app_key" + "=" + app_keys
        url_data = self.calculate_md5(url_data).upper()
        return url_data

    # 计算秒级时间戳
    @staticmethod
    def calculate_time_stamp():
        stamp = time.time()
        return int(stamp)

    # 计算md5
    @staticmethod
    def calculate_md5(url_data):
        me_md5 = hashlib.md5()
        me_md5.update(url_data.encode("utf-8"))
        secure = me_md5.hexdigest()
        return secure

    # 计算note_str
    @staticmethod
    def calculate_note_str():
        examples = "fa577ce340859f9fe"
        note_str = ""
        data = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789"
        for i in range(len(examples)):
            note_str += data[random.randint(0, len(data) - 1)]
        return note_str

    def start(self, string):
        request_AI_EmotionalAnalysis = {
            "app_id": self.me_data["app_id"],
            "time_stamp": self.calculate_time_stamp(),
            "nonce_str": self.calculate_note_str(),
            "text": string
        }
        request_AI_EmotionalAnalysis["sign"] = self.calculate_sign(request_AI_EmotionalAnalysis, self.me_data["app_key"])
        req_data = sorted(request_AI_EmotionalAnalysis.items())
        response = requests.post(self.request_url, req_data)
        return response.text

