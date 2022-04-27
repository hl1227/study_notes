from multiprocessing import Process
from time import sleep
import os

# def run(str):
#     #os.getpid()获取当前进程ID
#     print('子进程开始',str,os.getpid())
#     sleep(3)
#     print('子进程结束',str,os.getpid())
# def yes(str):
#     print('子进程开始', str, os.getpid())
#     sleep(3)
#     print('子进程结束', str, os.getpid())
#----------进程-------------------------------------------------
# if __name__ == '__main__':
#     #直接运行的程序叫做主进程
#     print('主进程启动')
#     #创建子进程(子进程和主进程会同时运行，互不影响干涉,包括全局变量)
#     #target的值是要执行的任务，args是传参
#     p=Process(target=run,args=('111',))
#     y=Process(target=yes,args=('444',))
#     p.start()
#     y.start()
#     #让子进程先结束，再结束主进程
#     p.join()
#     print('bbbb',os.getpid())
#     sleep(1)
#-------------进程池---------------------------------------
# from multiprocessing import Pool
#
# if __name__ == '__main__':
#     print('主进程启动')
#     #创建进程池，Pool()默认是cpu的核心数，可以自己改变，核心=同时执行几个子进程
#     pp=Pool(2)
#     for i in range(0,6):
#         #将子进程加入到线程池统一管理运行
#         pp.apply_async(run,args=(i,))
#     #线程池要先结束得先关闭
#     pp.close()
#     pp.join()
#
#     print('主进程结束')
#-------------进程间通讯（消息队列）---------------------------------------
# from multiprocessing import Queue
# def write(q):
#     print('启动write',os.getpid())
#     for i in range(0,6):
#         #将参数存入q
#         q.put(i)
#         sleep(1)
#     print('结束write', os.getpid())
# def read(q):
#     print('启动read', os.getpid())
#     while True:
#         #死循环获取q的参数
#         q1=q.get(True)
#         print(q1)
#     print('结束read', os.getpid())
# if __name__ == '__main__':
#     print('主进程开始')
#     #创建消息队列
#     q=Queue()
#     #将消息队列当作参数
#     p1=Process(target=write,args=(q,))
#     p2=Process(target=read,args=(q,))
#     p1.start()
#     p2.start()
#     p1.join()
#     #p2进程是个死循环，只能强行结束：当其他进程结束后再结束
#     p2.terminate()
#     print('主进程结束')
#---------进程池------------------------------------------------------------
#from multiprocessing.dummy import Pool
import time,random
from multiprocessing import Pool

def test(num):
    time.sleep(random.uniform(0,0.1))
    print(num)

if __name__ == '__main__':
    pool=Pool(4)
    num_list=[]
    for num in range(1,1001):
        num_list.append(num)
    pool.map_async(test,num_list)
    pool.close()
    pool.join()


