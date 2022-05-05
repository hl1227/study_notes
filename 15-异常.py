import traceback
try:
    8/0
except Exception as e:#报错运行的代码
    print(e)
    #traceback.print_exc(file=open('./15-log.txt','a+',encoding='utf-8'))#直接打印,并存储
    print(traceback.format_exc())#返回字符串
else:#没报错运行的代码
    print(1)
finally:#都会运行的代码
    print(2)
