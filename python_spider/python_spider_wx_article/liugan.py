#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/5 13:08
# @Author  : glacier
# @Site    : 
# @File    : liugan.py
# @Software: PyCharm Edu

from bs4 import BeautifulSoup
import re
import requests

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:55.0) Gecko/20100101 Firefox/55.0',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Connection': 'keep-alive',
    'Accept-Encoding':'gzip, deflate',
    'Upgrade-Insecure-Requests':'1'
}

if __name__ == '__main__':
    pn = 1
    for pn in range(10):
        pn = pn * 10
        url = "https://www.baidu.com/s?wd=%E6%98%A5%E5%AD%A3%E6%B5%81%E6%84%9F&pn="+str(pn)+"&tn=baidurt&ie=utf-8&rtt=1&bsst=1"
        html = requests.get(url,headers=headers).text

        soup = BeautifulSoup(html,"html.parser")
        h3s = soup.find_all('h3',{'class':'t'})

        for h3 in h3s:
            print(h3.find('a').get('href'))
            print(h3.find('a').get_text(strip=True))
            with open("liugan.txt", "a",encoding='utf-8') as f:
                f.write(h3.find('a').get('href'))
                f.write("\n")
                f.write(h3.find('a').get_text(strip=True))
                f.write("\n")
                f.close()

    print("爬取完成！")



