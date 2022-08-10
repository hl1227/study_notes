import requests,time
from lxml import etree
from concurrent.futures import ThreadPoolExecutor


request_url_list=[]
for page_num in range(1,287):
    if page_num == 1:
        request_url_list.append('https://springnovel.com/')
    else:
        request_url_list.append('https://springnovel.com/page/312/'.format(page_num))
        #request_url_list.append('https://emgai.net/truyen-18/?p={}'.format(page_num))
domain=''
f=open('9_1000novel.txt','w+',encoding='utf-8')

headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
        'cookie':'cf_clearance=YkUOsoNpY3ghJGIwAANV4AJQn7ZdZgDYshSRDpUt.AI-1659584855-0-150; __cf_bm=XGhrMt1szETud2Xeeu8g2rlBmc5Ay6WK46.StgYJPfE-1659584860-0-AYCm4fr6/Fp7LWfNHPp+dYleUll2mZVIE74ZvMZ5TjvfrErSzFW+ZlOCuDapjAzr9HDWFaHCJ6JE/IbQnNKjwWJ9PbKqtcdccSw4/hzmKlgL0gnkcyUzcp5ehHQ75gLGYw==; _ga=GA1.2.439485834.1659584862; _gid=GA1.2.2125019183.1659584862; __atuvc=8%7C31; __atuvs=62eb415bbb025a53007',
        'sec-ch-ua':'" Not;A Brand";v="99", "Google Chrome";v="97", "Chromium";v="97"'
        }
PROXIES={"https":"http://127.0.0.1:10900","http":"http://127.0.0.1:10900"}
sess=requests.Session()

def run(url:str):
    #try:
    for i in range(0,3):
        res_1=sess.get(url,headers=headers,proxies=PROXIES)
        res_1=res_1.content.decode()
        print(res_1)
        data=etree.HTML(res_1)
        res_url_list=data.xpath("//*[@class='content']//h2/a/@href")
        if res_url_list:
            break
        # else:
        #     print(i)
        #     time.sleep(10)
    print('#' * 20, url)
    print(res_url_list,'\n',len(res_url_list))


    # for res_url in list(set(res_url_list)):
    #     # if res_url not in reqed_list:
    #     # 寻找下一页
    #     #request_info_next(res_url)
    #     #########################################
    #     #获取找全部其他页面
    #     res_x=sess.get(f'{domain}{res_url}',headers=headers,proxies=PROXIES).content.decode()
    #     data_x = etree.HTML(res_x)
    #     content_list = data_x.xpath("//div[@class='entry-content']/p")
    #     save_data(content_list,res_url,url)
    #
    #     info_other_url_list = data_x.xpath("//p[@class='pages']/a[@class='post-page-numbers']/@href")
    #     # print(info_other_url_list)
    #     for info_other_url in list(set(info_other_url_list)):
    #         res_2 = sess.get(f'{domain}{info_other_url}', headers=headers, proxies=PROXIES).content.decode()
    #         data_2 = etree.HTML(res_2)
    #         content_list = data_2.xpath("//div[@class='entry-content']/p")
    #         save_data(content_list,info_other_url,url)




def request_info_next(res_url:str):
    res_x = sess.get(f'{domain}{res_url}', headers=headers, proxies=PROXIES).content.decode()
    data_x = etree.HTML(res_x)
    content_list = data_x.xpath("//div[@class='bbWrapper']/p | //div[@class='entry-content']/p")
    save_data(content_list, res_url)
    next_url=data_x.xpath("//a[@class='nextpostslink']/@href")
    if next_url:
        request_info_next(next_url[0])

def save_data(content_list,res_url,url):
    if content_list:
        t = ''
        for content_p in content_list:
            p = ''
            for c_p in content_p.xpath('.//text()'):
                p += c_p.replace('\t', '').replace('\n', '').replace('\r', '').replace('"', '').replace('“','').replace('\xa0', '').replace('&', '').strip()
            t += p
        for tt in t.split('。'):
            if len(tt) > 50:
                f.write(tt + '。' + '\n')
        print(f'写入完成:{domain+res_url}  {url[-3:]}')
    else:
        print(f'**详情页数据错误:{domain+res_url},{content_list}')
if __name__ == '__main__':

    with ThreadPoolExecutor(max_workers=1) as pool:
        pool.map(run,request_url_list)
        pool.shutdown()
    # for url in request_url_list:
    #     run(url)
    print('获取完成!!!')