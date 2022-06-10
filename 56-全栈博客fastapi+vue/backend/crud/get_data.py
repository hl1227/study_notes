from sqlalchemy.orm import Session
import random,time

def index_data(db:Session,skip=0,limit=10,category=None,source=None):
    #分类页数据
    if category:
        try:
            category_id=db.execute(f"select id from t_category where category = '{category}'").fetchone()[0]
            category_data_list=db.execute(f"select category,title,img_src,source,keyword,description,author,create_time from data  where status=1 and category_id like '%{str(category_id)+','}%' ORDER BY create_time DESC LIMIT {skip*limit},{limit}")
            return list(category_data_list)
        except Exception:
            return []
    #详情页数据
    elif source:
        return list(db.execute(f'select * from data where source = "{source}"'))
    #主页数据
    else:
        return list(db.execute(f'select category,title,img_src,source,keyword,description,author,create_time from data  where status=1 ORDER BY create_time DESC LIMIT {skip},{limit}'))

def get_categorys(db:Session,count:int=1,is_all=False):
    #所有分类
    if is_all:
        category_list = list(db.execute(f"SELECT DISTINCT category FROM t_category"))
    else:
    #随机分类
        category_list=list(db.execute(f"SELECT * FROM `t_category` AS t1 JOIN (SELECT ROUND(RAND() * ((SELECT MAX(id) FROM `t_category`) - (SELECT MIN(id) FROM `t_category`)) + (SELECT MIN(id) FROM `t_category`)) AS id ) AS t2 WHERE t1.id >= t2.id ORDER BY t1.id LIMIT {count}"))
        # max_category_id=db.execute('select max(id) from t_category').fetchone()[0]
        # random_id=random.randint(1,max_category_id-count)
        # category_list=db.execute(f"SELECT category FROM `t_category` where id >= {random_id} and id< {random_id+count+5} LIMIT {count}")
    return category_list

def count_by_category(db:Session,category):
    category_id = db.execute(f"select id from t_category where category = '{category}'").fetchone()[0]
    return int(db.execute(f"SELECT COUNT(id) FROM data where category_id like '%{str(category_id)+','}%' and status=1").fetchone()[0])

# def info_hot_data(db:Session,count=4,category=None):
#     category_id = db.execute(f"select id from t_category where category = '{category}'").fetchone()[0]
#     other_info_data_list = list(db.execute(f"select category,title,img_src,source,keyword,description,author,create_time from data  where status=1 and category_id like '%{str(category_id) + ','}%' ORDER BY RAND() LIMIT {count}"))
#     return other_info_data_list


def info_data(db:Session,count=4,category=None,hot=None):
    # 详情页其他数据
    if category:
        category_id = db.execute(f"select id from t_category where category = '{category}'").fetchone()[0]
        if hot:
            hot_info_data_list = list(db.execute(f"select category,title,img_src,source,keyword,description,author,create_time from data  where status=1 and category_id like '%{str(category_id) + ','}%' LIMIT {count}"))
            return hot_info_data_list
        else:
            other_info_data_list = list(db.execute(f"select category,title,img_src,source,keyword,description,author,create_time from data  where status=1 and category_id like '%{str(category_id)+','}%' ORDER BY RAND() LIMIT {count}"))
            return other_info_data_list
    #详情页\404 随机数据
    else:
        #random_info_data_list = list(db.execute(f"SELECT category,title,img_src,source,keyword,description,author,create_time FROM `data` AS t1 JOIN (SELECT ROUND(RAND() * ((SELECT MAX(id) FROM `data`) - (SELECT MIN(id) FROM `data`)) + (SELECT MIN(id) FROM `data`)) AS id ) AS t2 WHERE t1.id >= t2.id and status =1 ORDER BY t1.id LIMIT {count}"))
        random_info_data_list = list(db.execute(f"SELECT category,title,img_src,source,keyword,description,author,create_time FROM `data`  where status=1 and id >=(SELECT MAX(id) from data)-{random.randint(50,70)}  LIMIT {count}"))
        return random_info_data_list


def random_content(db:Session,count=4,category=None,source=None):
    if category:pass
    else:
        random_content_list=list(db.execute(f"select content from data where id >=(SELECT MAX(id) from data)-{random.randint(5,50)}  LIMIT {count}"))
        return random_content_list



