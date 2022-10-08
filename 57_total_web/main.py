'''
模仿scrapy-CrawlSpider 全站爬虫
'''
import requests,traceback,threading,re
from lxml import etree
from concurrent.futures import ThreadPoolExecutor
from queue import Queue

start_urls = ['https://www.indiatv.in/']
allowed_domain = 'indiatv.in'
allows=['.*']
denys=['.*video.*','.*livetv.*','.*news-podcast.*']
jobdir='./indiatv/0/url_filter.txt'
proxies = {"https": "http://127.0.0.1:10900", "http": "http://127.0.0.1:10900"}
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en',
}
session=requests.Session()
q=Queue(5000)
def parse_link(res_text):
    parse_links=[]
    data=etree.HTML(res_text)
    a_links=list(set(data.xpath('//a/@href')))
    for a_link in a_links:
        if allowed_domain in a_link:
            for allow in allows:
                if  re.findall(allow,a_link):
                    for deny in denys:
                        if not re.findall(deny,a_link):
                            if a_link not in parse_links:
                                parse_links.append(a_link)
    pure_links=[]
    with open(jobdir,'r',encoding='utf-8')as fr_filter:
        jobdir_list=fr_filter.read().split('\n')
        for parse_link in parse_links:
            if parse_link not in jobdir_list:
                pure_links.append(parse_links)
    return pure_links

    # with open(jobdir,'a+',encoding='utf-8')as fw_filter:
    #     for

def index_request(start_url):
    index_res=requests.get(start_url,headers=headers,proxies=proxies)
    code = index_res.apparent_encoding
    index_res_text=index_res.content.decode(code)
    pure_links=parse_link(index_res_text)
    return pure_links

def run():
    for start_url in start_urls:
        pure_links=index_request(start_url)
        print(pure_links)
if __name__ == '__main__':
    fr_filter = open(jobdir, 'a+', newline='\n')
    run()