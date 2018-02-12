#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/15 11:26
# @Author  : glacier
# @Site    : 二进制计算
# @File    : binary_array_to_number.py
# @Software: PyCharm Edu



# def binary_array_to_number(arr):
#   sum = 0
#   index = len(arr)-1
#   i = 0
#   while(index >= 0):
#      sum += mul(arr[i],index)
#      i += 1
#      index -=1
#   print(sum)
#
# def mul(index,arg2):
#     print(index,arg2)
#     for i in range(arg2):
#         index = index * 2
#     return index

def binary_array_to_number(arr):
    # return int("".join(map(str,arr)),2)
    print("".join(map(str,arr)),2)

binary_array_to_number([0,0,1,1])



