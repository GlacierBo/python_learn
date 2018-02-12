#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/21 16:58
# @Author  : glacier
# @Site    : 
# @File    : Satisfaction.py
# @Software: PyCharm Edu


import pymysql,xlwt,openpyxl
from xlrd import open_workbook
from xlutils.copy import copy
import time
from datetime import datetime


def db_deal(data_time):
     # 打开数据库连接
    db = pymysql.connect(
            "116.62.66.227",
            "root",
            "123456",
            "canteen",
            charset='utf8'
    )
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()

    wb=openpyxl.Workbook()
    wb.save(filename="Satisfaction.xlsx")
    print("新建 Excel："+"Satisfaction.xlsx"+"成功")

    results =[]

    for i in range(1,16):
        sql = "SELECT b.qid,a.uid,b.score,b.info,a.ctime from ainfo a LEFT JOIN answer b on a.uid = b.uid where a.ctime >= '%s' and b.qid = '%s'"% \
                    (data_time,str(i))

        try:
            # 执行SQL语句
            cursor.execute(sql)
            results += cursor.fetchall()
           # 提交到数据库执行
            db.commit()
        except:
            print("出错啦！")
            # 发生错误时回滚
            db.rollback()

    print("写入到 Excel...")
    book = open_workbook("Satisfaction.xlsx")
    wfile = copy(book)
    wsheet = wfile.get_sheet('Sheet')

    rowlen = len(results)
    i = 2
    for i in range(rowlen):
        for j in range(5):
            wsheet.write(i,j,results[i][j])

    wfile.save("Satisfaction.xlsx")
    print("成功写入 Excel,正在关闭数据库连接...")


    # 关闭数据库连接
    db.close()

if __name__ == '__main__':
     # db_deal()
     data_time = time.strftime('%Y-%m',time.localtime(time.time()))
     data_time = str(data_time) + "-1"

     db_deal(datetime.strptime("2018-1-1", "%Y-%m-%d"))

     print("小主，Execl已经生成好啦！等待您的下一个指令...")



