# -*- coding: utf-8 -*-
# @Time    : 2017-11-05 19:20
# @Author  : Storm
# @File    : my_plt_03.py

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

dataTrain = pd.read_csv('./data/train.csv', header=-1)  # 读取训练集
trainX = dataTrain.iloc[:, 0:8].as_matrix()
trainY = dataTrain.iloc[:, 8].as_matrix()

dataTrain_denoising = dataTrain.iloc[0:1999, :]

trainX_denoising = dataTrain.iloc[:1999, 0:8].as_matrix()
trainY_denoising = dataTrain.iloc[:1999, 8].as_matrix()

# 作图看各自变量对结果的影响
a = dataTrain_denoising[0]
b = dataTrain_denoising[1]
c = dataTrain_denoising[2]
d = dataTrain_denoising[3]
e = dataTrain_denoising[4]
f = dataTrain_denoising[5]
g = dataTrain_denoising[6]
h = dataTrain_denoising[7]
o = dataTrain_denoising[8]

e_big_count=0
f_big_count=0
for i in range(len(trainX_denoising)):
    if (e[i]>9):
        e_big_count += 1
    if (f[i]>8):
        f_big_count += 1

print(f_big_count)

# 箱图
# fig = plt.figure()
# ax = fig.add_subplot(111)
# ax.boxplot(d)
# plt.title('d_boxplot')
# plt.grid(True)
# plt.savefig('03_boxplot_d.png')
# plt.show()