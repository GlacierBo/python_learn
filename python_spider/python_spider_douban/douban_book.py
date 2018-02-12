# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     douban_book
   Description :
   Author :       Glacier
   date：          
-------------------------------------------------
   Change Activity:
                   :
-------------------------------------------------
"""
__author__ = 'Glacier'

import requests
from bs4 import BeautifulSoup
import traceback
import re

headers = {
    # 'Host': 'i.meizitu.net',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:55.0) Gecko/20100101 Firefox/55.0',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Connection': 'keep-alive',
    'Accept-Encoding':'gzip, deflate',
    'Upgrade-Insecure-Requests':'1'
}

# 获取html text
def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30, headers=headers)
        r.raise_for_status()
        r.encoding = 'utf-8'
        return r.text
    except:
        return ""

# 对text进行解析
def getBookList(fpath,text):

    soup = BeautifulSoup(html, "html.parser")
    bookName = soup.select("h1")[0].get_text(strip=True)
    bookInfoText = soup.find_all(id="info")[0]
    bookInfo = bookInfoText.get_text(" ",strip=True).split(" ")

    # print("书名: ", bookName)
    # print("作者：",bookInfo[3])
    # print("出版社: ",bookInfo[6])
    # print("出版年: ",bookInfo[11])
    # print("定价： ",bookInfo[15])
    # print("装订： ",bookInfo[17])

    Str = "书名:"+ str(bookName) + "\t作者:"+ str(bookInfo[3]) \
            + "\t出版社:" + str(bookInfo[6]) + "\t出版年:"+ str(bookInfo[11]) \
            + "\t定价:" + str(bookInfo[15]) + "\t装订:" + bookInfo[17]

    with open(fpath, 'a', encoding='utf-8') as f:
        f.write(str(bookInfo) + '\n')

if __name__ == '__main__':
    url = "https://book.douban.com/subject/27169888/"
    fpath = "doubanBook.txt"
    html = getHTMLText(url)
    getBookList(fpath,html)

