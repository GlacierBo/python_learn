#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/8 14:05
# @Author  : glacier
# @Site    : 
# @File    : demo1.py
# @Software: PyCharm Edu
import numpy as np
import matplotlib.pyplot as plt
# 该行用于设置chart 的样式，可以注掉

fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot(111)
ax.spines['left'].set_color('none')
ax.spines['bottom'].set_color('none')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.set_xticks([])
ax.set_yticks([])
# 实现功能
theta = np.arange(0, 2 * np.pi + 0.1,2 * np.pi / 1000)
x = np.cos(theta)
y = np.sin(theta)
v = np.linspace(0, 10, 100)
v.shape = (100, 1)
x = v * x
y = v * y
plt.plot(x, y, color='red')
plt.show()