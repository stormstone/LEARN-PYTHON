# -*- coding: utf-8 -*-
# @Time    : 2017-11-03 13:47
# @Author  : Storm
# @File    : a_first.py


import pandas as pd
from sklearn.neural_network import MLPRegressor

dataTrain = pd.read_csv('./data/train.csv', header=-1)  # 读取训练集
trainX = dataTrain.iloc[:, 0:8].as_matrix()
trainY = dataTrain.iloc[:, 8].as_matrix()

dataTest = pd.read_csv('./data/test.csv', header=-1)  # 读取测试集

# 神经网络
net = MLPRegressor(hidden_layer_sizes=12, max_iter=1000).fit(trainX, trainY)
res_net = net.predict(dataTest)
# print('神经网络预测结果:', res_net)
dataResult = pd.DataFrame(res_net)
# print(dataResult)
dataResult.to_csv('./data/first_answer.csv', header=None, index=None)
