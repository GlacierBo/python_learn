#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/3 14:23
# @Author  : glacier
# @Site    : 
# @File    : search_ip.py
# @Software: PyCharm Edu


import requests
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

if __name__ == '__main__':
    # ip = input("输入您要查询的ip：")
    ip = "153.35.214.242"
    kv = {'ip':ip}
    url = "http://m.ip138.com/ip.asp"
    req = requests.get(url,params=kv,headers=headers).text
    soup = BeautifulSoup(req,"html.parser")
    # print(soup)
    print(soup.h1.string)



