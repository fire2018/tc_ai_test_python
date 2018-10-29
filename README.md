# tc_ai_test_python
根据腾讯公开ai接口（https://ai.qq.com/）以及第三方的java库（http://taip.mydoc.io/?t=307518）开发的python程序
python版本是3.6
demo1目前实现的功能：
from . import BankCardDistinguish # 银行卡识别
from . import BlurredImageRecognition # 模糊图片识别
from . import BusinessLicenseDistinguish # 营业执照识别
from . import CrossAgeFaceRecognition # 跨年龄人脸识别
from . import CurrencyDistinguish # 通用ocr识别
from . import EmotionalAnalysis # 情感分析
from . import FaceContrast # 人脸对比
from . import FaceDetectionAndAnalysis # 人脸检测与分析
from . import FaceFusion # 人脸融合
from . import FaceMakeup # 人脸变装
from . import FacialMakeup # 人脸美妆
from . import Filter # 滤镜（天天P图）
from . import FoodPictureRecognition # 美食图片识别
from . import Gossip #智能聊天
from . import HandwritingDistinguish # 手写体识别
from . import IDCardIdentification # 身份证识别
from . import ImageLabelRecognition # 图像标签识别
from . import IntelligentYellowing # 智能鉴黄
from . import IntentionOrConstituent # 意图分析
from . import LicensePlateDistinguish # 车牌识别
from . import LookAndSay # 看图说话
from . import MultipleFaceDetection # 多人脸检测
from . import ObjectRecognition # 物体识别
from . import Participle # 基础文本分析_分词
from . import PartOfPpeech # 基础文本分析_词性
from . import PigmentsAgeDetection # 颜龄检测
from . import PositionOfFiveSenses # 五官定位
from . import ProperNouns # 基础文本分析_专有名词
from . import SceneRecognition # 场景识别
from . import Sticker # 大头贴
from . import Synonym # 基础文本分析_同义词
from . import TextTranslation # 文本翻译
from . import TravelOrDriveCardDistinguish # 行驶证和驾驶证的识别
from . import ViolentTerrorIdentification # 暴恐识别
from . import VisitingCardIdentification # 名片识别

live是用摄像头直接获取身份证信息（ocr）的例子，使用了opencv。
