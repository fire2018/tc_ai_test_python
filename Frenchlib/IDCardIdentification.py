import base64
import requests
import time
import random
import hashlib
from urllib import parse


class IDCardIdentification(object):
    def __init__(self, app_id, app_key):
        """
        身份证识别
        :param app_id: Appid  (Str)
        :param app_key: Appkey  (Str)
        """
        # 设置请求地址
        self.request_url = "https://api.ai.qq.com/fcgi-bin/ocr/ocr_idcardocr"
        self.me_data = {
            "app_id": app_id,
            "app_key": app_key
        }

    # 计算sign
    def calculate_sign(self, req_dict, app_key):
        # 获取列表化升序字典
        sort_list = sorted(req_dict.items())
        #print(sort_list)
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
    def calculate_note_str():
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
        #ls = base64.b64encode(img_path)
        ls = str(ls, encoding="utf-8")
        img.close()
        return ls

    def start(self, ima_path, types):
        """

        :param ima_path: 要识别的图片路径(str)
        :param types: 识别类型，0为正面，1为反面(int)
        :return: json数据
        """

        #'''
        request_AI_IDCardIdentification = {
            "app_id": self.me_data["app_id"],
            "time_stamp": self.calculate_time_stamp(),
            "nonce_str": self.calculate_note_str(),
            "image": self.calculate_img_base64(ima_path),
            "card_type": types
        } 
        #'''
        '''
        request_AI_IDCardIdentification = {
            "app_id": self.me_data["app_id"],
            "time_stamp": '2109086611',
            "nonce_str": '2109086611',
            "image": self.calculate_img_base64(ima_path),
            "card_type": types
        
        '''
        request_AI_IDCardIdentification["sign"] = self.calculate_sign(request_AI_IDCardIdentification,
                                                                      self.me_data["app_key"])
        print(request_AI_IDCardIdentification["sign"])
        req_data = sorted(request_AI_IDCardIdentification.items())
        #print(req_data)
        response = requests.post(self.request_url, req_data)
        return response.text
