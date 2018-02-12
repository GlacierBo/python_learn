#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/15 14:01
# @Author  : glacier
# @Site    : 
# @File    : delete_nth.py
# @Software: PyCharm Edu


def delete_nth(order,max_e):
    tt = []
    for c in order:
        if tt.count(c) < max_e:
            tt.append(c)
    return tt

delete_nth([20,37,20,21], 1)











