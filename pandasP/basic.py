#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/27 17:30
# @Author  : milittle
# @Site    : www.weaf.top
# @File    : basic.py
# @Software: PyCharm

# pandas核心就是Series和DataFrame
'''
* 本py文件介绍了Series和DataFrame的基本组成，以及方法
'''

import pandas as pd
import numpy as np


# 基本Series，索引从0到4，数据从1-5
s1 = pd.Series([1, 2, 3, 4, 5])
print(s1)

# 指定索引，然后对应数据
s2 = pd.Series([1, 2, 3., 4.], index=['a', 'b', 'c', 'd'])
print(s2)
print(s2.index)
print(s2.values)
print(s2[['a', 'b']])
print('a' in s2)

# Series 可以看成一个定长的dict， 因为构建Series以后，Series就不可以改变
d1 = {'a': 1., 'd': 2, 'b': 3, 'c': 4}
s3 = pd.Series(d1)
print(s3)

#DataFrame,二维结构
data = {
    'year' : [2014, 2015, 2016, 2017],
    'income' : [10000, 30000, 50000, 80000],
    'pay' : [5000, 20000, 30000, 30000]
}

# 从dict二维数据中构造DataFrame
df1 = pd.DataFrame(data)
print(df1)

# 从numpy array来构造DataFrame
df2 = pd.DataFrame(np.arange(12).reshape((3, 4)))
print(df2)

# 从numpy array来构造DataFrame，指定index值，和columns值
df3 = pd.DataFrame(np.arange(12).reshape((3, 4)), index=['a', 'b', 'd'], columns=[2, 44, 5, 22])
print(df3)

print(df1.columns) # 列信息
print(df2.index) # 索引信息
print(df1.values)# 值信息
print(df1.describe()) # 包括统计信息，最大值，最小值，均值，方差等等
print(df1.T) # 转置
print(df3.sort_index(axis=1)) # 列排序
print(df3.sort_index(axis=0)) # 行排序
print(df3.sort_values(by=44)) # 根据具体排序

