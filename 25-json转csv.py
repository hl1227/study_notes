import json
import csv
#csv:将数据转换成表格形式
#需求：json中的数据 转换成csv文件

#1,读取文件
json_fp=open('24-listjson.json','r')


#2，指定表头，表内容
#将json转换成列表
data_list = json.load(json_fp)
print(data_list)
#取列表的第0个值为keys
title = data_list[0].keys()
print(type(title))
#取列表的所有values
sheet_data = []
for data in data_list:
    sheet_data.append(data.values())
print(sheet_data)

#3 csv写入器
writer = csv.writer(open('25-csv.csv','w'))
#4 指定表头
writer.writerow(title)
#5 指定表内容
writer.writerows(sheet_data)
