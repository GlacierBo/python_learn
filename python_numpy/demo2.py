#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/8 14:06
# @Author  : glacier
# @Site    : 
# @File    : demo2.py
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
theta = np.arange(0, 2 * np.pi, 2 * np.pi / 100)
theta = np.append(theta, [2 * np.pi])
x = np.cos(theta)
y = np.sin(theta)
v = np.linspace(0, 10, 100)
for r in v:
    x1 = r * x
    y1 = r * y
    plt.plot(x1, y1)
plt.show()