import asyncio
import aiomysql
#https://pythonav.com/wiki/detail/6/91/#5.2%20%E5%BC%82%E6%AD%A5MySQL

pool = aiomysql.Pool(host='154.212.112.247', port=13006, user='root', password='itfkgsbxf3nyw6s1', db='mysql',
                     minsize=1, maxsize=10, echo=False, pool_recycle=-1, loop=asyncio.get_event_loop())
async def red1(name):
    #申请连接
    async with pool.acquire() as conn:
        #建立连接池
        async with conn.cursor() as cur:
            # 网络IO操作：执行SQL
            await cur.execute("SELECT {} FROM user".format(name))
            # 网络IO操作：获取SQL结果
            result = await cur.fetchall()
            print(result)
            # 网络IO操作：关闭链接
            await cur.close()
        conn.close()

async def red2(name):
    #申请连接
    async with pool.acquire() as conn:
        #建立连接池
        async with conn.cursor() as cur:
            # 网络IO操作：执行SQL
            await cur.execute("SELECT * FROM user")
            # 网络IO操作：获取SQL结果
            result = await cur.fetchall()
            print(result)
            # 网络IO操作：关闭链接
            await cur.close()
        conn.close()

task_list=[red1('Host'),red1('User')]

asyncio.run(asyncio.wait(task_list))

#################################################################
import aiomysql
import asyncio


async def select(loop, sql, pool):
    async with pool.acquire() as conn:
        async with conn.cursor() as cur:
            await cur.execute(sql)
            r = await cur.fetchone()
            print(r)


async def insert(loop, sql, pool):
    async with pool.acquire() as conn:
        async with conn.cursor() as cur:
            await cur.execute(sql)
            await conn.commit()


async def main(loop):
    pool = await aiomysql.create_pool(
        host='127.0.0.1',
        port=3306,
        user='root',
        password='123456',
        db='test',
        loop=loop)
    c1 = select(loop=loop, sql='select * from minifw limit 1', pool=pool)
    c2 = insert(loop=loop, sql="insert into minifw (name) values ('hello')", pool=pool)

    tasks = [asyncio.ensure_future(c1), asyncio.ensure_future(c2)]
    return await asyncio.gather(*tasks)


if __name__ == '__main__':
    cur_loop = asyncio.get_event_loop()
    cur_loop.run_until_complete(main(cur_loop))