# -*- coding: utf-8 -*-
# @Time    : 2017-10-15 19:26
# @Author  : Storm
# @File    : numpyTest.py
import numpy as np
from numpy.linalg import *


def main():
    lst = [[1, 3, 5], [2, 4, 5]]
    print(type(lst))
    np_lst = np.array(lst)
    print(type(np_lst))
    np_lst = np.array(lst, dtype=np.float)
    # dtype:bool,int,int8/16/32/64128,uint8,uint32/64/128,float,float16/32/64,complex64/128
    print(np_lst.shape)
    print(np_lst.ndim)
    print(np_lst.dtype)  # float默认64位
    print(np_lst.itemsize)  # 数据类型长度
    print(np_lst.size)  # 元素个数

    # Some Arrays
    print(np.zeros([2, 4]))  # 2行4列的0矩阵
    print(np.ones([3, 5]))
    print("Rand:")
    print(np.random.rand(2, 4))  # 2行4列的随机矩阵
    print(np.random.rand())
    print("RandInt:")
    print(np.random.randint(1, 10, 3))  # 整型，生成1到10随机的3个整数
    print("Randn:")
    print(np.random.randn(2, 4))  # 标准正态
    print("Choice:")
    print(np.random.choice([10, 20, 30]))  # 从给定的列表中随机选择
    print("Distribute:")
    print(np.random.beta(1, 10, 100))  # beta 分布

    # Array Opes
    lst = np.arange(1, 11).reshape([2, -1])
    print("Exp")
    print(np.exp(lst))
    print("Exp2")
    print(np.exp2(lst))
    print("Sqrt")
    print(np.sqrt(lst))
    print("Sin")
    print(np.sin(lst))
    print("Log")
    print(np.log(lst))
    lst = np.array([[[1, 2, 3, 4],
                     [4, 5, 6, 7]],
                    [[7, 8, 9, 10],
                     [10, 11, 12, 13]],
                    [[14, 15, 16, 17],
                     [18, 19, 20, 21]]
                    ])
    print("Sum")
    print(lst.sum(axis=2))  # axis最大为维数减一
    print("Max")
    print(lst.max(axis=1))
    print("Min")
    print(lst.min(axis=0))

    lst1 = np.array([10, 20, 30, 40])
    lst2 = np.array([4, 3, 2, 1])
    print("Add")
    print(lst1 + lst2)
    print("Sub")
    print(lst1 - lst2)
    print("Mul")
    print(lst1 * lst2)
    print("Div")
    print(lst1 / lst2)
    print("Square")
    print(lst1 ** 2)
    print("Dot")
    print(np.dot(lst1.reshape([2, 2]), lst2.reshape([2, 2])))
    print("Concatenate")
    print(np.concatenate((lst1, lst2), axis=0))
    print("Vstack")
    print(np.vstack((lst1, lst2)))
    print("Hstack")
    print(np.hstack((lst1, lst2)))
    print("Split")
    print(np.split(lst1, 4))
    print("Copy")
    print(np.copy(lst1))

    # liner
    print(np.eye(3))
    lst = np.array([[1., 2.], [3., 4.]])
    print("Inv:")
    print(inv(lst))
    print("T:")
    print(lst.transpose())
    print("Det(行列式):")
    print(det(lst))
    print("Eig(特征值，特征向量):")
    print(eig(lst))
    print("Solve(解方程组):")
    y = np.array([[5.], [7.]])
    print(solve(lst, y))

    # others
    print("FFT:")
    print(np.fft.fft(np.array([1, 1, 1, 1, 1, 1, 1, 1])))
    print("Coef:")
    print(np.corrcoef([1, 0, 1], [0, 2, 1]))
    print("Poly:")
    print(np.poly1d([2, 1, 3]))


if __name__ == '__main__':
    main()
