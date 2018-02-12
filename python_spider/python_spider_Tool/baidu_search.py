#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/3 13:57
# @Author  : glacier
# @Site    : 
# @File    : baidu_search.py
# @Software: PyCharm Edu

import requests

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
    key = input("输入您要查询的内容：")
    kv = {'wd':key}
    url = "https://www.baidu.com/s"
    req = requests.get(url,params=kv,headers=headers).text
    print(req)



