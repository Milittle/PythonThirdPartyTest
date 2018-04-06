#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/6 20:54
# @Author  : milittle
# @Site    : www.weaf.top
# @File    : numpy_test.py
# @Software: PyCharm

import numpy as np
from numpy import linalg


# 创建数组
def create_num():
    a = np.array([1,2,3,4,5,6])
    print('before:', a)
    # 直接给a.shape赋值是最简单的变形方式
    a.shape = (2,3)
    print('after：', a)

    b = a.ravel()  # 注意这里是返回值，本身a没有改变

    print('flat：', b)


# 按列拼接
def num_combine_by_h(*args):
    S = args[0]
    for i in args[1:]:
        S = np.hstack([S, i])
    return S

def num_combine_by_v(*args):
    S = args[0]
    for i in args[1:]:
        S = np.vstack([S, i])
    return S


def basic_operation():
    print(np.exp(2))
    print(np.exp2(2))
    print(np.sqrt(4))
    print(np.sin([2, 4]))
    print(np.log10(2))
    print(np.log(2))
    print(np.log2(2))
    print(np.max([1, 2, 3, 4]))




A = np.floor(np.random.randn(2,3) * 10)
print('A:\n', A)
B = np.floor(np.random.randn(2,3) * 10)
print('B:\n', B)
C = np.floor(np.random.randn(2,3) * 10)
print('C:\n', C)



A = np.array([[1, 2], [-1, 4]])
B = np.array([[2, 0], [3, 4]])
print('对应元素想乘：', A * B)
print('矩阵乘法:', np.dot(A, B))
# or print(A.dot(B))


# 求A的转置
print ('A的转置:', A.transpose())
# 求A的逆矩阵
print('A的逆矩阵：', linalg.inv(A))
# 特征值和特征向量
eigenvalues, eigenvectors = linalg.eig(A)
print('A 的特征值：', eigenvalues)
print('A 的特征向量：', eigenvectors)

if __name__ == '__main__':
    basic_operation()





