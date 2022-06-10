from fastapi import APIRouter,Depends,Request,Response
from fastapi.responses import RedirectResponse,HTMLResponse
from fastapi.templating import Jinja2Templates
from db.session import SessionLocal
from crud import get_data
import config,datetime,os,random



application = APIRouter()

templates = Jinja2Templates(directory='./templates')



def view_404(request,db,request_path=None):
    category_list = get_data.get_categorys(db, count=50)
    random_content_list=get_data.random_content(db,count=2)
    random_info_data_list = get_data.info_data(db, count=20)
    host = request.headers.get("host")
    return templates.TemplateResponse('404.html', status_code=200, context={"request": request,'data':{
        'category_list':category_list,
        'random_content_list':random_content_list,
        'random_info_data_list':random_info_data_list,
        'host':host,
        'request_path':request_path
    }})


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
#----------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------
@application.get('/favicon.ico')
def favicon():
    return None


@application.get('/robots.txt')
def robots():
    f = open('./static/robots.txt', 'r')
    content = f.read()
    f.close()
    return Response(content,status_code=200)
    #return RedirectResponse('/static/robots.txt',status_code=200)

@application.get('/googleafaaa78b6629b35a.html')
def googleafaaa():
    f=open('./static/googleafaaa78b6629b35a.html','rb')
    content = f.read()
    f.close()
    return HTMLResponse(content=content, status_code=200)


#站点地图
@application.get('/sitemap.xml')
def sitemap(request:Request,db=Depends(get_db)):
    #request.client.host
    domain='https://{}/'.format(request.headers.get("host"))
    res_1='''
        <urlset
        xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
        xsi:schemaLocation="http://www.sitemaps.org/schemas/sitemap/0.9
        http://www.sitemaps.org/schemas/sitemap/0.9/sitemap.xsd">'''
    res_list=['']
    category_list=get_data.get_categorys(db,is_all=True)
    data_list = get_data.index_data(db, 0, 1000)
    date = datetime.datetime.now()
    for category in category_list:
        res_list.append(category.category.replace(' ','-'))
    for data in data_list:
        res_list.append(data.category.replace(' ','-')+'/'+data.source)
    for res in res_list:
        res_1+='<url><loc>{}</loc >'.format(domain+res)
        res_1+='<lastmod>{}</lastmod>'.format(date.strftime("%Y-%m-%d"))
        res_1+='<changefreq>always</changefreq>'
        res_1+='<priority>1.0</priority></url>'
    res_1+='</urlset>'
    return Response(content=res_1,media_type='application/xml')

#主页
@application.get('/')
def index(request:Request,db=Depends(get_db)):
    category_list = get_data.get_categorys(db, count=config.INDEX_CATEGORY_COUNT)
    index_data_list=get_data.index_data(db,0,config.INDEX_DATA_COUNT)
    # 增加十条随机数据,再随机取
    index_data_list = index_data_list + get_data.info_data(db, count=10)
    index_data_list = random.sample(index_data_list, config.INDEX_DATA_COUNT)
    #######################
    host = request.headers.get("host")
    return templates.TemplateResponse(
        'index.html',{
            "request": request,
            'code':200,
            'msg':'成功',
            'data':{'index_data_list':index_data_list,'category_list':category_list,'host':host,'time':datetime.datetime.now().strftime("%Y-%m-%d")}
        })
#分类页
@application.get('/{category}')
def category(request:Request,category:str,page:int=1,count:int=config.CATEGORY_DATA_COUNT,db=Depends(get_db)):
    if page==0:
        return view_404(request,db,category)
    host = request.headers.get("host")
    if '127.0.0.1' in host:
        host = '127.0.0.1'
    category = category.replace('-', ' ')
    category_f_path = f'{config.CATEGORY_CACHE_PATH}/{host}/{category}'
    if config.CATEGORY_CACHE_ENABLED and os.path.exists(f'{category_f_path}/{category}.html'):
        # 返回缓存
        f = open(f'{category_f_path}/{category}.html', 'rb')
        content = f.read()
        f.close()
        return HTMLResponse(content=content, status_code=200)
    else:
        category_data_list = get_data.index_data(db,page-1,count,category)
        if len(category_data_list)<1 :
            return view_404(request,db,category.replace(' ', '-'))
        # 增加十条随机数据,再随机取
        # category_data_list = category_data_list + get_data.info_data(db, count=10)
        # category_data_list = random.sample(category_data_list, count)
        ########################
        category_list = get_data.get_categorys(db, count=config.CATEGORY_CATEGORY_COUNT)
        max_page=get_data.count_by_category(db,category)//count+1
        category_res =templates.TemplateResponse(
            'category.html', {
                "request": request,
                'code':200,
                'msg':'成功',
                'data':{'category_data_list':category_data_list,'category':category,
                        'category_list':category_list,'page':page,'max_page':max_page,
                        'host':host,'time':datetime.datetime.now().strftime("%Y-%m-%d")}
            })
        if config.CATEGORY_CACHE_ENABLED:
            #存缓存
            if not os.path.exists(category_f_path):
                os.makedirs(category_f_path)
            file_cache_category = open(f'{category_f_path}/{category}.html', 'w+', encoding='utf-8')
            file_cache_category.write(category_res.body.decode('utf-8'))
            file_cache_category.close()
        return category_res
#详情页
@application.get('/{category}/{source}')
def info(request:Request,category,source,db=Depends(get_db)):
    host = request.headers.get("host")
    if '127.0.0.1' in host:
        host = '127.0.0.1'
    category = category.replace('-', ' ')
    info_f_path = f'{config.INFO_CACHE_PATH}/{host}/{category}'
    if config.INFO_CACHE_ENABLED and os.path.exists(f'{info_f_path}/{source}.html'):
        # 返回缓存
        f = open(f'{info_f_path}/{source}.html', 'rb')
        content = f.read()
        f.close()
        return HTMLResponse(content=content, status_code=200)
    else:
        one_info_data_list =get_data.index_data(db,0,1,source=source)
        if len(one_info_data_list)<1:
            request_path=category+'-'+source
            return view_404(request,db,request_path)
        # 打乱正文
        content_list = one_info_data_list[0].content.split(' ')
        median = len(content_list) // 2
        shuffle = content_list[median:]
        random.shuffle(shuffle)
        shuffle_content = ' '.join(content_list[0:median] + shuffle)
        random_content=get_data.random_content(db,count=1)[0].content
        # ------------------------------------------
        category_list = get_data.get_categorys(db, count=config.INFO_CATEGORY_COUNT)
        random_info_data_list=get_data.info_data(db,count=config.INFO_RANDOM_DATA_COUNT)
        other_info_data_list=get_data.info_data(db,count=config.INFO_OTHER_DATA_COUNT,category=category.replace('-',' '))
        hot_info_data_list=get_data.info_data(db,count=config.INFO_OTHER_DATA_COUNT,category=category.replace('-',' '),hot=True)
        info_res =templates.TemplateResponse(
            'info.html', {
                "request": request,
                'code':200,
                'msg':'成功',
                'data':{'one_info_data_list':one_info_data_list,
                        'category':category,'category_list':category_list,
                        'random_info_data_list':random_info_data_list,'other_info_data_list':other_info_data_list,'hot_info_data_list':hot_info_data_list,
                        'host':host,'shuffle_content':shuffle_content,'random_content':random_content}
            })
        if config.INFO_CACHE_ENABLED:
            # 存缓存
            try:
                if not os.path.exists(info_f_path):
                    os.makedirs(info_f_path)
                file_cache_category = open(f'{info_f_path}/{source}.html', 'w+', encoding='utf-8')
                file_cache_category.write(info_res.body.decode('utf-8'))
                file_cache_category.close()
            except Exception as e:
                print(f'缓存创建失败:{category}/{source},信息:{e}')
        return info_res
