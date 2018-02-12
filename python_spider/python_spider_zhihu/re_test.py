#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/17 12:23
# @Author  : glacier
# @Site    : 
# @File    : re_test.py
# @Software: PyCharm Edu

import re

def re_text(text):
    href = re.findall('href="(.*?)"',text)
    title = re.findall('"_blank">(.*?)<',text)
    print("href: %s title: %s" %(str(href[0]),str(title[0])))




if __name__ == '__main__':
    str1 = '<a class="question_link" data-id="1513266" data-za-element-name="Title" ' \
           'href="/question/23329834" target="_blank">迄今为止，你拍过最棒的一张照片？</a>'

    re_text(str1)

