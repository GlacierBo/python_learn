#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/21 9:06
# @Author  : glacier
# @Site    : 
# @File    : from_sql_excel.py
# @Software: PyCharm Edu


import pymysql
import xlwt
import openpyxl


def db_deal():
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

    sql = "SELECT id,title,title_url,vote_count FROM p_zhihu_topic_flim"
    try:
        # 执行SQL语句
        cursor.execute(sql)
        results = cursor.fetchall()

        wb=openpyxl.Workbook()
        wb.save(filename="test.xlsx")
        print("新建 Excel："+"test.xlsx"+"成功")

        print("写入到 Excel...")
        wbk = xlwt.Workbook()
        sheet = wbk.add_sheet('Sheet')
        rowlen = len(results)
        for i in range(rowlen):
            for j in range(4):
                sheet.write(i,j,results[i][j])


        wbk.save("test.xlsx")

        print("成功写入 Excel,正在关闭数据库连接...")
       # 提交到数据库执行
        db.commit()
    except:
        print("出错啦！")
        # 发生错误时回滚
        db.rollback()

    # 关闭数据库连接
    db.close()


db_deal()
print("小主，Execl已经生成好啦！")
