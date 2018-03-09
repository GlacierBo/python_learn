#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/8 17:44
# @Author  : glacier
# @Site    : 
# @File    : anjuke-cx.py
# @Software: PyCharm Edu





import re,requests
from bs4 import BeautifulSoup
import traceback
import pymysql

headers = {
    # 'Host': 'i.meizitu.net',
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
        traceback.print_exc()
        return ""

# 对text进行解析
def getHTMLInfo(html):
    soup = BeautifulSoup(html,"html.parser")
    # class="house-details"
    house_details = soup.find_all("li",{"class":"list-item"})

    for house_detail in house_details:
        url = house_detail.find('a').get('href')
        title = house_detail.find("a",{"class":"houseListTitle"}).get("title")
        details = house_detail.find("div",{"class":"details-item"}).get_text(strip=True)
        address = house_detail.find("span",{"class":"comm-address"}).get("title")
        tips = house_detail.find("div",{"class":"tags-bottom"}).get_text(strip=True)

        price = house_detail.find("span",{"class":"price-det"}).get_text(strip=True)

        if int(price.replace("万","")) <= 120:
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

            sql = "insert into anju_suzhou(url,title,details,address,tips,price) value(%s,%s,%s,%s,%s,%s)"
            try:
                # 执行SQL语句
                cursor.execute(sql,(url,title,details,address,tips,price))
                # 提交到数据库执行
                db.commit()
            except:
                traceback.print_exc()
                # 发生错误时回滚
                db.rollback()

            # 关闭数据库连接
            db.close()


if __name__ == '__main__':

    for pn in range(1,51):
        try:
            print("正在爬取第"+ str(pn) +"个页面")
            # https://suzhou.anjuke.com/sale/p1-rd1/
            # https://ks.anjuke.com/sale/p1-rd1/
            # https://ks.anjuke.com/sale/chengxikunshan/p2-rd1/?kw=%E7%8E%89%E5%B1%B1#filtersort
            url = "https://ks.anjuke.com/sale/chengnankunshan/"+str(pn)+"-rd1/"
            html = getHTMLText(url);
            getHTMLInfo(html)
        except:
            continue

    print("爬取完成")