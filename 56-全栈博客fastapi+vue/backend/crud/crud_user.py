from sqlalchemy.orm import Session
import random

def sql_userdata(db:Session,username,password_hx):
    sql_userdata=db.execute(f"select * from user where username='{username}' and password_hx='{password_hx}'").fetchone()
    if not sql_userdata:
        return None
    return sql_userdata
