# -*- coding: utf-8 -*-
# @Time    : 2017-11-04 13:13
# @Author  : Storm
# @File    : my_plt_02.py


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

plt.figure()
plt.scatter(a, o)
plt.savefig('02_00_a_plt.png')
plt.figure()
plt.scatter(b, o)
plt.savefig('02_01_b_plt.png')
plt.figure()
plt.scatter(c, o)
plt.savefig('02_02_c_plt.png')
plt.figure()
plt.scatter(d, o)
plt.savefig('02_03_d_plt.png')
plt.figure()
plt.scatter(e, o)
plt.savefig('02_04_e_plt.png')
plt.figure()
plt.scatter(f, o)
plt.savefig('02_05_f_plt.png')
plt.figure()
plt.scatter(g, o)
plt.savefig('02_06_g_plt.png')
plt.figure()
plt.scatter(h, o)
plt.savefig('02_07_h_plt.png')
plt.show()
