#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/12 14:13
# @Author  : glacier
# @Site    : 
# @File    : dangni.py
# @Software: PyCharm Edu


import  re,requests
from bs4 import BeautifulSoup


headers = {
    # 'Host': 'i.meizitu.net',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:55.0) Gecko/20100101 Firefox/55.0',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Connection': 'keep-alive',
    'Accept-Encoding':'gzip, deflate',
    'Upgrade-Insecure-Requests':'1'
}  # 请求头，蛇无头不行，带上吧，后面会讲到用Cookie实现单账号免密登录

s = requests.session()  # 保留会话

def bs_test(text):
    soup = BeautifulSoup(text,"lxml")
    contents = soup.find_all('p',{'class':''})
    return contents


def re_test_html(text):
    # 过滤html 标签
    re_h = re.compile('</?\w+[^>]*>')
    s = re_h.sub('',text)
    return s

def re_test_css(text):
    # 过滤span
    re_h = re.compile('<span[^>]*>.*?</span>')
    s = re_h.sub('',text)
    return s

def save_text(text):
    with open('dangni.txt',"a+",encoding='utf-8') as f:
        f.write(text)
        f.close()

if __name__ == '__main__':

    for i in range(1,200,20):
        url = "https://movie.douban.com/subject/26930504/comments?start="+str(i)+"&limit=20&sort=new_score&status=P&percent_type="
        req_text =  s.get(url).text

        bsText = bs_test(req_text)
        reText = re_test_css(str(bsText))
        reText = re_test_html(str(reText))

        save_text(reText.lstrip())
    print('爬取完成')


