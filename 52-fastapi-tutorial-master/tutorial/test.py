from fastapi import APIRouter,Depends, status, HTTPException
# from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
# from typing import Optional
# from pydantic import BaseModel
#
test=APIRouter()
# oauth2_schema = OAuth2PasswordBearer(tokenUrl="/test/token")  # 请求Token的URL地址 http://127.0.0.1:8000/chapter06/token
#
# @test.get("/oauth2_password_bearer")
# async def oauth2_password_bearer(token: str = Depends(oauth2_schema)):
#     print(token)
#     return {"token": token}
#
# fake_users_db = {
#     "john snow": {
#         "username": "john snow",
#         "full_name": "John Snow",
#         "email": "johnsnow@example.com",
#         "hashed_password": "fakehashedsecret",
#         "disabled": False,
#     },
#     "alice": {
#         "username": "alice",
#         "full_name": "Alice Wonderson",
#         "email": "alice@example.com",
#         "hashed_password": "fakehashedsecret2",
#         "disabled": True,
#     },
# }
#
#
# def fake_hash_password(password: str):
#     return "fakehashed" + password
#
#
# class User(BaseModel):
#     username: str
#     email: Optional[str] = None
#     full_name: Optional[str] = None
#     disabled: Optional[bool] = None
#
#
# class UserInDB(User):
#     hashed_password: str
#
#
# @test.post("/token")
# async def login(form_data: OAuth2PasswordRequestForm = Depends()):
#     print('---',form_data.username)
#     #user_dict = fake_users_db.get(form_data.username)
#     # if not user_dict:
#     #     raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Incorrect username or password")
#     #user = UserInDB(**user_dict)
#     # hashed_password = fake_hash_password(form_data.password)
#     # if not hashed_password == user.hashed_password:
#     #     raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Incorrect username or password")
#     return {"access_token":'888', "token_type": "bearer"}


# 加密
from passlib.context import CryptContext
import passlib.hash
pwd_context=CryptContext(schemes=["bcrypt"], deprecated="auto")
res=pwd_context.hash('21232f297a57a5a743894a0e4a801fc3')
print(res)
res=pwd_context.hash('secret')
print(res)
res=pwd_context.hash('secret')
print(res)
print(pwd_context.verify('secret',res ))
print(passlib.hash)
import datetime,time
# datetime.fromtimestamp(time.time())
# import requests
# a=requests.get('http://coronavirus-tracker-api.herokuapp.com/v2/locations?source=jhu&country_code=CN&timelines=false').text
# print(a)