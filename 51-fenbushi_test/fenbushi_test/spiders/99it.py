from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule
import time
from scrapy_redis.spiders import RedisCrawlSpider
class Hy_99it_Spider(RedisCrawlSpider):
    name = 'hy_99it'
    redis_key = 'start_urls'
    page = 0
    #更新设置--------------------------------------------------
    # start_time = time.time()
    # up_time = 600  # 更新 秒
    #custom_settings = {
                       #设置爬取算法模式
                       # 'SCHEDULER_DISK_QUEUE' : 'scrapy.squeues.PickleFifoDiskQueue',
                       # 'SCHEDULER_MEMORY_QUEUE' : 'scrapy.squeues.FifoMemoryQueue',
                       # 'DEPTH_PRIORITY': 1, #0表示深度优先,1表示广度优先
                       # 'DEPTH_LIMIT' : 5    #最大深度值
                       #  'CONCURRENT_REQUESTS':32,
                       #  'DOWNLOAD_DELAY':1,
                       #  'CONCURRENT_REQUESTS_PER_DOMAIN' :32,
                       # 'LOG_LEVEL':'DEBUG'
                        #}
    #-默认入库,入FTP,入分类设置,更新时长---------------------------
    # table_name = 'hy_cn_tech'   #mysql表名
    # default_category='tech'          #默认分类
    #--------------------------------------------------------
    rules = (Rule(LinkExtractor(allow=r'http://www.99it.com.cn/news/.*html$'), callback='parse_item', follow=True),
             Rule(LinkExtractor(allow=r'http://www.99it.com.cn/.*'),follow=True),)

    def __init__(self):
        self.allowed_domains=['99it.com.cn']

    #     # mysql------------------------------------------
    #     self.conn = pymysql.Connect(
    #         host='154.212.112.247',
    #         port=13006,
    #         # 数据库名：
    #         db='seo-hy',
    #         user="root",
    #         passwd='itfkgsbxf3nyw6s1',
    #         charset='utf8')
    #     self.cur = self.conn.cursor()
        super(Hy_99it_Spider, self).__init__(name='hy_99it')

    def parse_item(self, response):
        # 后续更新:启动10分钟后关闭
        # if time.time() - self.start_time >= self.up_time:
        #     self.crawler.engine.close_spider(self, "更新10分钟完成!!")
        item = {}
        url=response.url
        item['url'] = url
        # 标题
        try:
            item['title'] = response.xpath("//h1/text()").extract_first()
            if item['title'] == None:
                item['title'] = ''
        except Exception:
            item['title'] = ''
        # 关键字
        try:
            item['keyword'] = response.xpath("//meta[@name='keywords']/@content").extract_first().replace(',“','')
            if item['keyword'] ==None or len(item['keyword'])<1:
                item['keyword'] = item['title'].replace(' ',',')
        except Exception:
            item['keyword'] = item['title'].replace(' ',',')
        # 摘要
        try:
            item['description'] = response.xpath("//meta[@name='description']/@content").extract_first().replace('原标题：','')
            if item['description'] == None:
                item['description'] = response.xpath("//meta[@property='og:description']/@content").extract_first()
            if item['description'] == None:
                item['description'] = item['title']
        except Exception:
            item['description'] = item['title']
        # 图片
        try:
            img_url=response.xpath("//div[@class='content_right']//img/@src").extract_first()
            if 'logo' in img_url or img_url == None:
                item['img_src'] = ''
            else:
                if img_url[0]=='h':
                    item['img_src']=img_url
                else:
                    item['img_src']='http://www.99it.com.cn'+img_url
        except Exception:
            item['img_src'] = ''
        # 正文
        try:
            cont=''
            #item['content'] =''.join(response.xpath("//div[@class='content_right']/div[1]//text()").extract()[2:]).replace('\n','').replace('投稿邮箱：jiujiukejiwang@163.com','').replace('。','。\n').replace('详情访问99科技网：http://www.99it.com.cn','').replace('相关推荐', '').replace('	', '').replace(' ', '').strip()
            txt_list=response.xpath("//div[@class='content_right']/div[1]//text()").extract()[2:]
            if len(txt_list)>4:
                for txt in txt_list:
                    if len(txt)>4:
                        cont+=txt.replace('\n','').strip()
            item['content']=cont.replace('投稿邮箱：jiujiukejiwang@163.com','').replace('详情访问99科技网：http://www.99it.com.cn','').replace('相关推荐', '').replace('。','。\n')
        except Exception:
            item['content'] = ''

        # 作者
        try:
            item['author'] = response.xpath("//div[@class='mate']/span[3]/text()").extract_first()[3:]
            if item['author'] == None:
                item['author'] = '马铃薯科技'
        except Exception:
            item['author'] = '马铃薯科技'

        # 发行时间
        try:
            item['release_time'] = response.xpath("//div[@class='mete']/span[1]/text()").extract_first()
            if item['release_time'] == None:item['release_time']=time.strftime('%Y-%m-%d %H:%M:%S')
        except Exception:
            item['release_time'] = time.strftime('%Y-%m-%d %H:%M:%S')
        #分类
        try:
            item['category']='tech'
        except Exception:
            item['category']='tech'
        # 来源
        item['be_from'] ='http://www.99it.com.cn/'
        #生成器返回:
        if len(item['title']) >=1 and len(item['content']) >= 50 and item['category'] != '':
            print(item)
        #     #-----------入库去重--------------------------------------
        #     find_ex = "select id,url from {} where title= %s ".format(self.table_name)
        #     self.cur.execute(find_ex, (item["title"]))
        #     if not self.cur.fetchone():
        #         news = "insert into {}(title,content,author,release_time,keyword,description,url,img_src,category,create_time,be_from) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)".format(self.table_name)
        #         self.cur.execute(news, (item['title'], item['content'], item['author'], item['release_time'], item['keyword'],item['description'], item['url'],item['img_src'], item['category'], time.time(),item['be_from']))
        #         self.conn.commit()
        #         self.page += 1
        #         print(time.strftime('%Y.%m.%d-%H:%M:%S'), '第', self.page, '条抓取成功:', item['url'])
        #     else:print('**数据重复:',item['url'])
        # else:
        #     print('##数据不匹配:标题长度:',len(item['title']),'文本长度:',len(item['content']),'category:',item['category'],response.url)
    #
    #
    # def close(self, reason):
    #     print(reason,'共抓取:',self.page,'条数据')
    #     self.conn.close()
        ##self.crawler.engine.close_spider(self, "关闭spider")
        #scrapy crawl hy_99it
