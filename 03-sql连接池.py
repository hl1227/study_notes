from sqlalchemy.orm import sessionmaker,scoped_session
from sqlalchemy import create_engine
from threading import Thread
import time


engine = create_engine(
        #url=f'mysql+pymysql://root:66884747@127.0.0.1:3306/fastapi_blog?charset=utf8',
        url=f'mysql+pymysql://root:itfkgsbxf3nyw6s1@154.212.112.247:13006/test?charset=utf8',
        max_overflow=0,  # 超过连接池大小外最多创建的连接
        pool_size=10,  # 连接池大小
        pool_timeout=100,  # 池中没有线程最多等待的时间，否则报错
        pool_recycle=-1  # 多久之后对线程池中的线程进行一次连接的回收（重置）
    )
SessionFactory = sessionmaker(bind=engine)
session = scoped_session(SessionFactory)


def task(sql):

    # 方式一：
    # 查询
    cursor = session.execute(sql)
    result = cursor.fetchall()

    # 方式二：
    # conn = engine.raw_connection()
    # cursor = conn.cursor()
    # cursor.execute(
    #     "select * from t1"
    # )
    # result = cursor.fetchall()
    # cursor.close()
    # conn.close()

    # 将连接交还给连接池
    session.remove()
    return result
def sql_insert(sql,params):
    # 添加
    try:
        cursor = session.execute(sql, params=params)
        session.commit()
        session.remove()
        time.sleep(0.1)
        print(cursor.lastrowid)
    except Exception:
        session.rollback()
        session.ping()
def main():
    #print(task(sql="select https from spider_proxy where id = 1"))

    sql="insert into hy_cn_test(title,url) values(:title,:url)"
    params={'title':'aaa','url':'bbb'}
    sql_insert(sql,params)
if __name__ == '__main__':
    for i in range(3):
        t = Thread(target=main)
        t.start()
        t.join()