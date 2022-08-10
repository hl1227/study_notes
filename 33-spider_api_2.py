import requests,traceback
from lxml import etree
from concurrent.futures import ThreadPoolExecutor

request_url_list=[]
for page_num in range(1,38):
    request_data={
        "action":"load_more_page_keyword",
        "the_loai":"DICHEDIT",
        "current_page_tax":f"{page_num}",
        "option_keyword_tax":"new-chap",
    }
    request_url_list.append(request_data)
f=open('14_truyenkk1_DICHEDIT.txt','w+',encoding='utf-8')
domain=''


headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
         #'cookie':'werA_0ff6_saltkey=8eA8Zkqo; werA_0ff6_lastvisit=1659581931; werA_0ff6_sid=mzQLXw; _ga=GA1.2.927147631.1659585571; _gid=GA1.2.387656995.1659585571; werA_viewadult=acceptrule; werA_0ff6_visitedfid=6; werA_0ff6_sendmail=1; _gat_gtag_UA_6272726_1=1; werA_0ff6_lastact=1659585999%09forum.php%09forumdisplay; werA_0ff6_forum_lastvisit=D_6_1659585999'
         }
PROXIES={"https":"http://127.0.0.1:10900","http":"http://127.0.0.1:10900"}
sess=requests.Session()

def run(request_data):
    try:
        res_11=requests.post('https://truyenkk1.com/wp-admin/admin-ajax.php',headers=headers,data=request_data,proxies=PROXIES)
        res_1=res_11.text
        data=etree.HTML(res_1)
        res_url_list=data.xpath("//h2[@class='crop-text-2']/a/@href")
        print('------',request_data['current_page_tax'],len(res_url_list),'\n',res_url_list)
        if res_url_list:
            for res_url in res_url_list[0:]:
                try:
                    if '/tag/....' not in res_url:
                        res_2=sess.get(domain+res_url,headers=headers,proxies=PROXIES)
                        res_2 = res_2.text
                        data_2 = etree.HTML(res_2)
                        index_url_list=data_2.xpath("//div[@class='col-xs-12 crop-text']/a/@href | //div[@id='abody']/div")
                        print(index_url_list)
                        request_info_next(index_url_list[0])
                except:
                    print(f'**详情页数据错误:{domain+res_url}:\n{traceback.format_exc()}','*' * 100)
        else:
            print('**分类页数据错误:',traceback.format_exc())
    except Exception as e:
        print(f'**错误:\n{traceback.format_exc()}','*'*100)
def request_info_next(res_url:str):
    res_x = sess.get(f'{domain}{res_url}', headers=headers, proxies=PROXIES).content.decode()
    data_x = etree.HTML(res_x)
    content_list = data_x.xpath("//div[@class='reading'] | //div[@class='entry-content']/p")
    save_data(content_list, res_url)
    next_url=data_x.xpath("//a[contains(text(),'Chương Tiếp »')]/@href")
    if next_url:
        request_info_next(next_url[0])
def save_data(content_list,res_url):
    if content_list:
        t = ''
        for content_p in content_list:
            p = ''
            for c_p in content_p.xpath('.//text()'):
                p += c_p.replace('\t', '').replace('\n', '').replace('\r', '').replace('"', '').replace('“','').replace('\xa0', '').replace('&', '').strip()
            t += p
        for tt in t.split('.'):
            if len(tt) > 50:
                f.write(tt + '.' + '\n')
        print(f'写入完成:{domain+res_url}')
    else:
        print(f'**详情页数据错误:{domain+res_url},{content_list}')
if __name__ == '__main__':
    with ThreadPoolExecutor(max_workers=10) as pool:
        pool.map(run,request_url_list)
        pool.shutdown()
    # for url in request_url_list:
    #     run(url)
    print('获取完成!!!')
