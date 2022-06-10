import time
def time_zsq(args):
    if args == 999:
        def inner(func):
            def run(*args,**kwargs):
                s_t=time.time()
                result=func(*args,**kwargs)
                e_t=time.time()
                print(f'用时:{e_t-s_t}')
                return result
            return run
        return inner


@time_zsq(999)
def run(num):
    for i in range(0,num):
        print(i**2)
    return 100

res=run(500)
print(res)