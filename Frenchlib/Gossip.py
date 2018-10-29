# - * - coding:utf-8 - * -
import hashlib
import random
import requests
import time
from urllib import parse


class Gossip(object):
    def __init__(self, ids, keys):
        # 接口请求地址
        self.request_url = "https://api.ai.qq.com/fcgi-bin/nlp/nlp_textchat"

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

    # 计算MD5数据值
    @staticmethod
    def calculate_md5(url_data):
        me_md5 = hashlib.md5()
        me_md5.update(url_data.encode("utf-8"))
        secure = me_md5.hexdigest()
        return secure

    # 计算session
    @staticmethod
    def calculate_session():
        session = random.randint(10000, 99999)
        return str(session)

    # 计算秒级时间时间戳
    @staticmethod
    def calculate_time_stamp():
        stamp = time.time()
        return int(stamp)

    # 应用主方法
    def start(self, string):
        #'''
        request_AI_Gossip = {
            "app_id": self.me_data["app_id"],
            "time_stamp": self.calculate_time_stamp(),
            "nonce_str": self.calculate_nonce_str(),
            "session": self.calculate_session(),
            "question": string
        }
        #'''
        '''
        request_AI_Gossip = {
            "app_id": self.me_data["app_id"],
            "time_stamp": "2109086611",
            "nonce_str": "2109086611",
            "session": "2109086611",
            "question": "2109086611"
        }
        '''
        request_AI_Gossip["sign"] = self.calculate_sign(request_AI_Gossip, self.me_data["app_key"])
        print(request_AI_Gossip["sign"])
        req_data = sorted(request_AI_Gossip.items())
        response = requests.post(self.request_url, req_data)
        return response.text