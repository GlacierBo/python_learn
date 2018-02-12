#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/12 15:35
# @Author  : glacier
# @Site    : 
# @File    : dangni_word.py
# @Software: PyCharm Edu


from os import path
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import chardet

from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

d = path.dirname(__file__)

# Read the whole text.

with open(u'dangni.txt',encoding='utf-8') as t:
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
