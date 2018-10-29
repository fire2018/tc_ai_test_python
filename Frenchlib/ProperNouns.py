import hashlib
import requests
import random
import time
from urllib import parse


class ProperNouns(object):
    def __init__(self, ids, key):
        """
        基础文本分析_专有名词
        :param app_id: Appid  (Str)
        :param app_key: Appkey  (Str)
        """
        self.request_url = "https://api.ai.qq.com/fcgi-bin/nlp/nlp_wordner"
        self.me_data = {
            "app_id": ids,
            "app_key": key
        }

    @staticmethod
    # 计算时间戳
    def calculate_time_stamp():
        stamp = time.time()
        return int(stamp)

    @staticmethod
    # 计算nonce_str
    def calculate_nonce_str():
        examples = "fa577ce340859f9fe"
        nonce_str = ""
        data = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789"
        for i in range(len(examples)):
            nonce_str = data[random.randint(0, len(examples) - 1)]
        return nonce_str

    # 计算sign
    def calculate_sign(self, req_dict, app_keys):
        sort_list = sorted(req_dict.items())
        url_data = parse.urlencode(sort_list)
        url_data = url_data + "&" + "app_key" + "=" + app_keys
        url_data = self.calculate_md5(url_data).upper()
        return url_data

    # 计算md5

    @staticmethod
    def calculate_md5(url_data):
        me_md5 = hashlib.md5()
        me_md5.update(url_data.encode("utf-8"))
        final = me_md5.hexdigest()
        return final

    def start(self, string):
        request_AI_ProperNouns = {
            "app_id": self.me_data["app_id"],
            "time_stamp": self.calculate_time_stamp(),
            "nonce_str": self.calculate_nonce_str(),
            "text": string.encode("gbk")
        }
        request_AI_ProperNouns["sign"] = self.calculate_sign(request_AI_ProperNouns, self.me_data["app_key"])
        request_data = sorted(request_AI_ProperNouns.items())
        response = requests.post(self.request_url, request_data)
        response.encoding = "gbk"
        return response.text
