#json是一种数据交互格式
#整个文件有且仅有一个{}或者【】
#里面不能写注释，key:value：必须是双引号，最后一个不能写逗号
import json
{
    "name":"张三",
    "age":18
}


#1字符串和dict  list转换
data = '[{"name":"张三","age":"18"},{"name":"李四","age":"20"}]'
list_data = json.loads(data)
print(list_data)

#2 dict list 转 字符串：
data2 = [{"name":"张三","age":"18"},{"name":"李四","age":"20"}]
str_data2 = json.dumps(data2,ensure_ascii=False)
print(str_data2)

#3 dict list 写入文件：
list2 = [{"name":"张三","age":"18"},{"name":"李四","age":"20"}]
json.dump(list2,open('24-listjson.json','w'))

#4 读取:json文件---list  dict
fp = json.load(open('24-listjson.json','r'))
print(fp)
