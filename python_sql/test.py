#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/6 14:36
# @Author  : glacier
# @Site    : 
# @File    : test.py
# @Software: PyCharm Edu

import pymysql

db = pymysql.connect(
        "localhost",
        "root",
        "123456",
        "product_test",
        charset='utf8'
)
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

sql = "select * from product_category"
try:
   # 执行SQL语句
   table  = cursor.execute(sql)
   print(table)
   # 提交到数据库执行
   db.commit()
except:
   print("出错啦！")
   # 发生错误时回滚
   db.rollback()

# 关闭数据库连接
db.close()