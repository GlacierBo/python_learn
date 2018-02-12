#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/15 13:15
# @Author  : glacier
# @Site    : 
# @File    : get_middle.py
# @Software: PyCharm Edu






# def get_middle(s):
#     # 偶数
#     if len(s)%2 == 0:
#         return s[int(len(s)/2-1)]+s[int(len(s)/2)]
#     else:
#         # 奇数
#         return s[int(len(s)/2)]

def get_middle(s):
    print(s[(len(s)-1)//2:len(s)//2+1])

get_middle("testi")


