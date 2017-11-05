# -*- coding: utf-8 -*-
# @Time    : 2017-11-05 19:59
# @Author  : Storm
# @File    : a_third.py

import pandas as pd
from sklearn.linear_model import LinearRegression

dataTrain = pd.read_csv('./data/train.csv', header=-1)  # 读取训练集
trainX = dataTrain.iloc[:, 0:8].as_matrix()
trainY = dataTrain.iloc[:, 8].as_matrix()

trainX_denoising = dataTrain.iloc[:1999, 4:7].as_matrix()
trainY_denoising = dataTrain.iloc[:1999, 8].as_matrix()

dataTest = pd.read_csv('./data/test.csv', header=-1)  # 读取测试集
dataTest_lowd = dataTest.iloc[:, 4:7].as_matrix()

lr = LinearRegression()  # 建立LR模型
lr.fit(trainX_denoising, trainY_denoising)
res_lr = lr.predict(dataTest_lowd)
print('线性回归预测结果:', res_lr)

print('===================================================')
print('线性回归参数：', lr.coef_)
dataResult = pd.DataFrame(res_lr)
# print(dataResult)
dataResult.to_csv('./data/my_answer_third.csv', header=None, index=None)

