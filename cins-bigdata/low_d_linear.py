# -*- coding: utf-8 -*-
# @Time    : 2017-11-04 14:11
# @Author  : Storm
# @File    : low_d_linear.py

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

dataTrain_low_d = pd.read_csv('./data/train_low_d.csv', header=-1)  # 读取训练集
trainX = dataTrain_low_d.as_matrix()
dataTrain = pd.read_csv('./data/train.csv', header=-1)  # 读取训练集
trainY = dataTrain.iloc[:, 8].as_matrix()
trainY_denoising = dataTrain.iloc[:1999, 8].as_matrix()

# 划分训练集一部分为测试集
trainX_split, testX_split, trainY_split, testY_split = \
    train_test_split(trainX, trainY_denoising, test_size=0.13, random_state=18)

# 2.线性回归
lr = LinearRegression()  # 建立LR模型
lr.fit(trainX_split, trainY_split)
res_lr = lr.predict(testX_split)
print('线性回归预测结果:', res_lr)

print('划分测试集真实结果：', testY_split)
print('===================================================')
print('线性回归参数：', lr.coef_)
print('线性回归相关性：', np.corrcoef(res_lr, testY_split))  # 0.81675171
