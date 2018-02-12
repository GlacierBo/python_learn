#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/15 9:30
# @Author  : glacier
# @Site    : list 去重
# @File    : unique_in_order.py
# @Software: PyCharm Edu


# unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
# unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
# unique_in_order([1,2,2,3,3])       == [1,2,3]

from itertools import groupby


# def unique_in_order(iterable):
#    new_list = []
#    for i in iterable:
#        if i not in new_list:
#            new_list.append(i)
#    print(new_list)
#    return new_list

def unique_in_order(iterable):
   return  [key for key,value in groupby(iterable)]


if __name__ == '__main__':
    iterable = ('AAAABBBCCDAABBB')
    unique_in_order(iterable)