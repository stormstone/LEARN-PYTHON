# -*- coding: utf-8 -*-
# @Time    : 2017-10-27 22:04
# @Author  : Storm
# @File    : z_mytest.py

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.linear_model import LinearRegression
from sklearn.neural_network import MLPRegressor
from sklearn.tree import DecisionTreeRegressor
from keras.models import Sequential
from keras.layers.core import Dense, Activation, Dropout

dataTrain = pd.read_csv('./data/mytest_trainData.csv')  # 读取训练集
trainX = dataTrain.iloc[:, 1:9].as_matrix()
trainY = dataTrain.iloc[:, 9].as_matrix()
dataTest = pd.read_csv('./data/mytest_testData.csv')  # 读取测试集
testX = dataTest.iloc[:, 1:9].as_matrix()
dataTrue = pd.read_csv('./data/mytest_trueResult.csv')  # 读取正确答案
trueY = dataTrue.iloc[:, 9].as_matrix()

# 1.作图看各自变量对结果的影响
a = dataTrain['a']
b = dataTrain['b']
c = dataTrain['c']
d = dataTrain['d']
e = dataTrain['e']
f = dataTrain['f']
g = dataTrain['g']
h = dataTrain['h']
o = dataTrain['o']
plt.figure()
plt.subplot(421)
plt.scatter(a, o)
plt.subplot(422)
plt.scatter(a, o)
plt.subplot(423)
plt.scatter(a, o)
plt.subplot(424)
plt.scatter(a, o)
plt.subplot(425)
plt.scatter(a, o)
plt.subplot(426)
plt.scatter(a, o)
plt.subplot(427)
plt.scatter(a, o)
plt.subplot(428)
plt.scatter(a, o)
# plt.show()

# 2.主成分分析 PCA
pca = PCA()

# 3.线性回归
lr = LinearRegression()  # 建立LR模型
lr.fit(trainX, trainY)
res_lr = lr.predict(testX)
print('线性回归预测结果:', res_lr)

# 4.神经网络
net = MLPRegressor(hidden_layer_sizes=12, max_iter=1000).fit(trainX, trainY)
res_net = net.predict(testX)
print('神经网络预测结果:', res_net)

# 5.决策树
dtr = DecisionTreeRegressor()
dtr.fit(trainX, trainY)
res_dtr = dtr.predict(testX)
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
kerasmodle.fit(trainX, trainY, epochs=200, batch_size=16)
res_keras = kerasmodle.predict(testX, batch_size=16)
print('keras结果：', res_keras)

# end.计算相关性
print('真实结果', trueY)
print('===================================================')
print('线性回归参数：', lr.coef_)
print('线性回归相关性：', np.corrcoef(res_lr, trueY))
print('神经网络相关性：', np.corrcoef(res_net, trueY))
print('决策树相关性：', np.corrcoef(res_dtr, trueY))
print('keras相关性：', np.corrcoef(np.reshape(res_keras, (1, 200)), trueY))
