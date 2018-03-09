#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/9 11:44
# @Author  : glacier
# @Site    : 
# @File    : anjuke-ks-pandas.py
# @Software: PyCharm Edu


import pandas as pd

data = pd.read_csv('anjuke-ks-tocsv.csv')

print(data['小区'])



