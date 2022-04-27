#coding=utf-8
str ='PhoneOSNew=2&VerSion=5.4.0.3&a=GetZsTrend_Narrow&apiv=w29&c=StockL2Data'
str_list = str.split(';')

cookies={}
for item in str_list:
    key=item.split('=')[0].strip()
    value=item.split('=')[1].strip()
    cookies[key]=value
print(cookies)



#selenium:
# c_l=[]
# for item in str_list:
#     d={'name':item.split('=')[0].strip(),'value':item.split('=')[1].strip(),'domain':'https://www.tianyancha.com/'}
#     c_l.append(d)
# print(c_l)