# -*- coding: utf-8 -*-
# @Time    : 2018/3/27 15:57
# @Author  : glacier
# @Email   : 2284711614@qq.com
# @File    : download_img.py
# @Software: PyCharm

import pymysql
import requests,traceback



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
        return r.content
    except:
        traceback.print_exc()
        return ""


def downIMG(url,imgName):
    try:
        LAST = str(url).split(".")[-1]
        PATH = "D:\\Python_IMG\\" +imgName + "."+ LAST
        html = getHTMLText(url)
        with open(PATH, 'wb') as f:
            f.write(html)
    except:
        pass
    pass

if __name__ == '__main__':

    db = pymysql.connect(
        "localhost",
        "root",
        "",
        "python",
        charset='utf8'
    )
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()

    sql = "SELECT img_url,article_title FROM xikangwang "
    try:
        # 执行SQL语句
        cursor.execute(sql)
        tables = cursor.fetchall()
        for table in tables:
            downIMG(table[0],table[1])
        # 提交到数据库执行
        db.commit()

    except:
        print("出错啦！")
        # 发生错误时回滚
        db.rollback()

    # 关闭数据库连接
    db.close()

    print("所有图片已下载完成")


