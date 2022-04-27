import pymongo
#连接mongod本地的服务
mongo_py=pymongo.MongoClient()

#建立新数据库
db=mongo_py['huliang']

#建立表
biao = db['shiyan']

#建立数据：
# a= {"name":'张三','age':50},
b=[{"name":'张三','age':50},
   {"name":'李四','age':51},
   {"name":'王五','age':48}]

#给表插入一个数据：
#biao.insert_one(a)

#插入多个
biao.insert_many(b)

#删除一个：
biao.delete_one({"name":'王五'})
#删除多个：
biao.delete_many({"name":'王五'})

#修改一个
biao.update({"name":'李四'},{'$set':{"name":'王五五'}})
#修改多个
biao.update_many({"name":'李四'},{'$set':{"name":'王五五'}})

#查询：
data = biao.find()
for i in data:
    print(i)
#关闭数据库
mongo_py.close()
