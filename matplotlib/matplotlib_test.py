#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/6 19:52
# @Author  : milittle
# @Site    : www.weaf.top
# @File    : matplotlib_test.py
# @Software: PyCharm

import matplotlib.pyplot as plt

# plt.xlim()
# plt.ylim()

# 画一个空表的面板
def draw_empty():
    plt.plot()
    plt.show()

# 画xy
def draw_x_y(x, y):
    # x and y must have same dim
    plt.plot(x, y)
    plt.show()

# 画xy和x轴数据的旋转
def draw_x_y_rotation(x, y):
    plt.plot(x, y)
    plt.xticks(rotation = 45) # 让某个轴的数字倾斜
    plt.yticks(rotation = 45)
    plt.show()

# 画标题和label
def draw_xy_title_label(x, y):
    plt.plot(x, y)
    plt.xticks(rotation = 45)
    plt.xlabel('x-axis')
    plt.ylabel('y-axis')
    plt.title('my_test')
    plt.show()

# 同时画两条线
def draw_two_xy(x,y, x1, y1):
    plt.plot(x, y, c = 'r', label = 'red')
    plt.plot(x1, y1, c = 'b', label = 'blue')
    plt.legend(loc = 'best') # 提示
    plt.xlabel('this is x')
    plt.ylabel('this is y')
    plt.title('some test')
    plt.xticks(rotation = 45)
    plt.show()


# 画子图
def draw_subplot(x, y, x1, y1): # 四个子图的实例
    fig = plt.figure(figsize=(16,8)) # 定义子图容器的大小
    a1 = fig.add_subplot(2, 2, 1)
    a2 = fig.add_subplot(2, 2, 2)
    a3 = fig.add_subplot(2, 2, 3)
    a3 = fig.add_subplot(2, 2, 4) # 画出空白面板

    a1.plot(x, y, c = 'r', label = 'red') # 填充信息
    a2.plot(x1, y1, c = 'b', label = 'blue')
    a1.legend(loc = 'best')
    a2.legend(loc = 'best')
    plt.show()

# 画条形图
def draw_bar(bar_pos, bar_hei, width = 0.8):
    plt.bar(bar_pos, bar_hei, width)
    plt.show()


# 画两条bar
def draw_two_bar(bar1_p, bar1_h, bar2_p, bar2_h, width1 = 0.8, width2 = 0.8):
    plt.bar(bar1_p, bar1_h, width = width1, color = 'r', label = 'red')
    plt.bar(bar2_p, bar2_h, width = width2, color = 'b', label = 'blue') # 这里的color和上面的不一致。需要注意
    num_cols = ['first', 'second', 'third', 'four', 'five', 'six']
    plt.xticks(range(1, 7), num_cols, rotation = 45)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('this is bar')
    plt.show()

# 画一个垂直的bar
def draw_vertical(bar_pos, bar_hei, width = 0.8):
    plt.barh(bar_pos, bar_hei, width, color='b', label='blue')  # 这里的color和上面的不一致。需要注意
    num_cols = ['first', 'second', 'third', 'four', 'five', 'six']
    plt.yticks(range(1, 7), num_cols, rotation=45)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('this is bar')
    plt.show()

# 画散点图
def draw_scatter(x, y):
    plt.scatter(x, y)
    plt.show()

# 尝试添加其他属性

def draw_another_profor_scatter(x, y):
    plt.scatter(x, y, marker='x', c = 'r', label = "red")
    plt.xlabel("this is x")
    plt.ylabel("this is y")
    plt.title("this is title")
    plt.xticks(rotation = 45)
    plt.legend(loc = "upper right")
    plt.show()

# 画出直方图
def draw_hist(x):
    plt.hist(x, range = (4, 5), bins = 20) # range决定当前坐标轴的显示区域，bins表示的是这么多数据分成多少块统计
    plt.show()


# 画一个盒图
def draw_box(x):
    plt.boxplot(x)
    plt.show()


x_axis = [794.28818799999999,
         808.50958700000001,
         826.25461900000005,
         833.53230499999995,
         841.97451199999989,
         846.94015999999999,
         851.69061199999987,
         861.97213299999999,
         874.92434100000003,
         888.51824600000009]
y_axis = [79.877565000000004,
         99.524317000000011,
         62.525946999999995,
         57.281737,
         52.371316,
         70.615566000000001,
         47.351207000000002,
         43.719923000000001,
         40.642712000000003,
         38.535789000000001]


x_another = x_axis.copy()

y_another = [i + 10 for i in y_axis]


bar_positions = [1, 2, 3, 4, 5, 6] #每条bar的位置
bar_heights = [2,3,6,1,7,8] #每条bar的高度值


#构造数据
bar_positions = [i+0.9 for i in range(6)]
bar_heights = [2,3,6,1,7,8]
#再构造一组数据
bar_positions2 = [i+1.1 for i in range(6)]
bar_heights2 = bar_heights.copy()


data = [2.7, 2.7, 2.8, 2.8, 2.9, 2.9, 2.9, 2.9, 2.9, 3.0, 3.0, 3.0, 3.0, 3.1, 3.1, 3.1, 3.2, 3.2, 3.2, 3.2, 3.2, 3.3, 3.3, 3.3, 3.3, 3.4, 3.4, 3.4, 3.4, 3.4, 3.4, 3.4, 3.4, 3.4, 3.5, 3.5, 3.5, 3.5, 3.5, 3.5, 3.5, 3.5, 3.5, 3.6, 3.6, 3.6, 3.6, 3.6, 3.6, 3.6, 3.6, 3.7, 3.7, 3.7, 3.7, 3.7, 3.7, 3.7, 3.7, 3.7, 3.8, 3.8, 3.8, 3.8, 3.8, 3.9, 3.9, 3.9, 3.9, 3.9, 3.9, 3.9, 3.9, 3.9, 3.9, 3.9, 3.9, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.1, 4.1, 4.1, 4.1, 4.1, 4.1, 4.1, 4.1, 4.1, 4.1, 4.1, 4.1, 4.1, 4.1, 4.1, 4.1, 4.2, 4.2, 4.2, 4.2, 4.2, 4.2, 4.2, 4.2, 4.2, 4.2, 4.2, 4.2, 4.3, 4.3, 4.3, 4.3, 4.3, 4.3, 4.3, 4.3, 4.3, 4.3, 4.3, 4.4, 4.4, 4.4, 4.4, 4.4, 4.4, 4.4, 4.5, 4.5, 4.5, 4.5, 4.5, 4.5, 4.5, 4.5, 4.5, 4.6, 4.6, 4.6, 4.6, 4.8, 4.8, 4.8]

if __name__ == '__main__':
    draw_box(data)


