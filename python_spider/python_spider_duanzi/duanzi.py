#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/21 15:04
# @Author  : glacier
# @Site    : 
# @File    : duanzi.py
# @Software: PyCharm Edu

import re,requests
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

def dz_bs_text(text):
    soup = BeautifulSoup(text,"lxml")
    content = soup.find_all('p',{'class':''})
    digg = soup.find_all('span',{'class':'digg'})

    content = dz_re_text(content)
    digg = dz_re_text(digg)

    content = content.split(',')
    digg = digg.split(',')

    max_happy_content = ""
    max_digg = 0

    for i in range(0,len(digg)):
        if int(digg[i]) >= max_digg:
            max_digg = int(digg[i])
            max_happy_content = content[i]

    return max_happy_content.strip()

def dz_re_text(html):

    strs = str(html).split(',')
    re_h = re.compile('</?\w+[^>]*>')
    s = re_h.sub('',str(strs).replace("[","").replace("]","").replace("'",""))
    return s


if __name__ == '__main__':
    url = 'http://neihanshequ.com/'
    req_text = s.get(url).text;
    bsText = dz_bs_text(req_text)
    print(bsText)




