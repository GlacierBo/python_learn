#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/22 11:35
# @Author  : glacier
# @Site    : 
# @File    : duanzi_api.py
# @Software: PyCharm Edu


import requests

headers = {
    # 'Host': 'i.meizitu.net',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Connection': 'keep-alive',
    'Accept-Encoding':'gzip, deflate',
    'Upgrade-Insecure-Requests':'1'
}

s = requests.session()  # 保留会话
url = 'http://m.neihanshequ.com/'

req_text = s.get(url,headers=headers).text;

print(req_text)

