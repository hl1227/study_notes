# 博客网站生成器2.0(多分类版)

## 1.简介:
		语言:Python3.9
		框架:FastApi
		服务:uvicorn
		数据库:Sqlalchemy+Mysql
		前端模板引擎:jinja2

## 2.功能:
		根据数据库字段自动生成主页/分类页/详情页,并且每条数据属于多个分类
            本地缓存机制:
                1.根据域名自动生成本地缓存文件
                
#### 2.1 主页:
		1.路径:'/'
		2.分类对象:返回随机获取数据库t_category.category字段作为分类
		3.数据对象:返回最新数据+随机数据
#### 2.2 分类页:
		1.路径:'/{category}?page=1'
		2.分类对象:返回随机获取数据库t_category.category字段作为分类
		3.数据对象:返回该分类最新数据+随机数据
		4.翻页对象:返回当前页数及最大页数
#### 2.3 详情页
		1.路径:'/{category}/{source}'
		2.分类对象:返回随机获取数据库t_category.category字段作为分类
		3.数据对象:根据source返回一条数据
		4.随机数据对象:随机返回几条数据
        5.其他数据对象:随机返回几条当前分类的其他数据
## 3.准备:
### 3.1 安装依赖
```		
	pip install -r requirements.txt
```
### 3.2 修改配置文件(数据库配置,数据条数配置)
		config.py 

### 3.3 准备数据库
        根据配置创建blog_2.sql数据库
        注意:表中keyword字段作为网站分类,分类种类至少需要配置的条数以上才能运行,否则报错!

## 4.运行:
		
```
	python main.py
```

## 5.jinja2前端模板引擎基础: 
参考:http://doc.yonyoucloud.com/doc/jinja2-docs-cn/index.html
#### 5.1 语法
###### 5.11 遍历语法:(遍历:依次取出列表的每一条数据)
```
    <ul>
      {% for 单个数据名 in 数据字段_list %}
        <li>
          {{ 单个数据名.属性 }}
        </li>
      {% endfor %}
    </ul>
```
或者取列表的前5个:(第一个以0开始)
```
    <ul>
      {% for 单个数据名 in 数据字段_list[0:5] %}
        <li>
          {{ 单个数据名.属性 }}
        </li>
      {% endfor %}
    </ul>
```
或者取列表的第5个:(第一个以0开始,并保证列表里有5个数据,否则报错)
```
    <ul>
        <li>
          {{ 数据字段_list.4.属性 }}
        </li>
    </ul>
```
###### 5.12 过滤器用法:
```HTML
		{{  单个数据名.属性 | 过滤器方法() }}
		<a href="/{{ category.keyword  | replace(' ','-')}}">{{ category.keyword }}</a>
```
###### 5.13 if语句及运算语句:
```HTML
		{% if 单个数据名.属性 >=18 %}
			<p>你已满18岁 {{ 单个数据名.属性-18 }}年</p>
		{% elif 单个数据名.属性 < 18 %}
			<p>你还差{{ 18-单个数据名.属性 }}年满18岁</p>
		{% else %}
			<p>pass</p>
		{% endif %}
```
## 6.页面字段及属性

#### 6.1 主页:(详见:./templates/index.html)
###### 6.11 主页分类字段:
	1.字段名: data.category_list
	2.类型:列表 
	3.遍历后属性:
		关键字(分类):  单个数据名.category    
###### 6.11 主页数据字段:
	1.字段名: data.index_data_list
	2.类型:列表 
	3.遍历后属性:
        标题:        单个数据名.title
        图片链接:     单个数据名.img_src
        source:      单个数据名.source
        关键字:       单个数据名.keyword
        描述:         单个数据名.description
        作者:         单个数据名.author
        分类:         单个数据名.category
        发布日期:     单个数据名.create_time
###### 6.12 主页时间字段:
    1.字段名: data.time
	2.类型:字符串
    3.解释:获取当前日期 格式:2020-01-01

#### 6.2 分类页:(详见:./templates/category.html)
###### 6.21 分类页面包屑字段:
	1.字段名: data.category
	2.类型:字符串
	3.解释:用于面包屑当前分类
###### 6.22 分类页分类字段:
	1.字段名: data.category_list
	2.类型:列表 
	3.遍历后属性:
        关键字(用于分类):  单个数据名.category    
###### 6.23 分类页数据字段:
	1.字段名: data.category_data_list
	2.类型:列表 
	3.遍历后属性:
        标题:        单个数据名.title
        图片链接:     单个数据名.img_src
        source:      单个数据名.source
        关键字:       单个数据名.keyword
        描述:         单个数据名.description
        作者:         单个数据名.author
        分类:         单个数据名.category
        发布日期:     单个数据名.create_time
    **分类页数据的URL分类应该为:/{{data.category}}/{{单个数据名.source}}
###### 6.24 分类页翻页字段:
		1.字段名: data.page
		2.类型:整数
		3.解释:用于当前分类第几页
----------------------------------
		1.字段名: data.max_page
		2.类型:整数
		3.解释:用于当前分类最大页数
###### 6.25 分类页时间字段:
            1.字段名: data.time
            2.类型:字符串
            3.解释:获取当前日期 格式:2020-01-01
#### 6.3 详情页:(详见:./templates/info.html)
###### 6.31 详情页面包屑字段:
		1.字段名:data.category
		2.类型:字符串
		3.解释:用于面包屑当前分类
###### 6.31 详情页分类字段:
	1.字段名: data.category_list
	2.类型:列表 
	3.遍历后属性:
		关键字(分类):  单个数据名.category 

###### 6.32 详情页数据字段:
	1.字段名: data.one_info_data_list
	2.类型:列表 
	3.遍历后属性:
        标题:        单个数据名.title
        图片链接:     单个数据名.img_src
        source:      单个数据名.source
        关键字:       单个数据名.keyword
        描述:         单个数据名.description
        作者:         单个数据名.author
        分类:         单个数据名.category
        发布日期:     单个数据名.create_time
        正文:        单个数据名.content
        打乱正文:     data.shuffle_content
        随机正文:     data.random_content
		
###### 6.33 详情页随机数据字段:
	1.字段名: data.random_info_data_list
	2.类型:列表 
	3.遍历后属性:
        标题:        单个数据名.title
        图片链接:     单个数据名.img_src
        source:      单个数据名.source
        关键字:       单个数据名.keyword
        描述:         单个数据名.description
        作者:         单个数据名.author
        分类:         单个数据名.category
        发布日期:     单个数据名.create_time
		
###### 6.34 详情页同分类的其他数据字段:
	1.字段名: data.other_info_data_list
	2.类型:列表 
	3.遍历后属性:
        标题:        单个数据名.title
        图片链接:     单个数据名.img_src
        source:      单个数据名.source
        关键字:       单个数据名.keyword
        描述:         单个数据名.description
        作者:         单个数据名.author
        分类:         单个数据名.category
        发布日期:     单个数据名.create_time

###### 6.35 详情页同分类的热门数据字段:
	1.字段名: data.hot_info_data_list
	2.类型:列表 
	3.遍历后属性:
        标题:        单个数据名.title
        图片链接:     单个数据名.img_src
        source:      单个数据名.source
        关键字:       单个数据名.keyword
        描述:         单个数据名.description
        作者:         单个数据名.author
        分类:         单个数据名.category
        发布日期:     单个数据名.create_time
	