import re

one = "1a2%b3c"
result = re.compile("\d+")

#match   从头匹配，匹配一次，如果头部不是数字，就返回NONE
str1 = result.match(one)
print(str1.group())

#search 从任意位置开始，匹配一次
print(re.compile(".*").match(one).group())

#findall查找符合正则的内容,返回list
print(re.findall("\d+",one))

#sub 替换字符串,把数字替换成%号
print(re.compile("\d+").sub("%",one))

#split  拆分,以%号为基础 拆分字符串
print(re.compile("%").split(one))


#要匹配中文，首先在网上查看中文的unicode范围为：
#  \u4e00-\u9fa5

str = "erhgrehgr你好，网页，网站"
#+号意思是至少匹配成功一次的意思

print(re.findall(("[\u4e00-\u9fa5]+"),str))

a='https://www.eonline.com/news/page/{page}'
print(re.compile("(http|https)://(www.)?(\w+(\.)?)+").match(a).group())