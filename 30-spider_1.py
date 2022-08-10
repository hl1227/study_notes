import requests,traceback,threading
from lxml import etree
from concurrent.futures import ThreadPoolExecutor

request_url_list=[]
for page_num in range(1,610):
    if page_num==1:
        request_url_list.append('https://oursogo.com/forum-6-1.html')
    else:
        request_url_list.append('https://oursogo.com/forum-6-{}.html'.format(page_num))
    #request_url_list.append('https://emgai.net/truyen-18/?p={}'.format(page_num))
f=open('8_oursogo.txt','w+',encoding='utf-8')
domain=''


headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
         'cookie':'werA_0ff6_saltkey=8eA8Zkqo; werA_0ff6_lastvisit=1659581931; werA_0ff6_sid=mzQLXw; _ga=GA1.2.927147631.1659585571; _gid=GA1.2.387656995.1659585571; werA_viewadult=acceptrule; werA_0ff6_visitedfid=6; werA_0ff6_sendmail=1; _gat_gtag_UA_6272726_1=1; werA_0ff6_lastact=1659585999%09forum.php%09forumdisplay; werA_0ff6_forum_lastvisit=D_6_1659585999'
         }
PROXIES={"https":"http://127.0.0.1:10900","http":"http://127.0.0.1:10900"}
sess=requests.Session()

def run(url:str):
    try:
        res_11=requests.get(url,headers=headers,proxies=PROXIES)
        res_1=res_11.text
        data=etree.HTML(res_1)
        res_url_list=data.xpath("//th[@class='common']/a/@href")
        print('------',url,len(res_url_list),'\n',res_url_list)
        if res_url_list:
            for res_url in res_url_list[0:]:
                try:
                    if '/tag/....' not in res_url:
                        res_2=sess.get(domain+res_url,headers=headers,proxies=PROXIES)
                        res_2 = res_2.text
                        data_2 = etree.HTML(res_2)
                        content_list=data_2.xpath("//*[@class='t_f'] | //div[@id='abody']/div")
                        if content_list:
                            t=''
                            for content_p in content_list:
                                p=''
                                for c_p in content_p.xpath('.//text()'):
                                    p+=c_p.strip()
                                t+=p
                            for tt in t.replace('\t','').replace('\n','').replace('\r','').replace('"','').replace('“','').replace('\xa0','').replace('&','').replace('【本文轉載自AAA成人小說(aaanovel.com)】','').split('。'):
                                if len(tt) > 50:
                                    f.write(tt+'。'+'\n')
                            print(f'写入完成:{domain+res_url}')
                        else:
                            print(f'**详情页数据错误:{domain+res_url},{content_list}')
                except:
                    print(f'**详情页数据错误:{domain+res_url}:\n{traceback.format_exc()}', '*' * 100)
        else:
            print('**分类页数据错误:',traceback.format_exc())
    except Exception as e:
        print(f'**错误:{url}:\n{traceback.format_exc()}','*'*100)

if __name__ == '__main__':
    with ThreadPoolExecutor(max_workers=1) as pool:
        pool.map(run,request_url_list)
        pool.shutdown()
    # for url in request_url_list:
    #     run(url)
    print('获取完成!!!')
