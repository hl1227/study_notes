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


####################################
import csv,os
class Save_Csv():
    def __init__(self,csv_name,fieldnames):
        if os.path.exists(csv_name):
            os.remove(csv_name)
        self.f=open(csv_name, 'w+', newline='',encoding='utf-8')
        self.csv_file = csv.DictWriter(self.f, fieldnames=fieldnames)
        self.csv_file.writeheader()

    def save_data(self,data):
        self.csv_file.writerow(data)
        self.f.flush()
    def save_close(self):
        self.f.close()
####################################
import openpyxl,traceback
class Save_Xlsx():
    def __init__(self):
        self.wb = openpyxl.Workbook()
        self.sht = self.wb.active
    def write_excel(self,row:list):
        self.sht.append(row)

    def save_excel(self,excel_name):
        try:
            self.wb.save(excel_name)
            print(f"获取完成:'{excel_name}'")
        except Exception:
            print(f'{traceback.format_exc()}\n文件保存失败:可能在其他地方打开了文件:{excel_name}')
s_xlsx = Save_Xlsx()
s_xlsx.write_excel([1,2,3])
s_xlsx.save_excel('xxx.xlsx')