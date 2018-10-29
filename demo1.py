from Frenchlib import LicensePlateDistinguish
from Frenchlib import FaceContrast
from Frenchlib import FaceDetectionAndAnalysis
from Frenchlib import FaceFusion
from Frenchlib import FaceMakeup
from Frenchlib import FacialMakeup
from Frenchlib import Filter
from Frenchlib import FoodPictureRecognition
from Frenchlib import Gossip
from Frenchlib import HandwritingDistinguish
from Frenchlib import IDCardIdentification
from Frenchlib import ImageLabelRecognition
from Frenchlib import IntelligentYellowing
from Frenchlib import IntentionOrConstituent
from Frenchlib import LicensePlateDistinguish
from Frenchlib import LookAndSay
from Frenchlib import MultipleFaceDetection
from Frenchlib import ObjectRecognition
from Frenchlib import Participle
from Frenchlib import PartOfPpeech
from Frenchlib import PigmentsAgeDetection
from Frenchlib import PositionOfFiveSenses
from Frenchlib import ProperNouns
from Frenchlib import SceneRecognition # 场景识别
from Frenchlib import Sticker # 大头贴
from Frenchlib import Synonym # 基础文本分析_同义词
from Frenchlib import TextTranslation # 文本翻译
from Frenchlib import TravelOrDriveCardDistinguish # 行驶证和驾驶证的识别
from Frenchlib import ViolentTerrorIdentification # 暴恐识别
from Frenchlib import VisitingCardIdentification # 名片识别


import demjson
import json
import base64

app_id = "your appid"
app_key = "your appkey"

'''# 名片识别
image = "C:\\Apache24\\htdocs\\image\\1\\mp.jpg"
test1 = VisitingCardIdentification.VisitingCardIdentification(app_id, app_key)
js = test1.start(image)
'''
'''# 暴恐识别
image = "C:\\Apache24\\htdocs\\image\\1\\xsz2.jpg"
test1 = ViolentTerrorIdentification.ViolentTerrorIdentification(app_id, app_key)
js = test1.start(image)
'''
'''# 行驶证和驾驶证的识别
image = "C:\\Apache24\\htdocs\\image\\1\\xsz2.jpg"
test1 = TravelOrDriveCardDistinguish.TravelOrDriveCardDistinguish(app_id, app_key)
js = test1.start(image,0)
'''
'''# 文本翻译
image = "C:\\Apache24\\htdocs\\image\\1\\mie5.jpg"
test1 = TextTranslation.TextTranslation(app_id, app_key)
js = test1.start('en','zh',"CCTV news (news network): a bridge even three places, the day cut to change the road. The opening ceremony of the Hong Kong-Zhuhai-Macao Bridge was held in Zhuhai, Guangdong Province, on the morning of April 23. Xi Jinping, general secretary of the CPC Central Committee, President of the State and Chairman of the Central military Commission, attended the ceremony to announce the official opening of the bridge and tour the bridge. On behalf of the CPC Central Committee, he expressed sincere thanks and sincere greetings to the vast number of people involved in the design, construction, and management of the bridge.")
'''
'''# 基础文本分析_同义词
image = "C:\\Apache24\\htdocs\\image\\1\\mie5.jpg"
test1 = Synonym.Synonym(app_id, app_key)
js = test1.start("古道西风瘦马，夕阳西下，断肠人在天涯")
'''
'''# 大头贴
image = "C:\\Apache24\\htdocs\\image\\chengzj.jpg"
test1 = Sticker.Sticker(app_id, app_key)
js = test1.start(1,image)
'''
'''# 场景识别
image = "C:\\Apache24\\htdocs\\image\\1\\mie5.jpg"
test1 = SceneRecognition.SceneRecognition(app_id, app_key)
js = test1.start(image)
'''
'''#基础文本分析_专有名词
image = "C:\\Apache24\\htdocs\\image\\1\\mie5.jpg"
test1 = ProperNouns.ProperNouns(app_id, app_key)
js = test1.start("古道西风瘦马，夕阳西下，断肠人在天涯")
'''
'''#五官定位
image = "C:\\Apache24\\htdocs\\image\\1\\mie5.jpg"
test1 = PositionOfFiveSenses.PositionOfFiveSenses(app_id, app_key)
js = test1.start(image)
'''
'''#颜龄检测
image = "C:\\Apache24\\htdocs\\image\\1\\mie5.jpg"
test1 = PigmentsAgeDetection.PigmentsAgeDetection(app_id, app_key)
js = test1.start(image)
'''
'''#基础文本分析_词性
image = "C:\\Apache24\\htdocs\\image\\1\\cat1.jpg"
test1 = PartOfPpeech.PartOfPpeech(app_id, app_key)
js = test1.start("古道西风瘦马，夕阳西下，断肠人在天涯")
'''
'''#基础文本分析_分词
image = "C:\\Apache24\\htdocs\\image\\1\\cat1.jpg"
test1 = Participle.Participle(app_id, app_key)
js = test1.start("古道西风瘦马，夕阳西下，断肠人在天涯")
'''
'''#物体识别
image = "C:\\Apache24\\htdocs\\image\\1\\cat1.jpg"
test1 = ObjectRecognition.ObjectRecognition(app_id, app_key)
js = test1.start(image)
'''
'''#看图说话
image = "C:\\Apache24\\htdocs\\image\\1\\yge1.jpg"
test1 = LookAndSay.LookAndSay(app_id, app_key)
js = test1.start(image)
'''
'''#车牌识别
image = "C:\\Apache24\\htdocs\\image\\24.jpg"
test1 = LicensePlateDistinguish.LicensePlateDistinguish(app_id, app_key)
js = test1.start(image)
'''
'''#意图分析
image = "C:\\Apache24\\htdocs\\image\\1\\zhang2.jpg"
test1 = IntentionOrConstituent.IntentionOrConstituent(app_id, app_key)
js = test1.start("古道西风瘦马，夕阳西下，断肠人在天涯")
'''
'''#智能鉴黄
image = "C:\\Apache24\\htdocs\\image\\1\\zhang2.jpg"
test1 = IntelligentYellowing.IntelligentYellowing(app_id, app_key)
js = test1.start(image)
'''
'''#图片标签
image = "C:\\Apache24\\htdocs\\image\\1\\ms1.jpg"
test1 = ImageLabelRecognition.ImageLabelRecognition(app_id, app_key)
js = test1.start(image)
'''
'''#手写体识别
image = "C:\\Apache24\\htdocs\\image\\1\\sx3.jpg"
test1 = HandwritingDistinguish.HandwritingDistinguish(app_id, app_key)
js = test1.start(image)
'''
'''#美食
image = "C:\\Apache24\\htdocs\\image\\1\\ms1.jpg"
test1 = FoodPictureRecognition.FoodPictureRecognition(app_id, app_key)
js = test1.start(image)
'''
'''#滤镜
image = "C:\\Apache24\\htdocs\\image\\1\\re1.jpg"
test1 = FacialMakeup.FacialMakeup(app_id, app_key)
js = test1.start(4,image)
'''
'''#人脸美妆
image = "C:\\Apache24\\htdocs\\image\\1\\re1.jpg"
test1 = FacialMakeup.FacialMakeup(app_id, app_key)
js = test1.start(4,image)
'''
'''#人脸变装
image = "C:\\Apache24\\htdocs\\image\\1\\te1.jpg"
test1 = FaceMakeup.FaceMakeup(app_id, app_key)
js = test1.start(4,image)
'''
'''#图像融合
image = "C:\\Apache24\\htdocs\\image\\chengzj.jpg"
test1 = FaceFusion.FaceFusion(app_id, app_key)
js = test1.start(5,image)
'''

'''#面部分析与检测
image = "C:\\Apache24\\htdocs\\image\\1\\yang2.jpg"
test1 = FaceDetectionAndAnalysis.FaceDetectionAndAnalysis(app_id, app_key)
js = test1.start(image,mode=0)
'''
'''#人脸对比
image0 = "C:\\Apache24\\htdocs\\image\\1\\qian1.jpg"
image1 = "C:\\Apache24\\htdocs\\image\\1\\chen2.jpg"
test1 = FaceContrast.FaceContrast(app_id, app_key)
js = test1.start(image0,image1)
'''
'''#车牌识别
image = "C:\\Apache24\\htdocs\\image\\21.jpg"
test1 = LicensePlateDistinguish.LicensePlateDistinguish(app_id, app_key)
js = test1.start(img_path=image)
'''
'''#身份证识别
image = "C:\\Apache24\\htdocs\\image\\11.jpg"
test1 = IDCardIdentification.IDCardIdentification(app_id, app_key)
js = test1.start(image,0)
'''
#'''#智能聊天
string = "上海天气!"
test1 = Gossip.Gossip(app_id, app_key)
js = test1.start(string)
#'''
print(js)

def strToImage(str,filename):
    image_str= str.encode('ascii')
    image_byte = base64.b64decode(image_str)
    image_json = open(filename, 'wb')
    image_json.write(image_byte)  #将图片存到当前文件的fileimage文件中
    image_json.close()
#'''
hjson = json.loads(js)
file_address = "C:\\Apache24\\htdocs\\image\\1\\" + r"new" + r".jpg"
strToImage(hjson['data']['image'],file_address)
#'''
# 身份证
#file_address = "C:\\Apache24\\htdocs\\image\\1\\" + hjson['data']['name'] + r".jpg"
#strToImage(hjson['data']['frontimage'],file_address)

 



