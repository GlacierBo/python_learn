#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/14 15:08
# @Author  : glacier
# @Site    : 
# @File    : tianmao.py
# @Software: PyCharm Edu


import requests
import re


if __name__ == '__main__':

    urls = []
    for i in range(400):
        urls.append("https://rate.tmall.com/list_detail_rate.htm?itemId=544539102631&spuId=719737009&sellerId=3077671836&order=100&currentPage=1"+str(i)+"")

    # 构建字段容器
    nickname = []
    ratedate = []
    color = []
    ratecontent = []

    # 循环抓取数据

    for url in urls:
        content = requests.get(url).text
        # 借助正则表达式使用findall进行匹配查询
        nickname.extend(re.findall('"displayUserNick":"(.*?)"',content))
        color.extend(re.findall(re.compile('"颜色分类:(.*?)"'),content))
        ratecontent.extend(re.findall(re.compile('"rateContent":"(.*?)","rateDate"'),content))
        ratedate.extend(re.findall(re.compile('"rateDate":"(.*?)","reply"'),content))

        # 写入数据
        file =open('time.txt','w',encoding='utf-8')

        for i in list(range(0,len(nickname))):
            print("正在写入第 %s 条数据"% i)
            file.write(''.join(ratedate[i])+'\n')
        file.close()

    print("爬取完成")






