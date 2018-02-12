#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/17 13:19
# @Author  : glacier
# @Site    : 
# @File    : db_test.py
# @Software: PyCharm Edu
import pymysql

import pymysql


def db_deal(title_url,title,count):
    # 打开数据库连接
    db = pymysql.connect(
            "localhost",
            "root",
            "123456",
            "python",
            charset='utf8'
    )
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()

     # 使用预处理语句创建表

    # SQL 插入语句
    sql = "INSERT INTO p_zhihu_topic(title,title_url, \
           vote_count) \
           VALUES ('%s', '%s', '%s')" % \
           (title_url,title,count)
    try:
       # 执行SQL语句
       cursor.execute(sql)
       print('插入成功')

       # 提交到数据库执行
       db.commit()
    except:
       print("出错啦！")
       # 发生错误时回滚
       db.rollback()

if __name__ == '__main__':

    title_url ="/question/22425541"
    title ="一个人旅行应该怎样自拍"
    count ="24K"

    db_deal(title_url,title,count)





