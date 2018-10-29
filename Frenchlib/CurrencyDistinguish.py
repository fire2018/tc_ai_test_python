import time
import random
import base64
import hashlib
import requests
from urllib import parse


class CurrencyDistinguish(object):
    def __init__(self, app_id, app_key):
        """
        通用ocr识别
        :param app_id: Appid  (Str)
        :param app_key: Appkey  (Str)
        """
        self.request_url = "https://api.ai.qq.com/fcgi-bin/ocr/ocr_generalocr"
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

    def start(self, img_path):
        """

        :param img_path: 图片路径  (Str)
        :return: JSON数据
        """
        request_AI_CurrencyDistinguish = {
            "app_id": self.me_data["app_id"],
            "time_stamp": self.calculate_time_stamp(),
            "nonce_str": self.calculate_nonce_str(),
            "image": self.calculate_image_base64(img_path)
        }
        request_AI_CurrencyDistinguish["sign"] = self.calculate_sign(request_AI_CurrencyDistinguish,
                                                                     self.me_data["app_key"])
        request_data = sorted(request_AI_CurrencyDistinguish.items())
        response = requests.post(self.request_url, request_data)
        return response.text
