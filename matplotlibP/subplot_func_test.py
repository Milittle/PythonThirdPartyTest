#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/7 11:23
# @Author  : milittle
# @Site    : www.weaf.top
# @File    : subplot_func_test.py
# @Software: PyCharm

'''
func:
subplot(nrows, ncols, index, **kwargs)

In the current figure, create and return an Axes,
at position index of a (virtual) grid of nrows by ncols axes.
Indexes go from 1 to nrows * ncols, incrementing in row-major order.

在这个figure中，创建一个axes，格子的index是由nrows和ncols的相乘而得
index是从1 到 nrows * ncols这么多组成

'''

import numpy as np
import matplotlib.pyplot as plt


def f(t):
    return np.exp(-t) * np.cos(2*np.pi*t)


t1 = np.arange(0.0, 3.0, 0.01)

ax1 = plt.subplot(212) # 代表的是2, 1, 2
ax1.margins(0.05)
ax1.plot(t1, f(t1), 'k')

ax2 = plt.subplot(221)
ax2.margins(0, 0.25)
ax2.plot(t1, f(t1), 'r')
ax2.set_title('Zoomed out')

ax3 = plt.subplot(222)
ax3.margins(x=0, y=0.25)
ax3.plot(t1, f(t1), 'g')
ax3.set_title('Zoomed in')

plt.show()