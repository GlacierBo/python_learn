#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/21 14:17
# @Author  : glacier
# @Site    : 获取天气信息
# @File    : get_weather.py
# @Software: PyCharm Edu

from bs4 import BeautifulSoup
import re
import requests

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


def bs_text(text):
    soup = BeautifulSoup(text,"lxml")
    contents = soup.find_all('li',{'class':'week-detail-now'})
    return contents

def re_text(text):
    re_h = re.compile('</?\w+[^>]*>')
    s = re_h.sub('',text)
    s = s.replace("judgeDayNightStr('','');","").strip().replace("[","").replace("]","")\
        .replace("查看今日天气详情","").replace("查看明日天气详情","").replace("\n","")
    return s

if __name__ == '__main__':
    print("获取天气信息")
    url = "http://tianqi.2345.com/kunshan/60037.htm"
    req_text = s.get(url).text

    bsText = bs_text(req_text)
    reText = re_text(str(bsText))
    reText = reText.split(",")

    for i in reText :
        print(i.strip())






