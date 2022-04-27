
#xpth是一种语法，需要安装lxml，html和xml的解析库
from lxml import etree

import requests

url = "https://news.baidu.com/"

headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"
}

data = requests.get(url,headers=headers).content.decode()

#print(data)

#1.转换类型成XPTH解析类
xpath_data = etree.HTML(data)

#2调用XPATH 方法
# /表示层级关系
result = xpath_data.xpath('/html/head/title/text()')
# //a表示跨多个层级的所有a标签
result = xpath_data.xpath('//a/text()')
# 找到a标签符合的@属性  //a[@属性="属性值"] 网页中查找
result = xpath_data.xpath('//a[@mon="ct=1&a=2&c=top&pn=1"]/text()')
#获取属性，标签的网址,返回一个列表
result = xpath_data.xpath('//a[@mon="ct=1&a=2&c=top&pn=1"]/@href')

result=xpath_data.xpath('//a[contains(@mon,"ct=")]/@href')
print(result)