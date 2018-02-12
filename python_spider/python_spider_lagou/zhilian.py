#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/9 11:53
# @Author  : glacier
# @Site    : 
# @File    : zhilian.py
# @Software: PyCharm Edu

import requests
from bs4 import BeautifulSoup
import traceback
import pymysql

headers ={
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Accept-Encoding': 'gzip, deflate, br'
}

def getHTMLText(url):
    try:
        r = requests.get(url,timeout=30,headers=headers)
        r.encoding = "utf-8"
        r.raise_for_status()
        return r.text
    except:
        traceback.print_exc()
        return ""

def getHTMLInfo(html):

    soup = BeautifulSoup(html,"html.parser")
    infolist = soup.find_all("table",{"class":"newlist"})

    for info in infolist:
        nowInfo =[]
        tds = info.find_all("td")
        for td in tds:
            nowInfo.append(td.get_text(strip=True))

        # 删除空项
        # while "" in nowInfo:
        #     nowInfo.remove("")

        positionname = nowInfo[0:1]
        persent = nowInfo[1:2]
        company = nowInfo[2:3]
        salary = nowInfo[3:4]
        city = nowInfo[4:5]
        info_type = nowInfo[5:6]
        info = nowInfo[6:7]
        print(positionname, company, salary, city,info_type,info,persent)


        # 打开数据库连接 #数据库信息可能需要自己修改
        db = pymysql.connect(
            "116.62.66.227",
            "root",
            "123456",
            "pythondb",
            charset='utf8'
        )
        sql = 'insert into zhilian_info_javascript (positionname, company, salary, city,info_type,info,persent) value(%s, %s, %s, %s,%s,%s,%s)'
        # 存入数据库
        # 使用 cursor() 方法创建一个游标对象 cursor
        cursor = db.cursor()
        try:
            # 执行SQL语句
            cursor.execute(sql, (positionname, company, salary, city,info_type,info,persent))
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
    # key_word = "java"
    key_word = input("请输入想要查询的关键词:")
    for pn in range(1,61):
        print("当前页码：",pn)
        url = "http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E4%B8%8A%E6%B5%B7%2b%E5%8C%97%E4%BA%AC%2b%E6%88%90%E9%83%BD%2b%E8%8B%8F%E5%B7%9E%2b%E6%9D%AD%E5%B7%9E&kw="+ key_word +"&isadv=0&" \
            "sg=a88505b61f9a438a83ff16e07c18a2cb&p="+str(pn)+""
        try:
            html = getHTMLText(url)
            getHTMLInfo(html)
        except:
            traceback.print_exc()
            continue
    print("爬取完成！请打开数据库查看！")

