#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/7 10:36
# @Author  : milittle
# @Site    : www.weaf.top
# @File    : plot_function_test.py
# @Software: PyCharm

import matplotlib.pyplot as plt
import math
import numpy as np

"""

参数说明
plot([x], y, [fmt], data=None, **kwargs)
plot([x], y, [fmt], [x2], y2, [fmt2], ..., **kwargs)


:param

[fmt] 的参数格式
fmt = '[color][marker][line]'

color:
character	color
'b'	        blue
'g'	        green
'r'	        red
'c'	        cyan
'm'	        magenta
'y'	        yellow
'k'	        black
'w'	        white

marker:
character	description
'.'	        point marker
','	        pixel marker
'o'	        circle marker
'v'	        triangle_down marker
'^'	        triangle_up marker
'<'	        triangle_left marker
'>'	        triangle_right marker
'1'	        tri_down marker
'2'	        tri_up marker
'3'	        tri_left marker
'4'	        tri_right marker
's'	        square marker
'p'	        pentagon marker
'*'	        star marker
'h'	        hexagon1 marker
'H'	        hexagon2 marker
'+'	        plus marker
'x'	        x marker
'D'	        diamond marker
'd'	        thin_diamond marker
'|'	        vline marker
'_'	        hline marker

line:
character	description
'-'	        solid line style
'--'	    dashed line style
'-.'	    dash-dot line style
':'	        dotted line style


some example:
'b'    # blue markers with default shape
'ro'   # red circles
'g-'   # green solid line
'--'   # dashed line with default color
'k^:'  # black triangle_up markers connected by a dotted line

**kwargs 的参数以及描述

Property	        Description
agg_filter	        a filter function, which takes a (m, n, 3) float array and a dpi value, and returns a (m, n, 3) array
alpha	            float (0.0 transparent through 1.0 opaque)
animated	        bool
antialiased or aa	bool
clip_box	        a Bbox instance
clip_on	            bool
clip_path	        [(Path, Transform) | Patch | None]
color or c	        any matplotlib color
contains	        a callable function
dash_capstyle	    [‘butt’ | ‘round’ | ‘projecting’]
dash_joinstyle	    [‘miter’ | ‘round’ | ‘bevel’]
dashes	            sequence of on/off ink in points
drawstyle	        [‘default’ | ‘steps’ | ‘steps-pre’ | ‘steps-mid’ | ‘steps-post’]
figure	            a Figure instance
fillstyle	        [‘full’ | ‘left’ | ‘right’ | ‘bottom’ | ‘top’ | ‘none’]
gid	                an id string
label	            object
linestyle or ls	    [‘solid’ | ‘dashed’, ‘dashdot’, ‘dotted’ | (offset, on-off-dash-seq) | '-' | '--' | '-.' | ':' | 'None' | ' ' | '']
linewidth or lw	    float value in points
marker	                        A valid marker style
markeredgecolor or mec	        any matplotlib color
markeredgewidth or mew	        float value in points
markerfacecolor or mfc	        any matplotlib color
markerfacecoloralt or mfcalt	any matplotlib color
markersize or ms	            float
markevery	                    [None | int | length-2 tuple of int | slice | list/array of int | float | length-2 tuple of float]
path_effects	                AbstractPathEffect
picker	                        float distance in points or callable pick function fn(artist, event)
pickradius	                    float distance in points
rasterized	                    bool or None
sketch_params	                (scale: float, length: float, randomness: float)
snap	                        bool or None
solid_capstyle	                [‘butt’ | ‘round’ | ‘projecting’]
solid_joinstyle	                [‘miter’ | ‘round’ | ‘bevel’]
transform	                    a matplotlib.transforms.Transform instance
url	                            a url string
visible	                        bool
xdata                           1D array
ydata	                        1D array
zorder	                        float

source url: https://matplotlib.org/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot
"""

# data define
x = [i for i in np.linspace(start = 0, stop = 10, num=500)]
print(type(x[0]))
y = [math.sin(i) for i in x]


def basic():
    plt.plot(x, y) # # plot x and y using default line style and color
    plt.show()


# [fmt] 可以被dict属性代替
def define_line():
    plt.plot(x, y, color='green', marker='o', linestyle='dashed',
            linewidth=2, markersize=1)
    plt.show()

# Plotting labelled data

data = {'x':[1,2,3,4,5,6,7,8,9], 'y':[1,2,3,4,5,6,7,8,9]}

def draw_label_data():
    plt.plot('x', 'y', data = data) # 我们使用了带有标签的data来画我们的图形
    plt.show()

# Plotting multiple sets of data
# 定义多个x, y
# 或者定义一个集合，第一列当作x，其他的当作y

mutil_data = np.array([[1,2,3,4,5,6,7,8,9],[2,3,4,5,6,7,8,9,10],[3,4,5,6,7,8,9,10,11],[4,5,6,7,8,9,10,11,12]])
print(mutil_data.shape)

def draw_mutil_data():
    plt.plot(mutil_data[0], np.transpose(mutil_data[1:]))
    plt.show()

if __name__ == '__main__':
    draw_mutil_data()
