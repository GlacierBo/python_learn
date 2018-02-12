#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/15 10:48
# @Author  : glacier
# @Site    : 
# @File    : find_short.py
# @Software: PyCharm Edu




# def find_short(word):
#     temp = word.split(" ")
#     temp_str = temp[0]
#     for i in temp:
#         if len(temp_str) > len(i):
#             temp_str = i
#     print(temp_str)


def find_short(s):
    return min(len(x) for x in s.plit())

if __name__ == '__main__':
    word = "bitcoin take over the world maybe who knows perhaps"
    find_short(word)

