
# -*- coding: utf-8 -*-
# @Time    : 2018/3/26 11:01
# @Author  : glacier
# @Email   : 2284711614@qq.com
# @File    : yiliao.py
# @Software: PyCharm
import re
import requests
import traceback
from bs4 import BeautifulSoup
import pymysql

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:55.0) Gecko/20100101 Firefox/55.0',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Connection': 'keep-alive',
    'Accept-Encoding':'gzip, deflate',
    'Upgrade-Insecure-Requests':'1'
}

def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30, headers=headers)
        r.raise_for_status()
        r.encoding = 'utf-8'
        return r.text
    except:
        traceback.print_exc()
        return ""

def getHTMLInfo(html):
    soup = BeautifulSoup(html, "html.parser")
    urls = soup.find('div',{'class':'header_main_nav_2'})

    # 导航栏的链接
    all_a_lib = urls.findAll('a')

    for a_lib in all_a_lib:
        new_url = a_lib['href']
        url = "http://apps.xikang.com"+new_url
        print(url)
        html2 = getHTMLText(url)
        soup2 = BeautifulSoup(html2, "html.parser")
        uls = soup2.find('ul',{'class':'news_list'})
        # 所有的列表
        lis = uls.findAll('li')

        for article in lis:
            art_url = article.find('a')
            img_url = art_url.find('img').attrs['src']
            article_url = art_url['href']
            article_title = art_url['title']

            #接下来根据 链接去获取文章内容
            article_content = getArticleContent(art_url['href'])

            # 打开数据库连接
            db = pymysql.connect(
                "localhost",
                "root",
                "",
                "python",
                charset='utf8'
            )
            # 使用 cursor() 方法创建一个游标对象 cursor
            cursor = db.cursor()

            print(img_url,article_url,article_title,article_content)
            sql = "insert into xikangwang(img_url,article_url,article_title,article_content) value(%s,%s,%s,%s)"
            try:
                # 执行SQL语句
                cursor.execute(sql, (img_url, article_url, article_title,article_content))
                # 提交到数据库执行
                db.commit()
            except:
                traceback.print_exc()
                # 发生错误时回滚
                db.rollback()

            # 关闭数据库连接
            db.close()


    pass

def getArticleContent(url):
    new_url = "http://apps.xikang.com" + url
    html = getHTMLText(new_url)
    soup = BeautifulSoup(html, "html.parser")
    article = soup.find('div',{'class':'mainarea'})
    # title = article.find('div',{'class':'articlebody_top'}).find('h1').get_text(strip=True)
    contents = article.find('div',{'id':'articlebody'}).findAll('p')
    # 切片处理，最后一条没卵用
    contents = contents[:-1]
    article_content = ""
    for content in contents:
        article_content += content.get_text(strip=True)
    return article_content


def getNavs():
    urls = [
        'http://apps.xikang.com/kbfeipang/index.jhtml',
        'http://apps.xikang.com/kbgaoxueya/index.jhtml',
        'http://apps.xikang.com/kbtangnb/index.jhtml',
        'http://apps.xikang.com/kbbaojianys/index.jhtml',

    ]
    return urls

if __name__ == '__main__':
    # 肥胖
    urls = getNavs()
    for url in urls:
        url = "http://apps.xikang.com/kbfeipang/index.jhtml"
        html = getHTMLText(url)
        getHTMLInfo(html)

    print("爬取完成。")


