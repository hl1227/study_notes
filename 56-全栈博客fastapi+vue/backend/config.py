

#连接数据库URL
SQLALCHEMY_DATABASE_URL='mysql+pymysql://root:itfkgsbxf3nyw6s1@154.212.112.247:13006/blog_2?charset=utf8mb4'

#主页随机分类个数
INDEX_CATEGORY_COUNT=8
#主页最新数据条数
INDEX_DATA_COUNT=30

#分类页分类个数
CATEGORY_CATEGORY_COUNT=8
#分类页数据条数
CATEGORY_DATA_COUNT=30

#详情页分类个数
INFO_CATEGORY_COUNT=6
#详情页随机数据条数
INFO_RANDOM_DATA_COUNT=4
#详情页其他数据条数
INFO_OTHER_DATA_COUNT=4

#分类页缓存开关 True or False
CATEGORY_CACHE_ENABLED=False
#分类页缓存根文件夹路径
CATEGORY_CACHE_PATH='./cache'


#详情页缓存开关 True or False
INFO_CACHE_ENABLED=False
#详情页缓存根文件夹路径
INFO_CACHE_PATH='./cache'