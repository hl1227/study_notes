import datetime,time

#生成时间计数
a=datetime.timedelta(days=1, seconds=1, microseconds=0, milliseconds=0, minutes=0, hours=5, weeks=2)
print(a)


now=datetime.datetime.now()
print(now)

#时间计算
now_1day=now-datetime.timedelta(days=1)#减一天
print(now_1day)

now_x=now+a #增加指定天数
print(now_x)

#时间转字符串
now_str=now.strftime('%Y-%m-%d %H:%M:%S')
print(now_str,type(now_str))

#字符串转时间
now=datetime.datetime.strptime(now_str,'%Y-%m-%d %H:%M:%S')
print(now,type(now))

#时间戳转字符串日期
t2=time.localtime(time.time())
t3=time.strftime("%Y-%m-%d %H:%M:%S",t2)
print(t3,type(t3))

#字符串日期转时间戳
t=time.mktime(time.strptime(now_str,'%Y-%m-%d %H:%M:%S'))
print(t,type(t))