# coding=gbk
import requests
from lxml import etree
import json
import csv

base_url = 'http://www.allitebooks.com/page/{}/'
header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36"}
data_list = []
for i in range(1,4):
    url=base_url.format(i)
    data = requests.get(url,headers=header).content.decode('gbk')
    parse_data = etree.HTML(data)
    book_list = parse_data.xpath('//div[@class="main-content-inner clearfix"]/article')

    for book in book_list:
        book_dict = {}
    #.//表示当前路径的，//text（）表示跨节点的text#书的名字
        book_dict['book_name'] = book.xpath('.//h2[@class="entry-title"]//text()')[0]
    #书的图片
        book_dict['book_image']= book.xpath('.//div[@class="entry-thumbnail hover-thumb"]//@src')[0]
    #书的作者
        book_dict['book_author'] = book.xpath('.//h5[@class="entry-author"]/a/text()')[0]
    #书的简介
        book_dict['book_info'] = book.xpath('.//div[@class="entry-summary"]/p/text()')[0]

        data_list.append(book_dict)
        title = data_list[0].keys()

        info = []
        for i in data_list:
            info.append(i.values())
    #print(info)

            write = csv.writer(open('26-数据表格.csv','w'))
            write.writerow(title)
            write.writerows(info)

