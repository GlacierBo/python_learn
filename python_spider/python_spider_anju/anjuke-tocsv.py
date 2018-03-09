#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/9 9:11
# @Author  : glacier
# @Site    : 
# @File    : anjuke-tocsv.py
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
sql = "SELECT details,address,price FROM anju_suzhou"
try:
    # 执行SQL语句
    table  = cursor.execute(sql)
    results = cursor.fetchall()

    csvFile = open('anjuke-tocsv.csv','w', newline='',encoding='utf-8') # 设置newline，否则两行之间会空一行
    writer = csv.writer(csvFile)
    writer.writerow(['户型','大小','层数','建造时间','小区名','地址','售价'])

    for result in results:
        others =  result[0].split("|")
        houseType = others[0]
        houseSize = others[1]
        houseFloor = others[2]
        houseBuild = others[3].split("\ue147")[0]
        houseName = result[1].split("  ")[0]
        houseAddress = result[1].split("  ")[-1]
        housePrice = result[2]

        writer.writerow([houseType,houseSize,houseFloor,houseBuild,houseName,houseAddress,housePrice])
        print(houseType  +","+ houseSize  +","+ houseFloor +","+ houseBuild+","+houseName +","+ houseAddress +","+ housePrice)

    csvFile.close()

    # 提交到数据库执行
    db.commit()
except:
    traceback.print_exc()
    # 发生错误时回滚
    db.rollback()

# 关闭数据库连接
db.close()

