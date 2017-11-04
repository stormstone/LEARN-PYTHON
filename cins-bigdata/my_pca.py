# -*- coding: utf-8 -*-
# @Time    : 2017-11-04 13:33
# @Author  : Storm
# @File    : my_pca.py

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.decomposition import PCA

dataTrain = pd.read_csv('./data/train.csv', header=-1)  # 读取训练集
trainX = dataTrain.iloc[:, 0:8].as_matrix()
trainY = dataTrain.iloc[:, 8].as_matrix()

trainX_denoising = dataTrain.iloc[:1999, 0:8].as_matrix()
trainY_denoising = dataTrain.iloc[:1999, 8].as_matrix()

# 划分训练集一部分为测试集
trainX_split, testX_split, trainY_split, testY_split = \
    train_test_split(trainX_denoising, trainY_denoising, test_size=0.13, random_state=18)

# 1.pca
pca = PCA()
pca.fit(trainX_denoising)
print(pca.components_)
print(pca.explained_variance_ratio_)
# 结果
# [ 0.47081104  0.44818543  0.06283937  0.00421227  0.00409331  0.00404064 0.00385838  0.00195956]
# 前三个占98%以上

# 重新建立pca模型，设置n_components = 3
pca = PCA(3)
pca.fit(trainX_denoising)
# 降维
low_d = pca.transform(trainX_denoising)
pd.DataFrame(low_d).to_csv('./data/train_low_d.csv', header=None, index=None)
