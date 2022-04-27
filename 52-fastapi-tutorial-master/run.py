#!/usr/bin/python3
# -*- coding:utf-8 -*-
# __author__ = '__Jack__'

import time
import uvicorn
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from coronavirus import application
from tutorial import app03, app04, app05, app06, app07, app08,test

# from fastapi.exceptions import RequestValidationError
# from fastapi.responses import PlainTextResponse
# from starlette.exceptions import HTTPException as StarletteHTTPException

'''FastAPI 应用的常见文档配置项'''
app = FastAPI(
    title='FastAPI Tutorial and Coronavirus Tracker API Docs',  #文档标题
    description='FastAPI教程 新冠病毒疫情跟踪器API接口文档，项目代码：https://github.com/liaogx/fastapi-tutorial',  #文档描述
    version='1.0.0',     #文档版本
    docs_url='/docs',    #文档路径
    redoc_url='/redocs', #文档2路径
    responses={200: {"description": "Good job!777"}}       #文档中状态码200的返回description为KEY
    #dependencies=[Depends(verify_token), Depends(verify_key)]   #全局依赖
)

'''FastAPI项目的静态文件配置'''
# mount表示将某个目录下一个完全独立的应用挂载过来，这个不会在API交互文档中显示
app.mount(path='/static', app=StaticFiles(directory='./coronavirus/static'), name='static')  # .mount()不要在分路由APIRouter().mount()调用，模板会报错


# @app.exception_handler(StarletteHTTPException)  # 重写HTTPException异常处理器
# async def http_exception_handler(request, exc): # exc为错误信息
#     """
#     :param request: 这个参数不能省
#     :param exc:
#     :return:
#     """
#     return PlainTextResponse(str(exc.detail), status_code=exc.status_code)
#
#
# @app.exception_handler(RequestValidationError)  # 重写请求验证异常处理器   请求参数不对
# async def validation_exception_handler(request, exc):
#     """
#     :param request: 这个参数不能省
#     :param exc:
#     :return:
#     """
#     return PlainTextResponse(str(exc), status_code=400)

#中间件,拦截http请求
@app.middleware('http')
async def add_process_time_header(request: Request, call_next):  # call_next将接收request请求做为参数
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers['X-Process-Time'] = str(process_time)  # 添加自定义的以“X-”开头的请求头
    return response

#加载中间件
app.add_middleware(
    CORSMiddleware,
    allow_origins=[#信任的域
        "http://127.0.0.1",
        "http://127.0.0.1:8080",'*'
    ],
    allow_credentials=True,#允许的证书
    allow_methods=["*"],   #跨域的请求方法[get,post,put]
    allow_headers=["*"],   #允许的请求头
)

app.include_router(app03, prefix='/chapter03', tags=['第三章 请求参数和验证'])
app.include_router(app04, prefix='/chapter04', tags=['第四章 响应处理和FastAPI配置'])
app.include_router(app05, prefix='/chapter05', tags=['第五章 FastAPI的依赖注入系统'])
app.include_router(app06, prefix='/chapter06', tags=['第六章 安全、认证和授权'])
app.include_router(app07, prefix='/chapter07', tags=['第七章 FastAPI的数据库操作和多应用的目录结构设计'])
app.include_router(app08, prefix='/chapter08', tags=['第八章 中间件、CORS、后台任务、测试用例'])
app.include_router(application, prefix='/coronavirus', tags=['新冠病毒疫情跟踪器API'])
app.include_router(test,prefix='/test',tags=['测试'])



if __name__ == '__main__':
    uvicorn.run('run:app', host='0.0.0.0', port=8001, reload=True, debug=True, workers=1)
#pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple/