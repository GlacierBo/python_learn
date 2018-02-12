#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/15 14:16
# @Author  : glacier
# @Site    : 
# @File    : make_readable.py
# @Software: PyCharm Edu
import time

def make_readable(seconds):

    tt = time.localtime(seconds)
    str1 = time.strftime("%H:%M:%S",tt)

    print(str1)
    # Do something


make_readable(86400)

