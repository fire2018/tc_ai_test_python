import time
import random
import requests
import hashlib
from urllib import parse


class Synonym(object):
    def __init__(self, ids, keys):
        """
        基础文本分析_同义词
        :param app_id: Appid  (Str)
        :param app_key: Appkey  (Str)
        """
        self.request_url = "https://api.ai.qq.com/fcgi-bin/nlp/nlp_wordsyn"
        self.me_data = {
            "app_id": ids,
            "app_key": keys
        }

    @staticmethod
    def calculate_time_stamp():
        stamp = time.time()
        return int(stamp)

    @staticmethod
    def calculate_nonce_str():
        examples = "fa577ce340859f9fe"
        nonce_str = ""
        data = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789"
        for i in range(len(examples)):
            nonce_str = data[random.randint(0, len(data) - 1)]
        return nonce_str

    def calculate_sign(self, req_dict, app_key):
        sort_list = sorted(req_dict.items())
        url_data = parse.urlencode(sort_list)
        url_data = url_data + "&" + "app_key" + "=" + app_key
        url_data = self.calculate_md5(url_data).upper()
        return url_data

    @staticmethod
    def calculate_md5(url_data):
        me_md5 = hashlib.md5()
        me_md5.update(url_data.encode("utf-8"))
        final = me_md5.hexdigest()
        return final

    def start(self, string):
        request_AI_Synonym = {
            "app_id": self.me_data["app_id"],
            "time_stamp": self.calculate_time_stamp(),
            "nonce_str": self.calculate_nonce_str(),
            "text": string.encode("gbk")
        }
        request_AI_Synonym["sign"] = self.calculate_sign(request_AI_Synonym, self.me_data["app_key"])
        request_data = sorted(request_AI_Synonym.items())
        response = requests.post(self.request_url, request_data)
        response.encoding = "gbk"
        return response.text





