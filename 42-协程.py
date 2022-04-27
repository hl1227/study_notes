

#协程：看上去是子程序，但在执行过程中，在子程序的内部可中断，然后转而去执行别的子程序，不是函数调用
#有点类似CPU中断
#看起来是多线程执行，其实是在一个线程里执行
#协程的执行效率极高，因为只有一个线程，不存在变量的冲突，共享资源不需要加锁，只需判断状态
#P是通过generator实现的
def data(c):
    c.send(None)
    for i in range(5):
        print('产生数据：',i)
        r=c.send(str(i))
        print(r)
    c.close()

def run():
    data=''
    while True:
        n=yield data
        if not n:
            return
        print('获取到数据：',n)
        data='200'

c=run()
data(c)