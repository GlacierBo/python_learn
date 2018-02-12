#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/5 11:25
# @Author  : glacier
# @Site    : 股市有风险，投资需谨慎
# @File    : tock_demo.py
# @Software: PyCharm Edu


import requests
from bs4 import BeautifulSoup
import traceback
import re

def getHTMLText(url):
    try:
        r = requests.get(url,timeout=30)
        # 状态码不为200 抛出异常
        r.raise_for_status()
        # 我们可以手动给encoding
        # r.encoding = r.apparent_encoding
        r.encoding = 'utf-8'
        return r.text
    except:
        return ""

def getStockList(lst,stockURL):
    html = getHTMLText(stockURL)
    soup = BeautifulSoup(html,"html.parser")
    a = soup.find_all('a')
    for i in a :
        try:
            href = i.attrs['href']
            lst.append(re.findall(r"[s][hz]\d{6}",href)[0])
        except:
            continue

def getStockInfo(lst,stockURL,fpath):
    for stock in lst:
        url = stockURL + stock + ".html"
        html = getHTMLText(url)
        print("股票代码：",stock)
        try:
            if html =="":
                continue
            infoDict={}
            soup = BeautifulSoup(html,"xml")
            stockInfo = soup.find('div', attrs={'class':'stock-bets'})
            name = stockInfo.find_all(attrs={'class':'bets-name'})[0]
            infoDict.update({'股票名称':name.text.split()[0]})

            keyList = stockInfo.find_all('dt')
            valueList = stockInfo.find_all('dd')
            for i in range(len(keyList)):
                key = keyList[i].text
                val = valueList[i].text
                # 构造
                infoDict[key] = val

            with open(fpath,'a',encoding='utf-8') as f:
                f.write(str(infoDict)+'\n')

        except:
            print("异常")
            traceback.print_exc()
            continue
    return ""

if __name__ == '__main__':
    print("开始统计股票")
    stock_list_url = "http://quote.eastmoney.com/stocklist.html"
    stock_info_url = "https://gupiao.baidu.com/stock/"
    output_file="BaiduStockInfo.txt"
    slist = []
    getStockList(slist,stock_list_url)
    getStockInfo(slist,stock_info_url,output_file)
    print("统计结束")






