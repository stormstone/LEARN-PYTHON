# -*- coding: utf-8 -*-
# @Time    : 2017-11-03 14:05
# @Author  : Storm
# @File    : my_logistic.py

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import RandomizedLogisticRegression
from sklearn.linear_model import LogisticRegressionCV

dataTrain = pd.read_csv('./data/train.csv', header=-1)  # 读取训练集
trainX = dataTrain.iloc[:, 0:8].as_matrix()
trainY = dataTrain.iloc[:, 8].as_matrix()

# 划分训练集一部分为测试集
trainX_split, testX_split, trainY_split, testY_split = \
    train_test_split(trainX, trainY, test_size=0.33, random_state=18)

# logistic回归
logistic = LogisticRegression()  # 建立LR模型
logistic.fit(trainX_split, trainY_split)
res_logistic = logistic.predict(testX_split)
print('logistic回归预测结果:', res_logistic)

print('划分测试集真实结果：', testY_split)
print('===================================================')
print('logistic回归参数：', res_logistic.coef_)
print('logistic回归相关性：', np.corrcoef(res_logistic, testY_split))
