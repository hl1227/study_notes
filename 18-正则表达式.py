import re
#正则表达式，规则处理字符串（文本）

#1.转译字符:\(表示接下来是使用表达式)
str1 = "a\drt"
pattern = re.compile("a\b")
#.findall返回的是一个列表
re_1 = pattern.findall(str1)
print(re_1)

#3.表达式符号“.”,表示匹配除了换行符以外的，*表示任意次
str2 = """msegsgegfe12n
          egregergre12N"""
#表示截取m到n之间 除了换行符意外的多个字符,
#在后面加上re.S，就会匹配换行符，
#后面加上|re.I，可以不区分大小写
pattern = re.compile("^ms(.*)n$",re.S|re.I)
re_2 = pattern.findall(str2)
print(re_2)

print(re.findall("^ms(.*)n$",str2,re.S|re.I))
#4纯数字正则：\d 表示0-9之间的一个数,不能是字符串
#5：^表示从头开始，$表示结尾，*表示任意次
str3 = "1234563"
pattern=re.compile("^\d*$")
#match返回的是一个对象，需要转译
re_3 = pattern.match(str3)
print(re_3.group())

#正则范围运算:
# [ab12]寻找a和b和1和2的全部
str4 = "cacbc1c2ca"
pattern = re.compile("[ab12]")
re_4 = pattern.findall(str4)
print(re_4)

#[1-6]，寻找1-6的数字
str5 = "0159602"
pattern = re.compile("[1-6]")
re_5 = pattern.findall(str5)
print(re_5)

#匹配中文”
str6 = "abcd123嘿哈哈嘿,如果六年"
print(re.findall(("[\u4e00-\u9fa5]+"),str6))