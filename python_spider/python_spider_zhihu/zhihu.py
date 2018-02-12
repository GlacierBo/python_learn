#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/15 15:34
# @Author  : glacier
# @Site    : 
# @File    : zhihu.py
# @Software: PyCharm Edu


import requests
from bs4 import BeautifulSoup as BS
import time
from subprocess import Popen  # 打开图片
import http.cookiejar
import re
import pymysql

def bs_text(text):
    soup = BS(text,"lxml")
    contents = soup.find_all('div',{'class':'question_link'})
    return contents


# 模拟浏览器访问
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.109 Safari/537.36'
}
home_url = "https://www.zhihu.com"
base_login = "https://www.zhihu.com/login/"  # 一定不能写成http,否则无法登录

session = requests.session()
session.cookies = http.cookiejar.LWPCookieJar(filename='ZhiHuCookies')
try:
    # 加载Cookies文件
    session.cookies.load(ignore_discard=True)
except:
    print("cookie未保存或cookie已过期")
    # 第一步 获取_xsrf
    _xsrf = BS(session.get(home_url, headers=headers).text, "lxml").find("input", {"name": "_xsrf"})["value"]

    # 第二步 根据账号判断登录方式
    account = "账号"
    password = "密码"

    # 第三步 获取验证码图片
    gifUrl = "http://www.zhihu.com/captcha.gif?r=" + str(int(time.time() * 1000)) + "&type=login"
    gif = session.get(gifUrl, headers=headers)
    # 保存图片
    with open('code.gif', 'wb') as f:
        f.write(gif.content)
    # 打开图片
    Popen('code.gif', shell=True)
    # 输入验证码
    captcha = input('captcha: ')

    data = {
        "captcha": captcha,
        "password": password,
        "_xsrf": _xsrf,
    }

    # 第四步 判断account类型是手机号还是邮箱
    if re.match("^.+\@(\[?)[a-zA-Z0-9\-\.]+\.([a-zA-Z]{2,3}|[0-9]{1,3})(\]?)$", account):
        # 邮箱
        data["email"] = account
        base_login = base_login + "email"
    else:
        # 手机号
        data["phone_num"] = account
        base_login = base_login + "phone_num"

    print(data)

    # 第五步 登录
    response = session.post(base_login, data=data, headers=headers)
    print(response.content.decode("utf-8"))

    # 第六步 保存cookie
    session.cookies.save()


def bs_text(text):
    soup = BS(text,"lxml")
    contents = soup.find_all('a',{'class':'question_link'})
    count = soup.find_all('a',{'class':'zm-item-vote-count js-expand js-vote-count'})

    # 标题链接
    title_url = re_text_title(contents)
    # 标题
    title = re_text_del_html(contents)
    # 高赞回答
    vote_count = re_text_del_html(count)

    title = str(title).replace("\n","").replace("[","").replace("]","").split(",")
    vote_count = str(vote_count).replace("\n","").replace("[","").replace("]","").split(",")

    for i in  range(0,len(title_url)):
         db_deal(title_url[i],title[i],vote_count[i])

def re_text_title(text):
    href = re.findall('href="(.*?)"',str(text))
    return href

def re_text_del_html(text):
    re_h = re.compile('</?\w+[^>]*>')
    s = re_h.sub('',str(text))
    return s

def db_deal(title_url,title,count):
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

    sql = "INSERT INTO p_zhihu_topic_flim(title,title_url, \
           vote_count) \
           VALUES ('%s', '%s', '%s')" % \
           (title_url,title,count.replace("K","000"))
    try:
       # 执行SQL语句
       cursor.execute(sql)
       print(title_url,title,count.replace("K","000"))
       # 提交到数据库执行
       db.commit()
    except:
       print("出错啦！")
       # 发生错误时回滚
       db.rollback()

    # 关闭数据库连接
    db.close()


# 获取首页信息
for i in range(1,50):
    resp = session.get("https://www.zhihu.com/topic/19556784/top-answers?page="+str(i)+"", headers=headers, allow_redirects=False).text
    bsText = bs_text(resp)

print("爬取精品贴完成，等待小主下一步指示...")






