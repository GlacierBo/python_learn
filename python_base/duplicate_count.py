#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/15 13:26
# @Author  : glacier
# @Site    : 
# @File    : duplicate_count.py
# @Software: PyCharm Edu

from itertools import groupby


def duplicate_count(text):
    # text = text.lower()
    # print(text)
    # tt = []
    # for i in text:
    #    if text.count(i) != 1:
    #        i in tt[:] or tt.append(i)
    # return len(tt)
    return len( [c for c in set(text.lower()) if text.lower().count(c)>1] )




duplicate_count("ABBA")
