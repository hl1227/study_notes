#coding=utf-8
#目标：自动登陆马蜂窝，并爬取个人中心数据
import requests
from lxml import etree

#增加代理IP
url = "http://icanhazip.com"
headers = {
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36"
          }
proxy = {'http':'112.85.131.247:9999',
         'https': '112.85.131.247:9999'}
response = requests.get(url,headers=headers,proxies=proxy,verify=False)

print(response.text)
print(response.elapsed.microseconds/1000000)

#############################################################################################################

session=requests.Session()
#     sess = requests.Session()
#     sess.keep_alive = False  # 关闭多余连接
data={'passport':'13521093039','password':'password123'}
heder={
     'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
     'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
     }

url='https://passport.mafengwo.cn/login/'
response = session.post(url=url,headers=heder,data=data)

print(response.status_code)
#获取缓存
cook=session.cookies.get_dict()
print(cook)


url1 = 'http://www.mafengwo.cn/friend/index/follow'
response1=session.get(url=url1,headers=heder,cookies=cook).content

data=etree.HTML(response1)
info=data.xpath('//div[@class="name"]/a/text()')
print(info)


####################################################################
import requests
class Requests(object):
    def __init__(self):
        url = "https://www.baidu.com/s?wd=5656"
        headers = {
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36"
        }
        self.response =requests.get(url,headers=headers)
    def run(self):
        data = self.response.content
        #获取请求头：
        requests_headers = self.response.request.headers
        print(requests_headers)
        #获取响应头
        response_headers = self.response.headers
        print(response_headers)
        #获取状态吗
        code = self.response.status_code
        print(code)
        #获取请求的cookie，百度没有，是浏览器添加的
        #request_cookie = self.response.request.cookies
        #print(request_cookie)
        #获取响应的cookie
        response_cookie = self.response.cookies
        print(response_cookie)
Requests().run()

####################################################################################
import requests

#session()可以自动保存cookies
session = requests.session()

url = "https://www.yaozh.com/login/"
#登陆数据
form_data = {
    "username":"fjfj1227",
    "pwd":"66884747",
    "formhash":"1278599113",
    "backurl":"https%3A%2F%2Fwww.yaozh.com%2F"
}
headers = {
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36"
          }
#发送post请求
response = session.post(url,data=form_data,headers=headers)



url1 = "https://www.yaozh.com/member/"
#登陆成功后，带着有效数据，求情目标数据
data = session.get(url1,headers=headers).content
with open("17-yaozhi.html","wb")as f:
    f.write(data)
print(data)

#############解混淆
import ast
import astunparse
class VisitLiteral(ast.NodeVisitor):
    pass

if __name__ == '__main__':
    # s = '"""asd\\x22\\x3e"""'
    # xx = ast.parse(g_response)
    # VisitLiteral().visit(xx)
    # print(astunparse.unparse(xx))

    # 方案2 容错高
    node = ast.parse(repr(g_response).replace("\\\\", "\\"))
    VisitLiteral().visit(node)
    print(astunparse.unparse(node))




