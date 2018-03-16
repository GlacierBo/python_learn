[TOC]

## python 学习笔记

```shell
# -*- coding:utf-8 -*-
```

### 通用序列操作

#### 索引

```python
>>> greeting = 'chongshi'
>>> greeting[0]
'c'
>>> greeting[2]
'o'
```

```python
## 使用负数索引
>>> greeting = 'chongshi'
>>> greeting[-1]
'i'
>>> greeting[-2]
'h'
```

#### 字典

``` python
# 不用字典
brand = ['李宁','耐克','阿迪达斯']
slogan = ['一切皆有可能','Just do it','Impossible is nothing'] 
print('李宁的口号是：',slogan[brand.index('李宁')])
```

``` python
# 字典是映射类型
dict = {'李宁':'一切皆有可能','耐克':'Just do it','阿迪达斯':'Impossible is nothing'}
print('李宁的口号是：',dict['李宁'])
```

 ``` python
>>> dict = {}
>>> dict.fromkeys((1,2,3))
{1: None, 2: None, 3: None}

>>> dict = dict.fromkeys(range(32),"赞")
 ```

#### 分片

```python
>>> tag = '<a href="http://www.python.org">Python web site</a>'
>>> tag[9:30]   # 取第9个到第30个之间的字符
'http://www.python.org'
>>> tag[32:-4]   #取第32到第-4（倒着数第4个字符）
'Python web site'
>>>
```

```python
>>> numbers = [0,1,2,3,4,5,6,7,8,9]
>>> numbers[7:-1]   # 从第7个数到 倒数第一个数
[7, 8]              #显然这样不可行
>>> numbers[7:10]   #从第7个数到第10个数
[7, 8, 9]            #这样可行，索引10指向的是第11个元素。
>>> numbers[7:]    # 可以置空最后一个索引解决
[7, 8, 9]
>>> numbers[:3]   
[0, 1, 2]
>>> numbers[:]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

### 列表

#### 将字符串拆分成列表

list 函数可以将一个字符串拆分成列表

```shell
>>> list('chongshi')
['c', 'h', 'o', 'n', 'g', 's', 'h', 'i']
```

#### 删除元素

```shell
>>> names = ['zhangsan','lisi','wangwu','sunliu']
>>> del names[2]
>>> names
['zhangsan', 'lisi', 'sunliu']
```

#### 分片赋值(这个厉害了)

```shell
>>> name = list('huzi')
>>> name
['h', 'u', 'z', 'i']
>>> name[2:]=list('dazhi')
>>> name
['h', 'u', 'd', 'a', 'z', 'h', 'i']
```

### Python连接Mysql

#### 基础版SQL

```python
#coding=utf-8
import MySQLdb

# Connect() 方法用于创建数据库的连接，里面可以指定参数：用户名，密码，主机等信息。
# 这只是连接到了数据库，要想操作数据库需要创建游标。
conn= MySQLdb.connect(
        host='localhost',
        port = 3306,
        user='root',
        passwd='123456',
        db ='test',
        )

# 通过获取到的数据库连接conn下的cursor()方法来创建游标。
cur = conn.cursor()

#创建数据表
cur.execute("create table student(id int ,name varchar(20),class varchar(30),age varchar(10))")

#插入一条数据
cur.execute("insert into student values('2','Tom','3 year 2 class','9')")

#修改查询条件的数据
cur.execute("update student set class='3 year 1 class' where name = 'Tom'")

#删除查询条件的数据
cur.execute("delete from student where age='9'")

# 关闭游标
cur.close()
# 关闭事物
conn.commit()
# 关闭连接
conn.close()
```

#### 进阶版SQL

```python
#插入一条数据
sqli="insert into student values(%s,%s,%s,%s)"
cur.execute(sqli,('3','Huhu','2 year 1 class','7'))

# 一次插入多条数据   executemany()方法可以一次插入多条值，返回值为受影响的行数
sqli = "insert into student values(%s,%s,%s,%s)"
cur.executemany(sqli,[
    ('3','Tom','1 year 1 class','6'),
    ('3','Jack','2 year 1 class','7'),
    ('3','Yaheng','2 year 2 class','7'),])
```

#### 遍历查询出来的数据

fetchone() 方法可以帮助我们获得表中的数据，可是每次执行cur.fetchone() 游标会从表中的当前数据位置移动到下一条数据的位置

scroll(0,'absolute') 方法可以将游标定位到表中的第一条数据。

```python
# 这个方法只能查询出数据有几条
aa = cur.execute("select * from student")
print(aa)

# fetchmany() 方法获取到数据
info = cur.fetchmany(aa)

# 通过for循环打印出来
for ii in info:
    print(ii)
```

### 模块化

#### 引入模块

```python
## hello.py

def hello():
    print "hello world !"
    
def test():
    hello()

if __name__=='__main__':test()
    
## f __name__ == '__nain__' 解释：
## python文件的后缀为.py ，.py文件可以用来直接运行，就像一个独立的小程序；也可以用来作为模块被其它程序调用。
## __name__是模块的内置属性，如果等于'__main__' 侧表示直接被使用，那么将执行方法test()方法；如果是被调用则不执行 if 判断后面的test()方法。
```

```python
## test.py

import hello
hello.hello()
```

#### time模块

```python
## 引入模块
import  time
aa = time.asctime()
print aa
```

#### random模块

```python
## 引入模块
from random import *
from time import  *

data1 = (2013 ,1,1,0,0,0,-1,-1,-1)
time1 = mktime(data1)
data2 = (2014 ,1,1,0,0,0,-1,-1,-1)
time2 = mktime(data2)

random_time = uniform(time1,time2)
print asctime(localtime(random_time))
```

#### MuduleDemo

```python
## 取18张牌

from random import *

## 定义13个数字与大小王
values = range(1,13) + 'dwang xwang'.split()
## 定义四个花色
suits = 'hei hong mei fang '.split()

## 循环嵌套将其循环组合
deck = ['%s of %s'%(v,s) for v in values for s in suits]

## 调用pprint模块
from pprint import pprint
from random import shuffle

## 随机
shuffle(deck)
pprint(deck[:18])
```

#### 加载模块

```shell
# 安装模块的时候可能会出现
# running setup.py install for olefile ... error
# 尝试一下命令，可能是权限的问题 后面加上--user
pip install Pillow --user
```

#### 中文空格

chr(12288)

