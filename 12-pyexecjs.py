import execjs

#实例化node对象
node=execjs.get()
#Js源文件编译
ctx=node.compile(open('12-pyexecjs.js','r',encoding='utf-8').read())
function_name=f'getPwd("123456")'
#执行JS函数
res=ctx.eval(function_name)
print(res)