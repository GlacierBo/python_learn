# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     tieba_img
   Description :
   Author :       Glacier
   date：          
-------------------------------------------------
   Change Activity:
                   :
-------------------------------------------------
"""
__author__ = 'Glacier'



import os
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

def re_test(text):
    re_h = re.compile('src="(.+?\.jpg)"')
    s = re_h.findall(text)
    return s

def bs_test(text):
    soup = BeautifulSoup(text,"lxml")
    contents = soup.find_all('img',{'class':'BDE_Image'})
    return contents

def save_text(text):
    import os
    with open('tieba.txt',"a+",encoding='utf-8') as t:
        t.write(text)
        t.close()

def save_img(url):
    # 去空格
    url.strip()
    path = url.split('/')
    filename = path[-1]

    if not os.path.exists('baidu_img'):  # 没有文件夹，则创建文件夹
        os.mkdir('baidu_img')

    url_re = s.get(url.strip(), headers=headers)
    if url_re.status_code == 200:  # 200是http响应状态
        print("保存中..." )
        open('baidu_img/' + filename, 'wb').write(url_re.content)

if __name__ == '__main__':
    for i in range(19):
        url = "http://tieba.baidu.com/p/4820729828?pn="+str(i+1)
        req_text = s.get(url).text
        bsImg = bs_test(req_text)
        reImg = re_test(str(bsImg))

        for i in reImg:
            save_img(i)

    print('下载完成')



