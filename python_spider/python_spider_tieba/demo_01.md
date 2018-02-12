## python 爬取百度贴吧某818贴子

### 爬取818帖子

``` python
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/12 12:25
# @Author  : glacier
# @Site    : 
# @File    : tieba.py
# @Software: PyCharm Edu

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

# 过滤
def re_test(text):
    re_h = re.compile('</?\w+[^>]*>')
    s = re_h.sub('',text)
    return s

# 抓取
def bs_test(text):
    soup = BeautifulSoup(text,"lxml")
    contents = soup.find_all('div',{'class':'d_post_content j_d_post_content '})
    return contents

# 保存
def save_text(text):
    import os
    with open('tieba.txt',"a+",encoding='utf-8') as t:
        t.write(text)
        t.close()

if __name__ == '__main__':
    for i in range(29):
        url = "https://tieba.baidu.com/p/2562739391?see_lz=1&pn="+str(i+1)
        req_text = s.get(url).text

        bsText = bs_test(req_text)
        reText = re_test(str(bsText))
        save_text(reText.lstrip())
    print('爬取完成')
```

### 词云分析高频词

``` python
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/12 11:01
# @Author  : glacier
# @Site    : 
# @File    : wordCloud.py
# @Software: PyCharm Edu

from os import path
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import chardet

from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

d = path.dirname(__file__)

# Read the whole text.

with open(u'tieba.txt',encoding='utf-8') as t:
    text = t.read()

# read the mask / color image taken from
# http://jirkavinse.deviantart.com/art/quot-Real-Life-quot-Alice-282261010
alice_coloring = np.array(Image.open(path.join(d, "flower.png")))

# 设置停用词
stopwords = set(STOPWORDS)
stopwords.add("said")

# 你可以通过 mask 参数 来设置词云形状
wc = WordCloud(background_color="white",
               font_path="C:\Windows\Fonts\SIMYOU.TTF",
               max_words=2000,
               mask=alice_coloring,
               stopwords=stopwords,
               max_font_size=40,
               random_state=42)
# generate word cloud
wc.generate(text)

# create coloring from image
image_colors = ImageColorGenerator(alice_coloring)

# show
# 在只设置mask的情况下,你将会得到一个拥有图片形状的词云
plt.imshow(wc, interpolation="bilinear")
plt.axis("off")
plt.figure()
# recolor wordcloud and show
# we could also give color_func=image_colors directly in the constructor
# 我们还可以直接在构造函数中直接给颜色
# 通过这种方式词云将会按照给定的图片颜色布局生成字体颜色策略
plt.imshow(wc.recolor(color_func=image_colors), interpolation="bilinear")
plt.axis("off")
plt.figure()
plt.imshow(alice_coloring, cmap=plt.cm.gray, interpolation="bilinear")
plt.axis("off")
plt.show()
```

### 效果展示

![](http://ovh6566rp.bkt.clouddn.com/Figure_2-2.png)

