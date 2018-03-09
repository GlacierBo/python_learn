#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/9 10:54
# @Author  : glacier
# @Site    : 
# @File    : anjuke-ks-average.py
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

    house_details = soup.find_all("div",{"class":"li-itemmod"})
    for house_detail in house_details:
        title = house_detail.find('a').get('title')
        href = house_detail.find('a').get('href')
        price = house_detail.find('div',{'class':'li-side'}).find('strong').get_text(strip=True)
        address = house_detail.find('div',{'class':'li-info'}).find('address').get_text(strip=True)
        buildData = house_detail.find('p',{'class':'date'}).get_text(strip=True)

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

        sql = "insert into anju_ks_community(houseName,houseUrl,housePrice,houseAddress,buildData) value(%s,%s,%s,%s,%s)"
        try:
            # 执行SQL语句
            cursor.execute(sql,(title,href,price,address,buildData))
            # 提交到数据库执行
            db.commit()
        except:
            traceback.print_exc()
            # 发生错误时回滚
            db.rollback()

        # 关闭数据库连接
        db.close()


if __name__ == '__main__':
    for pn in range(1,50):
        try:
            # print("正在爬取第"+ str(pn) +"个页面")
            # https://suzhou.anjuke.com/sale/p1-rd1/
            # https://ks.anjuke.com/sale/p1-rd1/

            url = "https://ks.anjuke.com/community/p"+str(pn)+"/"
            print(url)
            html = getHTMLText(url);
            getHTMLInfo(html)
        except:
            continue

    print("爬取完成")





