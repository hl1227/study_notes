#coding=utf-8
import requests
from lxml import etree
import random
def daili():
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
    header = random.choice(headers)
    #抓取西刺高匿代理
    url_daili='https://www.xicidaili.com/nn/1'
    response=requests.get(url_daili,headers=header).text
    data=etree.HTML(response)
    ip=data.xpath('//tr/td[contains(text(),".")]/text()')
    duankou=data.xpath('//tr/td[3]/text()')
    leixing=data.xpath('//tr/td[6]/text()')
    #处理代理，拼接
    proxy_list0=[]
    for a in range(0,len(ip)):
        proxy=leixing[a].lower()+':'+ip[a]+':'+duankou[a]
        proxy_list0.append(proxy)
    proxy_https=[]
    proxy_http=[]
    for proxy in proxy_list0:
        if proxy[4]=='s':
            https = {}
            https['https']=proxy[6:]
            proxy_https.append(https)
        else:
            http = {}
            http['http']=proxy[5:]
            proxy_http.append(http)

    #测试代理可用性及速度
    url='http://www.baidu.com/'
    for proxy in proxy_http:
        respons=requests.get(url,headers=header,proxies=proxy)
        print(respons.status_code)
        print(respons.elapsed.microseconds/1000000)
    return proxy_https,proxy_http
a=daili()
print(a)


