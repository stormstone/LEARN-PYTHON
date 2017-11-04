# -*- coding: utf-8 -*-
# @Time    : 2017-11-03 13:37
# @Author  : Storm
# @File    : my_net.py

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPRegressor

dataTrain = pd.read_csv('./data/train.csv', header=-1)  # 读取训练集
trainX = dataTrain.iloc[:, 0:8].as_matrix()
trainY = dataTrain.iloc[:, 8].as_matrix()

trainX_denoising = dataTrain.iloc[:1999, 0:8].as_matrix() #0.72762773
# trainX_denoising = dataTrain.iloc[:1999, 4:8].as_matrix() #0.6215849
# trainX_denoising = dataTrain.iloc[:1999, 4:7].as_matrix() #0.56980478
trainY_denoising = dataTrain.iloc[:1999, 8].as_matrix()

# 划分训练集一部分为测试集
trainX_split, testX_split, trainY_split, testY_split = \
    train_test_split(trainX_denoising, trainY_denoising, test_size=0.13, random_state=18)

net = MLPRegressor(hidden_layer_sizes=16, max_iter=1000).fit(trainX_split, trainY_split)
res_net = net.predict(testX_split)
print('神经网络预测结果:', res_net)

# end.计算相关性
print('划分测试集真实结果：', testY_split)
print('===================================================')
print('神经网络相关性：', np.corrcoef(res_net, testY_split))
