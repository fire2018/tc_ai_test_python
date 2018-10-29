# This script will detect faces via your webcam.
# Tested with OpenCV3

import cv2
from Frenchlib import IDCardIdentification
import demjson
import json
import base64

app_id = "your appid"
app_key = "your appkey"

def strToImage(str,filename):
    image_str= str.encode('ascii')
    image_byte = base64.b64decode(image_str)
    image_json = open(filename, 'wb')
    image_json.write(image_byte)  #将图片存到当前文件的fileimage文件中
    image_json.close()


cap = cv2.VideoCapture(0)

# Create the haar cascade
faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

while(True):
	# Capture frame-by-frame
	ret, frame = cap.read()	
	cv2.imwrite('C:\\Apache24\\htdocs\\image\\1\\111.jpg', frame)
	test1 = IDCardIdentification.IDCardIdentification(app_id, app_key)
	js = test1.start('C:\\Apache24\\htdocs\\image\\1\\111.jpg',0)
	
	hjson = json.loads(js)

	print('姓名：'+hjson['data']['name'])
	print('性别：'+hjson['data']['sex'])
	print('民族：'+hjson['data']['nation'])
	print('生日：'+hjson['data']['birth'])
	print('地址：'+hjson['data']['address'])
	print('id：'+hjson['data']['id'])
	file_address = "C:\\Apache24\\htdocs\\image\\1\\" + hjson['data']['name'] + r".jpg"
	strToImage(hjson['data']['frontimage'],file_address)

	# Display the resulting frame
	cv2.imshow('frame', frame)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
