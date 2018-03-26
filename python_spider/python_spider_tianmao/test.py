#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/5 10:06
# @Author  : glacier
# @Site    : 爬取淘宝商品
# @File    : yiliao.py
# @Software: PyCharm Edu

import requests,re,time

headers = {
    # 'Host': 'i.meizitu.net',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:55.0) Gecko/20100101 Firefox/55.0',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Connection': 'keep-alive',
    'Accept-Encoding':'gzip, deflate',
    'Upgrade-Insecure-Requests':'1'
}

def getHTMLText(url):
    print(url)
    try:
        r = requests.get(url,timeout = 30,headers=headers)
        # 响应不是200 则抛出异常
        r.raise_for_status()
        # 编码方式处理
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "getHTMLText 异常"

def parsePage(ilt,html):
    try:
        plt = re.findall(r'\"view_price\"\:\"[\d\.]*\"',html)
        tlt = re.findall(r'\"raw_title\"\:\".*?\"',html)
        print(plt)
        print(tlt)
        for i in range(len(plt)):
            price = eval(plt[i].split(":")[1])
            title = eval(tlt[i].split(":")[1])
            ilt.append([price,title])
    except:
        print("parsePage 异常")

def printGoodsList(ilt):
    tplt = "{:4}\t{:8}\t{:16}"
    print(tplt.format("序号","价格","商品名称"))
    count = 0
    for g in ilt:
        count = count + 1
        print(tplt.format(count,g[0],g[1]))

if __name__ == '__main__':
    goods = input("输入您要查找的商品：")
    # goods = "书包"
    depth = 3 # 深度
    start_url = "https://s.taobao.com/search?q=" + goods
    # 构造一个list
    infoList = []
    # 设计每个url链接
    for i in range(depth):
        try:
            url = start_url + '&s=' + str(44*i)
            html = getHTMLText(url)
            parsePage(infoList,html)
        except:
            continue
    printGoodsList(infoList)



