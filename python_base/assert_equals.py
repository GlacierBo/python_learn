#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/15 10:24
# @Author  : glacier
# @Site    : 出现多次的字符用')'出现一次的字符用'('代替
# @File    : assert_equals.py
# @Software: PyCharm Edu


def duplicate_encode(word):
    return   "".join(["(" if word.lower().count(c) == 1 else ")" for c in word.lower()])



if __name__ == '__main__':
    word = "din"
    duplicate_encode(word)








