import requests,random,time
from lxml import etree

class ShangBiao_img():

       def open_json(self):
              with open('搜索结果1.json','r',encoding='utf-8')as f:
                     item=f.read()
              item=eval(item)
              print(item)
              dict=item['rows']
              print(dict)
              for data in dict:
                  print(data)
                  self.page_no=data["page_no"]
              print('page_no=========',self.page_no)
       def get_id(self):
              session=requests.session()
              self.headers = {"Accept": "application/json, text/javascript, */*; q=0.01",
                              "Accept-Encoding": "gzip, deflate",
                              "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
                              "Connection": "keep-alive",
                              "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                              "Cookie":'',# cookie
                              "Host": "sbgg.saic.gov.cn:9080",
                              "Origin": "http://sbgg.saic.gov.cn:9080",
                              "Referer": "http://sbgg.saic.gov.cn:9080/tmann/annInfoView/annSearch.html?annNum=1641",
                              "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
                              "X-Requested-With": "XMLHttpRequest", }
              data={'annNum':'1642',
                    'annTypecode':'TMZCSQ'
              }
              url='http://sbgg.saic.gov.cn:9080/tmann/annInfoView/selectInfoidBycode.html'
              self.id=session.post(url=url,headers=self.headers,data=data).text
              print('id============',self.id)
       def get_img(self):
              url="http://sbgg.saic.gov.cn:9080/tmann/annInfoView/imageView.html"
              data={'id':self.id,
                    'pageNum':'1',
                    'flag':'1'
              }
              img_json=requests.post(url=url,headers=self.headers,data=data).text
              print(img_json)
              image = img_json["imaglist"][3]
              print(image)
       def run(self):
              self.open_json()
              self.get_id()
              self.get_img()
ShangBiao_img().run()



