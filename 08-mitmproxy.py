# import pyperclip
# print(pyperclip.paste())
# import uiautomator2 as u2,time
# d=u2.connect('127.0.0.1:62001')
# #打开APP
# d.xpath('//*[@text="抖音"]').click()
# #点击搜索
# d.click(0.936, 0.049)
# #输入内容
# # d.send_keys("科技", clear=True)
# time.sleep(5)
# d.app_stop_all()
# "C:\Program Files\Google\Chrome\Application\chrome.exe" --proxy-server=127.0.0.1:8080 --ignore-certificate-errors

#from mitmproxy import ctx
import mitmproxy.http
import json
class Counter():
    def requests(self,flow:mitmproxy.http.HTTPFlow):
        print(flow.request.url)
    def response(self,flow:mitmproxy.http.HTTPFlow):
        print(json.loads(flow.response.text))

addons=[Counter()]
'''运行方式:
        mitmweb为您提供基于浏览器的 GUI
        1将要拦截的软件端口设置为8080,并下载好证书
        2命令行运行:mitmdump
        3 mitmdump -s addons.py
        高级:https://www.liuyixiang.com/post/108653.html
'''