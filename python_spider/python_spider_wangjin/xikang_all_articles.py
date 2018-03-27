# -*- coding: utf-8 -*-
# @Time    : 2018/3/27 16:30
# @Author  : glacier
# @Email   : 2284711614@qq.com
# @File    : xikang_all_articles.py
# @Software: PyCharm

import requests
import traceback
from bs4 import BeautifulSoup
import pymysql
IP = 'http://apps.xikang.com'

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:55.0) Gecko/20100101 Firefox/55.0',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Connection': 'keep-alive',
    'Accept-Encoding':'gzip, deflate',
    'Upgrade-Insecure-Requests':'1'
}

def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30, headers=headers)
        r.raise_for_status()
        r.encoding = 'utf-8'
        return r.text
    except:
        traceback.print_exc()
        return ""



def initURL():
    urls = {
        'http://apps.xikang.com/fpgs/index.jhtml',
        'http://apps.xikang.com/kbgaoxueya/index.jhtml',
        'http://apps.xikang.com/kbtangnb/index.jhtml',
        'http://apps.xikang.com/kbbaojianys/index.jhtml'
    }
    return urls
# 二级导航
def getNavUrl(url):
    html = getHTMLText(url)
    soup = BeautifulSoup(html,"html.parser")
    nav = soup.find('div',{'class':'header_main_nav_2'})
    lis = nav.findAll('li')
    NavUrls =[]

    for li in lis:
        a_libs = li.findAll('a')
        for a_lib in a_libs:
            NavUrls.append(IP + a_lib['href'])
    print(NavUrls)
    return NavUrls
# 三级导航
def getSmallNavUrl(small_nav):
    a_libs = small_nav.findAll('a')
    urls = []
    for a_lib in a_libs:
        urls.append(IP + a_lib['href'])
    return urls

def getArticleList(url):
    html = getHTMLText(url)
    soup = BeautifulSoup(html, "html.parser")
    try:
        # 有没有 辅 Nav
        small_nav = soup.find('div',{'class':'news_list_tit'})
        # 获取urls
        urls = getSmallNavUrl(small_nav)
        url = 'http://apps.xikang.com/fpyylf/index.jhtml'
        # 获取所有文章
        getArticles(url)
        pass
    except:
        # 如果没有 辅Nav 那就不需要做过多的处理了
        # 直接处理文章内容就行了
        pass

    pass
def detailArticle():
    pass

def getArticles(url):
    urls = getAllPageUrls(url)
    for url in urls:
        html = getHTMLText(url)
        soup = BeautifulSoup(html,'html.parser')
        detailArticle(soup)
    pass

# 获取所有需要抓取的 子页面
def getAllPageUrls(url):

    ip = url.replace(url.split('/')[-1],"")
    # 解析网页
    html_first = getHTMLText(url)
    soup_first = BeautifulSoup(html_first, "html.parser")
    # 获取页码，决定循环次数
    page = soup_first.find('div', {'class': 'page'}).findAll('a')
    maxPage = page[-2].get_text()
    urls = []
    for i in range(1,(int(maxPage)+1)):
        urls.append(ip + "index_" + str(i) + '.jhtml')
    return urls


if __name__ == '__main__':
    url = 'http://apps.xikang.com/fpzlff/index.jhtml'
    # getNavUrl(url)
    getArticleList(url)
    pass







