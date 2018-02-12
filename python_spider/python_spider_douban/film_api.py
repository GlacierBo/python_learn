# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     film_api
   Description :
   Author :       Glacier
   date：          
-------------------------------------------------
   Change Activity:
                   :
-------------------------------------------------
"""
__author__ = 'Glacier'

'''
电影
https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&start=40&limit=20
评论
https://movie.douban.com/j/review/1294699/full?show_works=False
'''

import requests,re
from bs4 import BeautifulSoup
import traceback
import pymysql

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:55.0) Gecko/20100101 Firefox/55.0',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Connection': 'keep-alive',
    'Accept-Encoding': 'gzip, deflate',
    'Upgrade-Insecure-Requests': '1'
}

# 构建请求 url
def initRequestURL(type):
    limit = 200
    # 计数器
    count = 0
    for i in range(1,limit):
        try:
            url = "https://movie.douban.com/j/chart/top_list?type=" + str(type) \
                  + "&interval_id=100%3A90&action=&start="+str((i-1)*20)+"&limit=" + str(i*20)
            # url = "https://movie.douban.com/j/chart/top_list?type=1&interval_id=100%3A90&action=&start=280&limit=300"
            print(url)
            html = getHTMLText(url)
            soup = BeautifulSoup(html,"html.parser")
            if str(soup.get_text()) == "[]":
                break
            getHTMLInfo(html, count)
        except:
            print("initRequestURL 异常")
            break

# 解析 HTML
def getHTMLText(url):
    try:
        r = requests.get(url,timeout=30,headers=headers)
        r.raise_for_status()
        return r.text
    except:
        # 如果出错则打印错误
        traceback.print_exc()
        return "getHTMLText 异常"

# 信息过滤
def getHTMLInfo(html,count):
    try:
        # 影片名
        titles = re.findall(r'\"title\"\:\".*?\"', html)
        # 评分
        scores = re.findall(r'\"score\"\:\".*?\"', html)
        # 发布时间
        release_dates = re.findall(r'\"release_date\"\:\".*?\"', html)
        # url
        # cover_urls = re.findall(r'\"cover_url\"\:\".*?\"', html)
        ids = re.findall(r'\"id\"\:\".*?\"', html)
        # 影片类型
        types = re.findall(r'\"types\":\[.*?\]', html)
        # 评价人数
        vote_counts = re.findall(r'\"vote_count\"\:\d+', html)

        for i in range(len(titles)):
            title = eval(titles[i].split(":")[1])
            score = eval(scores[i].split(":")[1])
            film_id = eval(ids[i].split(":")[1])
            film_type = eval(types[i].split(":")[1])
            release_date = eval(release_dates[i].split(":")[1])
            vote_count = eval(vote_counts[i].split(":")[1])

            film_type = str(film_type).replace("[","").replace("]","").replace("'","")
            # 打开数据库连接 #数据库信息可能需要自己修改
            db = pymysql.connect(
                "localhost",
                "root",
                "123456",
                "python",
                charset='utf8'
            )
            print(film_id,title,film_type,score,release_date,vote_count)
            sql = 'insert into douban_film(film_id,title,`film_type`,score,release_date,vote_count) ' \
                  'VALUES (%s,%s, %s, %s, %s, %s)'
            # 存入数据库

            # 使用 cursor() 方法创建一个游标对象 cursor
            cursor = db.cursor()
            try:
                # 执行SQL语句
                cursor.execute(sql, (film_id,title,film_type,score,release_date,vote_count))
                # 提交到数据库执行
                db.commit()
                count = count + 1
                print("正在插入第"+ str(count) +"条数据")
            except:
                print("出错了")
                traceback.print_exc()
                # 发生错误时回滚
                db.rollback()

            # 关闭数据库连接
            db.close()

            # infoList.append([id, title, rating, cover_url, type])
    except:
        traceback.print_exc()
        print("getHTMLInfo 异常")


if __name__ == '__main__':

    type = 31
    for i in range(1,type):
        initRequestURL(i)


    print("爬取完成！")









