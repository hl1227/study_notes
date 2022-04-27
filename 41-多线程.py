'''

'''
import threading
import time
# def run(str):
#     print('子线程启动',str,threading.current_thread().name)
#     time.sleep(2)
#     print('子线程结束' , str ,threading.current_thread().name)
# if __name__ == '__main__':
#     #任何进程默认会启动一个主线程，可以启动新的子线程
#     #threading.current_thread().name 当前线程的名称
#     print('主线程启动',threading.current_thread().name)
#     #创建子线程：
#     t=threading.Thread(target=run,args=('aaa',))
#     t.start()
#     #主线程等待子线程结束
#     t.join()
#     print('主线程结束', threading.current_thread().name)
#----------多线程数据共享-------------------------------
#因为共享数据
#方法1：创建锁对象
# lock=threading.Lock()
# aa=1000
# def x1(str):
#     global aa
#     for i in range(1000):
#         #上锁
#         lock.acquire()
#         aa=aa+str
#         print(aa)
#         lock.release()
# def x2():
#     global aa
#     for i in range(1000):
#
#         aa -=1
#         print(aa,'-------------')
#
#
# t=threading.Thread(target=x1,args=(1,))
# t.start()
# t2=threading.Thread(target=x2)
# t2.start()
#方法2：建立一个对象：
# local=threading.local()
# #在线程里定义，成为局部变量
# local.aa=aa
#-----延迟线程------------------
# def x3():
#     print('aaa')
#
# t=threading.Timer(3,x3)
# t.start()
#---线程消息队列:----------------------------------
# import queue
# def write(q):
#     print('启动write')
#     for i in range(0,6):
#         #将参数存入q
#         q.put(i)
#         time.sleep(1)
#     print('结束write')
# def read(q):
#     print('启动read')
#     while True:
#         #死循环获取q的参数
#         q1=q.get(True)
#         print(q1)
#     print('结束read')
# if __name__ == '__main__':
#     print('主进程开始')
#     #创建消息队列
#     q=queue.Queue()
#     #将消息队列当作参数
#     p1=threading.Thread(target=write,args=(q,))
#     p2=threading.Thread(target=read,args=(q,))
#     p1.start()
#     p2.start()
#
#     print('主进程结束')
#---------------------线程调度----------------------
#创建线程条件标量
# cond=threading.Condition()
# def a1():
#     with cond:
#         for i in range(0,10,2):
#             print(i,threading.current_thread().name)
#             time.sleep(1)
#             #1执行一条后等到到2
#             cond.wait()
#             #3执行后告诉4
#             cond.notify()
# def a2():
#     with cond:
#         for i in range(1,10,2):
#             print(i,threading.current_thread().name)
#             time.sleep(1)
#             #2执行一条后告诉3
#             cond.notify()
#             #4执行后等到1
#             cond.wait()
# threading.Thread(target=a1).start()
# threading.Thread(target=a2).start()
#多线程+消息队列-------------------------------------------------------------
# from queue import Queue,Empty
# import pymysql,time,threading,random
#
# class test():
#     def __init__(self):
#         # self.conn = pymysql.Connect(
#         #     host='154.212.112.247',
#         #     port=13006,
#         #     # 数据库名：
#         #     db='test',
#         #     user="root",
#         #     passwd='itfkgsbxf3nyw6s1',
#         #     charset='utf8')
#         # self.cur = self.conn.cursor()
#         self.que=Queue()
#     def write_que(self):
#         for num in range(0,1000):
#             self.que.put(num)
#             time.sleep(random.uniform(0, 0.01))
#             print('****')
#     def read_que(self,t_num):
#         while True:
#             try:
#                 start_v=self.que.get(timeout=2)
#                 time.sleep(random.uniform(0,0.2))
#                 print(start_v,t_num)
#                 self.que.task_done()
#             except Empty:
#                 break
#
# if __name__ == '__main__':
#     test=test()
#     t0 = threading.Thread(target=test.write_que)
#     t0.daemon = True
#     t0.start()
#
#     for threading_num in range(0,10):
#         t=threading.Thread(target=test.read_que,args=(threading_num,))
#         t.start()
#         #print('-----')
#         #t.join()
#线程池1-----------------------------------------------------------------------

from concurrent.futures import ThreadPoolExecutor,as_completed
import random
def test(num):
    time.sleep(random.uniform(0,0.1))
    print(num)
    return '-----'+str(num)

if __name__ == '__main__':
    with ThreadPoolExecutor(max_workers=5) as pool:
        res=pool.map(test,[i for i in range(0,10)])
        #pool.shutdown()
        for a in res:
            print(a)
        pool.shutdown()
        print(111)
#线程池2-----------------------------------------------------------------------
# import threadpool
# def test(num):
#     time.sleep(random.uniform(0,0.1))
#     print(num)
#     return '-----'+str(num)
# if __name__ == '__main__':
#     pool = threadpool.ThreadPool(10)
#     requests = threadpool.makeRequests(test, [i for i in range(0,10)])
#     [pool.putRequest(req) for req in requests]
#     pool.wait()

