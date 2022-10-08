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

#生成每天日期
def create_assist_date(datestart=None, dateend=None):
    # 创建日期辅助表
    if datestart is None:
        datestart = '20220101'
    if dateend is None:
        dateend = datetime.datetime.now().strftime('%Y%m%d')

    # 转为日期格式
    datestart = datetime.datetime.strptime(datestart, '%Y%m%d')
    dateend = datetime.datetime.strptime(dateend, '%Y%m%d')
    date_list = []
    date_list.append(datestart.strftime('%Y%m%d'))
    while datestart < dateend:
        # 日期叠加一天
        datestart += datetime.timedelta(days=+7)
        # 日期转字符串存入列表
        date_list.append(datestart.strftime('%Y%m%d'))
    print(date_list)