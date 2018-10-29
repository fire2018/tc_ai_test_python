import hashlib
import base64
import random
import time
import requests
from urllib import parse


class LicensePlateDistinguish(object):
    def __init__(self, app_id, app_key):
        """
        车牌识别
        :param app_id: Appid  (Str)
        :param app_key: Appkey  (Str)
        """
        # 设置请求地址
        self.request_url = "https://api.ai.qq.com/fcgi-bin/ocr/ocr_plateocr"
        self.me_data = {
            "app_id": app_id,
            "app_key": app_key
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

    # 计算note_str
    @staticmethod
    def calculate_nonce_str():
        examples = "fa577ce340859f9fe"
        note_str = ""
        data = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789"
        for i in range(len(examples)):
            note_str += data[random.randint(0, len(data) - 1)]
        return note_str

    # 将图片弄成Base64编码传输
    @staticmethod
    def calculate_img_base64(img_path):
        img = open(img_path, "rb")
        ls = base64.b64encode(img.read())
        ls = str(ls, encoding="utf-8")
        img.close()
        return ls

    def start(self, img_path=None, image_url=None):
        """
        2选一,如果都挺默认选择图片的网络路径
        :param img_path:图片的本地路径  (Str)
        :param image_url:图片的网络路径  (Str)
        :return:json数据
        """
        request_AI_LicensePlateDistinguish = {
            "app_id": self.me_data["app_id"],
            "time_stamp": self.calculate_time_stamp(),
            "nonce_str": self.calculate_nonce_str()
        }
        if img_path is not None or image_url is not None:

            if img_path is not None:
                request_AI_LicensePlateDistinguish["image"] = self.calculate_img_base64(img_path)
                request_AI_LicensePlateDistinguish["sign"] = self.calculate_sign(request_AI_LicensePlateDistinguish,
                                                                                 self.me_data["app_key"])
                req_data = sorted(request_AI_LicensePlateDistinguish.items())
                response = requests.post(self.request_url, req_data)
                return response.text

            if image_url is not None:
                request_AI_LicensePlateDistinguish["image_url"] = image_url
                request_AI_LicensePlateDistinguish["sign"] = self.calculate_sign(request_AI_LicensePlateDistinguish,
                                                                                 self.me_data["app_key"])
                req_data = sorted(request_AI_LicensePlateDistinguish.items())
                response = requests.post(self.request_url, req_data)
                return response.text
        else:
            return "最少传入一个参数"
