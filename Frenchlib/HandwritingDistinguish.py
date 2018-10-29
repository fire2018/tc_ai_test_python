import time
import random
import base64
import hashlib
import requests
from urllib import parse


class HandwritingDistinguish(object):
    def __init__(self, app_id, app_key):
        """
        手写体识别
        :param app_id: Appid  (Str)
        :param app_key:  Appkey  (Str)
        """
        self.request_url = "https://api.ai.qq.com/fcgi-bin/ocr/ocr_handwritingocr"
        self.me_data = {
            "app_id": app_id,
            "app_key": app_key
        }

    # 计算time_stamp
    @staticmethod
    def calculate_time_stamp():
        stamp = time.time()
        return int(stamp)

    # 计算 nonce_str
    @staticmethod
    def calculate_nonce_str():
        examples = "fa577ce340859f9fe"
        nonce_str = ""
        data = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789"
        for i in range(len(examples)):
            nonce_str = data[random.randint(0, len(examples) - 1)]
        return nonce_str

    # 计算图片的base64位值
    @staticmethod
    def calculate_image_base64(image_path):
        image = open(image_path, "rb")
        image_base = base64.b64encode(image.read())
        image_base = str(image_base, encoding="utf-8")
        return image_base

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

    def start(self, img_path=None, image_url=None):
        """
        任选一个参数传入,也可以两个都传入，如果两个都传入,默认选择图片的网络路径
        :param img_path:图片的本地路径  (Str)
        :param image_url:图片的网络路径  (Str)
        :return:json数据
        """
        request_AI_HandwritingDistinguish = {
            "app_id": self.me_data["app_id"],
            "time_stamp": self.calculate_time_stamp(),
            "nonce_str": self.calculate_nonce_str()
        }
        if img_path is not None or image_url is not None:

            if img_path is not None:
                request_AI_HandwritingDistinguish["image"] = self.calculate_image_base64(img_path)
                request_AI_HandwritingDistinguish["sign"] = self.calculate_sign(request_AI_HandwritingDistinguish,
                                                                                self.me_data["app_key"])
                req_data = sorted(request_AI_HandwritingDistinguish.items())
                response = requests.post(self.request_url, req_data)
                return response.text

            elif image_url is not None:
                request_AI_HandwritingDistinguish["image_url"] = image_url
                request_AI_HandwritingDistinguish["sign"] = self.calculate_sign(request_AI_HandwritingDistinguish,
                                                                                self.me_data["app_key"])
                req_data = sorted(request_AI_HandwritingDistinguish.items())
                response = requests.post(self.request_url, req_data)
                return response.text
        else:
            return "最少传入一个参数"
