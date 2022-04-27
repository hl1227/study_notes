# import asyncio
#
# @asyncio.coroutine
# def hello():
#     print("Hello world!")
#     # 异步调用asyncio.sleep(1):
#     r = yield from asyncio.sleep(1)
#     print("Hello again!")
#
# # 获取EventLoop:
# loop = asyncio.get_event_loop()
# # 执行coroutine
# loop.run_until_complete(hello())
# loop.close()
import threading
import asyncio


# @asyncio.coroutine
# def hello():
#     print('Hello world! (%s)' % threading.currentThread())
#     yield from asyncio.sleep(1)
#     print('Hello again! (%s)' % threading.currentThread())
#
# loop = asyncio.get_event_loop()
# tasks = [asyncio.ensure_future(hello()), hello()]
# loop.run_until_complete(asyncio.wait(tasks))
# loop.close()
'---------------------------------------------------------------------------'
# async def func(arg):
#     print(arg)
#     await asyncio.sleep(2)
#     print(arg+100)
#     return '888'
#
# async def main():
#     print('main开始')
#     task_list = []
#     for num in range(3):
#         task_list.append( asyncio.create_task(func(num), name=str(num)))
#
#     print('main结束')
#     done,pending=await asyncio.wait(task_list)
#     print(done)
#     print(pending)
#     for data in done:
#         print(data.result())
# asyncio.run(main())
'---------------------------------------------------------------------------'
import aiohttp
async def fetch(session, url):
    print("发送请求：", url)
    async with session.get(url, verify_ssl=False) as response:
        text = await response.text()
        print("得到结果：", url, len(text))
async def main():
    async with aiohttp.ClientSession() as session:
        url_list = [
            'https://python.org',
            'https://www.baidu.com',
            'https://www.pythonav.com'
        ]
        tasks = [asyncio.create_task(fetch(session, url)) for url in url_list]
        await asyncio.wait(tasks)
if __name__ == '__main__':
    asyncio.run(main())