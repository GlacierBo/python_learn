# -*- coding: utf-8 -*-
# @Time    : 2018/3/27 9:31
# @Author  : glacier
# @Email   : 2284711614@qq.com
# @File    : yiliao_vedio_flash.py
# @Software: PyCharm


import re,requests
import traceback
from bs4 import BeautifulSoup
import python_spider_wangjin.download_media as download

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
        return r.content
    except:
        traceback.print_exc()
        return ""

def getHTMLInfo(url):
    # 解析网页
    html_first = getHTMLText(url)
    soup_first = BeautifulSoup(html_first,"html.parser")
    # 获取页码，决定循环次数
    page = soup_first.find('div',{'class':'page'}).findAll('a')
    maxPage = page[-2].get_text()
    urls = getVedioURLS(maxPage=maxPage,url=url)

    for url in urls:
        print(url)
        # 获得视频链接
        html = getHTMLText(url)
        soup = BeautifulSoup(html, "html.parser")
        videoDiv = soup.find('div',{'class':'main_video_col2'})
        # 获取分类
        type = videoDiv.find('div',{'class':'main_video_col2_tit'}).get_text()
        videoLis = videoDiv.findAll('li')

        for videoLi in videoLis:
            vedio_url = "http://apps.xikang.com" + videoLi.find('a')['href']
            vedio_title = videoLi.find('a')['title']
            vedio_img = videoLi.find('img').attrs['src']
            # print(vedio_img,vedio_url,vedio_title)
            try:
                vedio_resourse = getVedioEmbed(vedio_url)
                print(vedio_resourse)
                print(vedio_title)
                PATH = 'D:/Python_Download/' + vedio_title + '.flv'
                download.do_load_media(url=vedio_resourse,path=PATH)

            except:
                print('视频链接无效')
                continue

    pass

def getVedioURLS(url,maxPage):
    urls = []
    tt = url.replace(url.split('/')[-1],"")
    for i in range(1,(int(maxPage)+1)):
        new_url = tt + 'index_' + str(i) + '.jhtml'
        urls.append(new_url)
    return urls


def getVedioEmbed(url):
    html = getHTMLText(url)
    soup = BeautifulSoup(html, "html.parser")
    embed = soup.find('div',{'id':'player'})
    result = "http://apps.xikang.com" + getRE(embed)
    return result

def getRE(strTxt):
    pattern = re.compile('var filePath = "(.*)"')
    result = pattern.findall(str(strTxt))
    result = result[0].replace("..","")
    return result

def getVedioBigURL():
    urls = {
        'http://apps.xikang.com/kbvideoDiet/index_1.jhtml',
        'http://apps.xikang.com/kbvideosport/index_1.jhtml',
        'http://apps.xikang.com/kbvideoHealthCare/index_1.jhtml',
        'http://apps.xikang.com/kbvideoDisease/index_1.jhtml',
        'http://apps.xikang.com/kbvideoHealthExam/index_1.jhtml',
        'http://apps.xikang.com/kbvideoHotchpotch/index.jhtml'
    }
    return urls

if __name__ == '__main__':
    # http://apps.xikang.com/u/cms/xikang/vedio1/xkll-0001.flv
    # http://apps.xikang.com/u/cms/xikang/vedio1/xkll-0003.flv
    ### 视频链接已找到 http://apps.xikang.com/u/cms/xikang/vedio1/xktj0003.flv
    urls = getVedioBigURL()
    for url in urls:
        html = getHTMLInfo(url)

    print("视频下载完成！")

