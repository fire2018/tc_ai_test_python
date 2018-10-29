# - * - coding:UTF-8 - * -
import hashlib
import random
import requests
import time
from urllib import parse


class Participle(object):
    # 初始化方法
    def __init__(self, ids, keys):
        """
        基础文本分析_分词
        :param app_id: Appid  (Str)
        :param app_key: Appkey  (Str)
        """
        # 请求接口设置
        self.request_url = "https://api.ai.qq.com/fcgi-bin/nlp/nlp_wordseg"
        # app_id及app_key的设置
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
        me_md5.update(url_data.encode("utf-8"))
        secure = me_md5.hexdigest()
        return secure

    # 计算秒级时间戳
    @staticmethod
    def calculate_time_stamp():
        stamp = time.time()
        return int(stamp)

    # 计算nonce_str
    @staticmethod
    def calculate_nonce_str():
        # 腾讯AI示例数据
        examples = "fa577ce340859f9fe"
        nonce_str = ""
        data = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789"
        for i in range(len(examples)):
            nonce_str += data[random.randint(0, len(data) - 1)]
        return nonce_str

    def start(self, string):
        request_AI_Participle = {
            "app_id": int(self.me_data["app_id"]),
            "time_stamp": self.calculate_time_stamp(),
            "nonce_str": self.calculate_nonce_str(),
            # 设置发送的编码格式必须是GBK
            "text": string.encode("gbk")
        }
        request_AI_Participle["sign"] = self.calculate_sign(request_AI_Participle, self.me_data["app_key"])
        req_data = sorted(request_AI_Participle.items())
        response = requests.post(self.request_url, req_data)
        # 设置解码格式
        response.encoding = "gbk"
        return response.text
