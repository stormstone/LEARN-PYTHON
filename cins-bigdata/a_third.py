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

