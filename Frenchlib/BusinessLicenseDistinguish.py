import time
import random
import base64
import hashlib
import requests
from urllib import parse


class BusinessLicenseDistinguish(object):
    def __init__(self, app_id, app_key):
        """
        营业执照识别
        :param app_id:腾讯AI的APPID  (Str)
        :param app_key: 腾讯AI的APPKEY  (Str)
        """
        self.request_url = "https://api.ai.qq.com/fcgi-bin/ocr/ocr_bizlicenseocr"
        self.me_data = {
            "app_id": app_id,
            "app_key": app_key,
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
            nonce_str = data[random.randint(0, len(examples) - 1)]
        return nonce_str

    @staticmethod
    def calculate_image_base64(img_path):
        image = open(img_path, "rb")
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
        request_AI_BusinessLicenseDistinguish = {
            "app_id": self.me_data["app_id"],
            "time_stamp": self.calculate_time_stamp(),
            "nonce_str": self.calculate_nonce_str(),
            "image": self.calculate_image_base64(img_path)
        }
        request_AI_BusinessLicenseDistinguish["sign"] = self.calculate_sign(request_AI_BusinessLicenseDistinguish,
                                                                            self.me_data["app_key"])
        req_data = sorted(request_AI_BusinessLicenseDistinguish.items())
        response = requests.post(self.request_url, req_data)
        return response.text
