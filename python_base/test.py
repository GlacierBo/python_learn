#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/15 12:25
# @Author  : glacier
# @Site    : 
# @File    : test.py
# @Software: PyCharm Edu



def normalize(name):
    n = name.lower().capitalize()
    return n
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)