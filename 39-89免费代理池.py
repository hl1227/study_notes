import requests
from lxml import etree
import random
class Bajiudaili(object):
    #抓取89免费代理
    def __init__(self):
        headers = [{"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36"},
                   {"User-Agent": "Mozilla/5.0(compatible;MSIE9.0;WindowsNT6.1;Trident / 5.0"},
                   {"User-Agent": "Mozilla/4.0(compatible;MSIE8.0;WindowsNT6.0;Trident/4.0)"},
                   {"User-Agent": "Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;360SE)"},
                   {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0"},
                   {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1"},
                   {"User-Agent": "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"},
                   {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"},
                   {"User-Agent": "Mozilla/5.0 (hp-tablet; Linux; hpwOS/3.0.0; U; en-US) AppleWebKit/534.6 (KHTML, like Gecko) wOSBrowser/233.70 Safari/534.6 TouchPad/1.0"},
                   {"User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"},
                   {"User-Agent": "Mozilla/5.0(Macintosh;IntelMacOSX10.6;rv:2.0.1)Gecko/20100101Firefox/4.0.1"}
                   ]
        self.header = random.choice(headers)
    def daili(self):

        url1='http://www.89ip.cn/index_{}.html'
        for pages in range(1,2):
            url=url1.format(pages)
            response=requests.get(url=url,headers=self.header).text
            data=etree.HTML(response)
            ip=data.xpath('//tr/td[1]/text()')
            duankou=data.xpath('//tr/td[2]/text()')
            ip_list=[]
            for a in range(0,len(ip)):
                proxy=ip[a].strip()+':'+duankou[a].strip()
                ip_list.append(proxy)
            return ip_list

    #验证http可用性
    def http(self):
        ip_list=self.daili()
        http_list=[]
        for proxy0 in ip_list:
            proxy={}
            proxy['http']=proxy0
            url='https://search.jd.com/Search?keyword=%E5%A2%99%E7%A0%96&enc=utf-8&wq=%E5%A2%99%E7%A0%96'
            try:
                response=requests.get(url,proxies=proxy,headers=self.header,timeout=3)
            except Exception:
                print(proxy,"不可用")
            else:
                http_list.append(proxy)
        return http_list
    #验证https可用性
    def https(self):
        ip_list=self.daili()
        https_list=[]
        for proxy0 in ip_list:
            proxy={}
            proxy['https']=proxy0
            url='https://search.jd.com/Search?keyword=%E5%A2%99%E7%A0%96&enc=utf-8&wq=%E5%A2%99%E7%A0%96'
            try:
                response=requests.get(url,headers=self.header,proxies=proxy,timeout=3)
            except Exception:
                print(proxy,"不可用")
            else:
                https_list.append(proxy)
        return https_list
http=Bajiudaili().http()
https=Bajiudaili().https()
print(http)
print(https)
with open('39-ip.txt','a')as f:
    f.write(str(http))
    f.write(str(https))

