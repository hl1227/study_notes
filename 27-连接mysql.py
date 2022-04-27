import pymysql,time
#'查看SQL连接线程'
# show processlist;

        # 书名字,  分类,作者, 图片链接   ,介绍,  正文,     章节名         章节地址
        #    title,cate,author,img_src,intro,content,chapter_title,chapter_src
#小说库
class sql():
    def __init__(self):
        # 1建立数据库链接  返回一个对象   connect()
        self.conn = pymysql.Connect(
            host='localhost',
            port=3306,
            #数据库名：
            db='111',
            user='root',
            passwd='66884747',
            charset='utf8')
        #2建立游标对象
        self.cur = self.conn.cursor()
    def save_b_novel(self,title,cate,author,img_src,intro,chapter_src,last_time,home_src,word_num):
        b_novel ="insert into b_novel(category,title,author,pic,content,tag,serialize,link,create_time,update_time,word)  values(%s,'%s','%s','%s','%s','%s',%s,'%s',%s,%s,%s)"  %(20,title,author,img_src,intro,cate,0,home_src,time.time(),last_time,word_num)
        print(b_novel)
        #执行语句
        self.cur.execute(b_novel)
        #3提交
        self.conn.commit()
    #章节库
    def save_b_chapter(self,title,chapter_title,chapter_content,weigh,chapter_word):
        find_novel_id='select id from b_novel where title="%s"' % title
        self.cur.execute(find_novel_id)
        self.conn.commit()
        novel_id=self.cur.fetchone()[0]
        b_chapter="insert into b_chapter(novel_id,title,content,status,create_time,update_time,weigh,word) values(%s,'%s','%s',%s,%s,%s,%s,%s)" % (novel_id,chapter_title,chapter_content,1,time.time(),time.time(),weigh,chapter_word)
        print(b_chapter)
        #执行语句
        self.cur.execute(b_chapter)
        #3提交
        self.conn.commit()
    #外键库
    def save_b_source(self,title,json):
        find_novel_id = 'select id from b_novel where title="%s"' % title
        self.cur.execute(find_novel_id)
        self.conn.commit()
        novel_id=self.cur.fetchone()[0]
        b_source="insert into b_source(novel_id,reurl,text,create_time,update_time) values (%s,'%s','%s',%s,%s)" %(novel_id,'笔趣阁',json,time.time(),time.time())
        print(b_source)
        self.cur.execute(b_source)
        # 3提交
        self.conn.commit()
        #4关闭游标
        self.cur.close()
        #5关闭数据库连接
        self.conn.close()
    #修改
    #updata_dog='update dog set name="拉布拉多" where id=1'
    #删除
    #delete_dog = 'delete from dog where id=4'
    #查看数据，建立语句
    # select_dog = 'select * from b_chapter where id=1'
    #查看返回值：fetchone()查看第一条，fetchall()查看所有,返回一个元祖
    #print(cur.fetchall())
        #4关闭游标
        #cur.close()
        #5关闭数据库连接
        #conn.close()
        #4关闭游标
        #self.cur.close()
        #5关闭数据库连接
        #self.conn.close()
sql().save_b_novel(title='斗破苍穹',cate='玄幻',author='天蚕土豆',img_src='http://www.com',intro='介绍',chapter_src='章节链接',last_time='8888',home_src='主页链接',word_num=10000)
sql().save_b_chapter(title='斗破苍穹',chapter_title='章节名',chapter_content='章节正文',weigh='88',chapter_word=1000)
sql().save_b_source(title='斗破苍穹',json='[{章节:第一章,章节名:XXX,章节链接:URL}]')