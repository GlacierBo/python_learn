# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     classification
   Description :
   Author :       Glacier
   date：          
-------------------------------------------------
   Change Activity:
                   :
-------------------------------------------------
"""
__author__ = 'Glacier'

import requests
from bs4 import BeautifulSoup
import pymysql
import traceback

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:55.0) Gecko/20100101 Firefox/55.0',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Connection': 'keep-alive',
    'Accept-Encoding':'gzip, deflate',
    'Upgrade-Insecure-Requests':'1'
}

# 获取html text
def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30, headers=headers)
        r.raise_for_status()
        r.encoding = 'utf-8'
        return r.text
    except:
        print("解析HTML异常")
        return ""

def getHTMLInfo(html):
    soup = BeautifulSoup(html,"html.parser")
    booksInfo = soup.find_all('li', {'class': 'subject-item'})

    for bookInfo in booksInfo:
        writer = bookInfo.find('div', {'class': 'pub'})
        # print(booksInfo[0])
        hrefs = bookInfo.find_all('a')
        img = bookInfo.find('img')
        info = bookInfo.find('p')
        score = bookInfo.find('span', {'class': 'rating_nums'})
        # 图书名
        bookNameStr = hrefs[1].get("title")
        # 作者
        writerStr = writer.get_text(strip=True)
        # 图书链接
        bookHref = hrefs[1].get("href")
        # 评分
        scoreStr = score.get_text(strip=True)
        # 图片链接
        imgUrlStr = img.get("src")
        # 简介
        bookInfoStr = info.get_text(strip=True)

        # 打开数据库连接 #数据库信息可能需要自己修改
        db = pymysql.connect(
            "localhost",
            "root",
            "123456",
            "python",
            charset='utf8'
        )
        sql = 'insert into douban_book(bookName,writer,bookHref,scoreStr,bookInfoStr,imgUrlStr) value(%s, %s, %s, %s, %s,%s)'
        # 存入数据库

        # 使用 cursor() 方法创建一个游标对象 cursor
        cursor = db.cursor()
        try:
            # 执行SQL语句
            cursor.execute(sql, (bookNameStr, writerStr, bookHref, scoreStr,bookInfoStr, imgUrlStr))
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
    keyword = "小说"

    for i in range(0,50):
        url = "https://book.douban.com/tag/" + str(keyword) + "?start=" + str(i*20)
        try:
            html = getHTMLText(url)
            getHTMLInfo(html)
        except:
            print("出错啦！")
            traceback.print_exc()
            continue

        print("执行完毕")



