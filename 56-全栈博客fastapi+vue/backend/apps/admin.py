from fastapi import APIRouter, Depends, Request, Response

admin = APIRouter()


# 1.1后台主页当前用户
@admin.get('/index/active_user')
def admin_index_active_user():
    return {'code': 200, 'msg': 'ok',
            'data': {'username': 'fjfj1227', 'authority': 'root', 'last_time': '2022-06-10 15:20:00',
                     'nickname': 'Deceiver',
                     'headshot_src': 'https://t7.baidu.com/it/u=2168645659,3174029352&fm=193&f=GIF'}}


# 1.2后台主页表格数据
@admin.get('/index/table_data')
def admin_index_table_data():
    return {'code': 200, 'msg': 'ok', 'data': {'list': [
        {'name': '小明', 'age': 18, 'sex': '男', 'other': '郭文文个火狐韦尔股份'},
        {'name': '小王', 'age': 11, 'sex': '男', 'other': '郭文文个火狐韦尔股份'},
        {'name': '小红', 'age': 12, 'sex': '女', 'other': '郭文文个火狐韦尔股份'},
        {'name': '小红', 'age': 12, 'sex': '女', 'other': '郭文文个火狐韦尔股份'},
        {'name': '小红', 'age': 12, 'sex': '女', 'other': '郭文文个火狐韦尔股份'},
    ], 'count': 5}}


# 1.3后台主页主数据
@admin.get('/index/main_data')
def admin_index_main_data():
    pass


# 1.4后台主页折线图数据
@admin.get('/index/line_chart_data')
def admin_index_line_chart_data():
    return {'code': 200, 'msg': 'ok', 'data': {'xdata': [data for data in range(202201, 202213)],
                                               'ydata': [{'体育数据': 105, '科技数据': 540, '军事数据': 459, '财经数据': 268},
                                                         {'体育数据': 108, '科技数据': 530, '军事数据': 419, '财经数据': 278},
                                                         {'体育数据': 104, '科技数据': 580, '军事数据': 439, '财经数据': 238},
                                                         {'体育数据': 142, '科技数据': 630, '军事数据': 489, '财经数据': 248},
                                                         {'体育数据': 162, '科技数据': 430, '军事数据': 449, '财经数据': 258},
                                                         {'体育数据': 180, '科技数据': 536, '军事数据': 499, '财经数据': 267},
                                                         {'体育数据': 230, '科技数据': 532, '军事数据': 389, '财经数据': 318},
                                                         {'体育数据': 140, '科技数据': 538, '军事数据': 384, '财经数据': 348},
                                                         {'体育数据': 160, '科技数据': 530, '军事数据': 370, '财经数据': 228},
                                                         {'体育数据': 160, '科技数据': 510, '军事数据': 432, '财经数据': 198},
                                                         {'体育数据': 105, '科技数据': 500, '军事数据': 422, '财经数据': 215},
                                                         {'体育数据': 220, '科技数据': 490, '军事数据': 468, '财经数据': 247}]
                                               }
            }


# 1.6后台主页饼状图数据
@admin.get('/index/pie_chart_data')
def admin_index_pie_chart_data():
    return {'code': 200, 'msg': 'ok', 'data': {'pie1': [
        {'name': '体育数据', 'value': 220},
        {'name': '科技数据', 'value': 490},
        {'name': '军事数据', 'value': 468},
        {'name': '财经数据', 'value': 247}]
    }}


# 1.6后台主页柱状图数据
@admin.get('/index/histogram_data')
def admin_index_histogram_data():
    return {'code': 200, 'msg': 'ok', 'data': {'pie2': [
        {'name': 'CPU使用率', 'value': 47},
        {'name': '内存使用率', 'value': 79}
    ]
    }}


@admin.get('/login')
def admin_index():
    return '后台登录页'
