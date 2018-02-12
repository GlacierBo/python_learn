#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/15 12:49
# @Author  : glacier
# @Site    : 
# @File    : filter_list.py
# @Software: PyCharm Edu


# def filter_list(l):
#      ll = []
#      for i in l:
#          if type(i) == type(1):
#              ll.append(i)
#      return ll

def filter_list(l):
    return [x for x in l if type(x) is not str]

ll = filter_list([1,2,'aasf','1','123',123])
for i in ll:
    print(i)




