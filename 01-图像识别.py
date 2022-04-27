#连接百度图像识别，建立应用
# http://console.bce.baidu.com/ai/?fromai=1#/ai/easydl/app/detail~appId=922387
from aip import AipOcr

with open('01-图像识别.png','rb')as f:
    img=f.read()
    """ 你的 APPID AK SK """
APP_ID = '15988481'
API_KEY = 'ahHikEiAzQT18ZCOT0CO9gfc'
SECRET_KEY = '5Zdk4r4NCpNtmvvI385jOnEquaO7msjl'
client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
a=client.accurate(img)
print(a)
for list in a['words_result']:
    text=list['words']
    print(text)