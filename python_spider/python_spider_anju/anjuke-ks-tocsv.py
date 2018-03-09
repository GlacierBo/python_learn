#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/9 11:39
# @Author  : glacier
# @Site    : 
# @File    : anjuke-ks-tocsv.py
# @Software: PyCharm Edu

import pymysql,traceback


import csv


# 打开数据库连接
db = pymysql.connect(
    "localhost",
    "root",
    "123456",
    "python",
    charset='utf8'
)

cursor = db.cursor()
sql = "SELECT houseName,housePrice FROM anju_ks_community"
try:
    # 执行SQL语句
    table  = cursor.execute(sql)
    results = cursor.fetchall()

    csvFile = open('anjuke-ks-tocsv.csv','w', newline='',encoding='utf-8') # 设置newline，否则两行之间会空一行
    writer = csv.writer(csvFile)
    writer.writerow(['小区','价格（平方/元）'])

    for result in results:
        writer.writerow([result[0],result[1]])
    csvFile.close()

    # 提交到数据库执行
    db.commit()
except:
    traceback.print_exc()
    # 发生错误时回滚
    db.rollback()

# 关闭数据库连接
db.close()