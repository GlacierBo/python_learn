#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/15 12:22
# @Author  : glacier
# @Site    : 
# @File    : add_binary.py
# @Software: PyCharm Edu

import re


def add_binary(a,b):
    s = a+b
    return str(bin(s))


add_binary(51,12)
