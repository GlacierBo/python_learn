#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/12 12:25
# @Author  : glacier
# @Site    : 
# @File    : tieba.py
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
}

s = requests.session()  # 保留会话

def re_test(text):
    re_h = re.compile('</?\w+[^>]*>')
    s = re_h.sub('',text)
    return s

def bs_test(text):
    soup = BeautifulSoup(text,"lxml")
    contents = soup.find_all('div',{'class':'d_post_content j_d_post_content '})
    return contents

def save_text(text):
    import os

    with open('tieba.txt',"a+",encoding='utf-8') as t:
        t.write(text)
        t.close()

if __name__ == '__main__':
    for i in range(30):
        url = "https://tieba.baidu.com/p/5479305573?see_lz=1&pn="+str(i+1)
        req_text = s.get(url).text

        bsText = bs_test(req_text)
        reText = re_test(str(bsText))
        save_text(reText.lstrip())
    print('爬取完成')


