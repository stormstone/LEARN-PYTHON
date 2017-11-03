# -*- coding: utf-8 -*-
# @Time    : 2017-11-03 12:47
# @Author  : Storm
# @File    : mytest.py

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.neural_network import MLPRegressor
from sklearn.tree import DecisionTreeRegressor
from keras.models import Sequential
from keras.layers.core import Dense, Activation, Dropout

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
# plt.show()

# 2.线性回归
lr = LinearRegression()  # 建立LR模型
lr.fit(trainX_split, trainY_split)
res_lr = lr.predict(testX_split)
print('线性回归预测结果:', res_lr)

# 3.神经网络
net = MLPRegressor(hidden_layer_sizes=12, max_iter=1000).fit(trainX_split, trainY_split)
res_net = net.predict(testX_split)
print('神经网络预测结果:', res_net)

# 4.决策树
dtr = DecisionTreeRegressor()
dtr.fit(trainX_split, trainY_split)
res_dtr = dtr.predict(testX_split)
print('决策树预测结果：', res_dtr)

# 6.keras
kerasmodle = Sequential()
kerasmodle.add(Dense(32, input_dim=8))
kerasmodle.add(Activation('relu'))
kerasmodle.add(Dropout(0.5))
kerasmodle.add(Dense(64, input_dim=32))
kerasmodle.add(Activation('tanh'))
kerasmodle.add(Dropout(0.5))
kerasmodle.add(Dense(1, input_dim=64))
kerasmodle.add(Activation('linear'))
kerasmodle.compile(loss='mean_squared_error', optimizer='sgd')
kerasmodle.fit(trainX_split, trainY_split, epochs=200, batch_size=16)
res_keras = kerasmodle.predict(testX_split, batch_size=16)
print('keras结果：', res_keras)

# end.计算相关性
print('划分测试集真实结果：', testY_split)
print('===================================================')
print('线性回归参数：', lr.coef_)
print('线性回归相关性：', np.corrcoef(res_lr, testY_split))
print('神经网络相关性：', np.corrcoef(res_net, testY_split))
print('决策树相关性：', np.corrcoef(res_dtr, testY_split))
print('keras相关性：', np.corrcoef(np.reshape(res_keras, (1, len(testY_split))), testY_split))
