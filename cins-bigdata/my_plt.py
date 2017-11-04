# -*- coding: utf-8 -*-
# @Time    : 2017-11-03 13:43
# @Author  : Storm
# @File    : my_plt.py

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

dataTrain = pd.read_csv('./data/train.csv', header=-1)  # 读取训练集
trainX = dataTrain.iloc[:, 0:8].as_matrix()
trainY = dataTrain.iloc[:, 8].as_matrix()
# 划分训练集一部分为测试集
trainX_split, testX_split, trainY_split, testY_split = \
    train_test_split(trainX, trainY, test_size=0.33, random_state=18)

# 作图看各自变量对结果的影响
a = dataTrain[0]
b = dataTrain[1]
c = dataTrain[2]
d = dataTrain[3]
e = dataTrain[4]
f = dataTrain[5]
g = dataTrain[6]
h = dataTrain[7]
o = dataTrain[8]

# 1.所有因素分别对结果的影响
plt.figure()
plt.subplot(421), plt.scatter(a, o)
plt.subplot(422), plt.scatter(b, o)
plt.subplot(423), plt.scatter(c, o)
plt.subplot(424), plt.scatter(d, o)
plt.subplot(425), plt.scatter(e, o)
plt.subplot(426), plt.scatter(f, o)
plt.subplot(427), plt.scatter(g, o)
plt.subplot(428), plt.scatter(h, o)
# plt.savefig('0_all_plt.png')
plt.show()

# 2.标记噪声位置
# a
plt.figure()
plt.scatter(a, o)
plt.xlabel("a")
plt.ylabel("i")
plt.title("a_plt")
plt.plot([-0.5, -0.5], [-0.2, 0.8], 'r')
plt.plot([0.5, 0.5], [-0.2, 0.8], 'r')
plt.plot([-0.5, 0.5], [-0.2, -0.2], 'r')
plt.plot([-0.5, 0.5], [0.8, 0.8], 'r')
plt.savefig('01_00_a_plt.png')
plt.show()

# b
plt.figure()
plt.scatter(b, o)
plt.xlabel("b")
plt.ylabel("i")
plt.title("b_plt")
plt.plot([-0.5, -0.5], [-0.2, 0.8], 'r')
plt.plot([0.5, 0.5], [-0.2, 0.8], 'r')
plt.plot([-0.5, 0.5], [-0.2, -0.2], 'r')
plt.plot([-0.5, 0.5], [0.8, 0.8], 'r')
plt.savefig('01_01_b_plt.png')
plt.show()

# c
plt.figure()
plt.scatter(c, o)
plt.xlabel("c")
plt.ylabel("i")
plt.title("c_plt")
plt.plot([-0.5, -0.5], [-0.2, 0.8], 'r')
plt.plot([0.5, 0.5], [-0.2, 0.8], 'r')
plt.plot([-0.5, 0.5], [-0.2, -0.2], 'r')
plt.plot([-0.5, 0.5], [0.8, 0.8], 'r')
plt.savefig('01_02_c_plt.png')
plt.show()

# d
plt.figure()
plt.scatter(d, o)
plt.xlabel("d")
plt.ylabel("i")
plt.title("d_plt")
plt.plot([-0.5, -0.5], [-0.2, 0.8], 'r')
plt.plot([0.5, 0.5], [-0.2, 0.8], 'r')
plt.plot([-0.5, 0.5], [-0.2, -0.2], 'r')
plt.plot([-0.5, 0.5], [0.8, 0.8], 'r')
plt.savefig('01_03_d_plt.png')
plt.show()

# e
plt.figure()
plt.scatter(e, o)
plt.xlabel("e")
plt.ylabel("i")
plt.title("e_plt")
plt.plot([2, 2], [-0.2, 0.8], 'r')
plt.plot([30, 30], [-0.2, 0.8], 'r')
plt.plot([2, 30], [-0.2, -0.2], 'r')
plt.plot([2, 30], [0.8, 0.8], 'r')
plt.savefig('01_04_e_plt.png')
plt.show()

# f
plt.figure()
plt.scatter(f, o)
plt.xlabel("f")
plt.ylabel("i")
plt.title("f_plt")
plt.plot([2, 2], [-0.2, 0.8], 'r')
plt.plot([25, 25], [-0.2, 0.8], 'r')
plt.plot([2, 25], [-0.2, -0.2], 'r')
plt.plot([2, 25], [0.8, 0.8], 'r')
plt.savefig('01_05_f_plt.png')
plt.show()

# g
plt.figure()
plt.scatter(g, o)
plt.xlabel("g")
plt.ylabel("i")
plt.title("g_plt")
plt.plot([0, 0], [-0.2, 0.8], 'r')
plt.plot([1, 1], [-0.2, 0.8], 'r')
plt.plot([0, 1], [-0.2, -0.2], 'r')
plt.plot([0, 1], [0.8, 0.8], 'r')
plt.savefig('01_06_g_plt.png')
plt.show()
