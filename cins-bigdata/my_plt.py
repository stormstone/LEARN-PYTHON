# -*- coding: utf-8 -*-
# @Time    : 2017-11-03 13:43
# @Author  : Storm
# @File    : my_plt.py


import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

dataTrain = pd.read_csv('./data/train.csv', header=-1)  # 读取训练集
trainX = dataTrain.iloc[:, 0:8].as_matrix()
trainY = dataTrain.iloc[:, 8].as_matrix()

# 划分训练集一部分为测试集
trainX_split, testX_split, trainY_split, testY_split = \
    train_test_split(trainX, trainY, test_size=0.33, random_state=18)

# 1.作图看各自变量对结果的影响
a = dataTrain[0]
b = dataTrain[1]
c = dataTrain[2]
d = dataTrain[3]
e = dataTrain[4]
f = dataTrain[5]
g = dataTrain[6]
h = dataTrain[7]
o = dataTrain[8]
plt.figure()
plt.subplot(421)
plt.scatter(a, o)
plt.subplot(422)
plt.scatter(b, o)
plt.subplot(423)
plt.scatter(c, o)
plt.subplot(424)
plt.scatter(d, o)
plt.subplot(425)
plt.scatter(e, o)
plt.subplot(426)
plt.scatter(f, o)
plt.subplot(427)
plt.scatter(g, o)
plt.subplot(428)
plt.scatter(h, o)
plt.show()
