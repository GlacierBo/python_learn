#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/9 9:57
# @Author  : glacier
# @Site    : 
# @File    : lagou.py
# @Software: PyCharm Edu


import requests
from bs4 import BeautifulSoup
import traceback
import pymysql

headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Accept-Encoding': 'gzip, deflate, br'
}

def getHTMLText(url):
    try:
        r = requests.get(url,headers=headers,timeout=30)
        r.raise_for_status()
        r.encoding = "utf-8"
        return r.text
    except:
        traceback.print_exc()
        print("异常啦")

def getHTMLInfo(html):

    soup = BeautifulSoup(html,"html.parser")
    Infos = soup.find_all("li",{"class":"con_list_item default_list"})

    for Info in Infos:
        labs= Info.find('div',{'class': 'li_b_r'}).get_text(strip=True)
        positionid = Info.attrs["data-positionid"]
        salary = Info.attrs["data-salary"]
        company  = Info.attrs["data-company"]
        positionname = Info.attrs["data-positionname"]
        companyid = Info.attrs["data-companyid"]
        hrid = Info.attrs["data-hrid"]
        adword = Info.attrs["data-adword"]

       #  print("{0:10}{1:15}{2:25}{3:25}".format(positionid,positionname,salary,company))

        # 打开数据库连接 #数据库信息可能需要自己修改
        db = pymysql.connect(
            "116.62.66.227",
            "root",
            "123456",
            "pythondb",
            charset='utf8'
        )
        sql = 'insert into lagou_info(positionid, salary, company, positionname,companyid, hrid,adword,labs) value(%s, %s, %s, %s,%s, %s,%s,%s)'
        # 存入数据库

        # 使用 cursor() 方法创建一个游标对象 cursor
        cursor = db.cursor()
        try:
            # 执行SQL语句
            cursor.execute(sql, (positionid, salary, company, positionname,companyid, hrid,adword,labs))
            # 提交到数据库执行
            db.commit()
        except:
            print("出错了")
            traceback.print_exc()
            # 发生错误时回滚
            db.rollback()

        # 关闭数据库连接
        db.close()


if __name__ == '__main__':
    key_word = input("输入查询的职位：")
    # key_word = "Java"
    for i in range(1,31):
        try:
            url = 'https://www.lagou.com/zhaopin/'+ key_word +'/'+ str(i) +'/?filterOption=3'
            print(url)
            html = getHTMLText(url)
            getHTMLInfo(html)
        except:
            traceback.print_exc()
            continue

    print("爬取完成！")


