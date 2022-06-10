from fastapi import APIRouter,Depends,Request,Response

admin = APIRouter()


@admin.get('')
def admin_index():
    return '后台主页'

@admin.get('/login')
def admin_index():
    return '后台登录页'