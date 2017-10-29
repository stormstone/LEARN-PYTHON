# -*- coding: utf-8 -*-
# @Time    : 2017-10-29 17:13
# @Author  : Storm
# @File    : z_mytest_keras.py

import pandas as pd
import numpy as np
from numpy import corrcoef
from keras.models import Sequential
from keras.layers.core import Dense, Activation, Dropout

dataTrain = pd.read_csv('./data/mytest_trainData.csv')  # 读取训练集
trainX = dataTrain.iloc[:, 1:9].as_matrix()
trainY = dataTrain.iloc[:, 9].as_matrix()

trainX2 = dataTrain.iloc[:1800, 1:9].as_matrix()
trainY2 = dataTrain.iloc[:1800, 9].as_matrix()
testX2 = dataTrain.iloc[1800:2000, 1:9].as_matrix()
trueY2 = dataTrain.iloc[1800:2000, 9].as_matrix()

dataTest = pd.read_csv('./data/mytest_testData.csv')  # 读取测试集
testX = dataTest.iloc[:, 1:9].as_matrix()
dataTrue = pd.read_csv('./data/mytest_trueResult.csv')  # 读取正确答案
trueY = dataTrue.iloc[:, 9].as_matrix()

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
kerasmodle.fit(trainX2, trainY2, epochs=200, batch_size=16)
res_keras = kerasmodle.predict(testX2, batch_size=16)
print('keras结果：', res_keras)

# end.计算相关性
print('真实结果：', trueY2)
print('keras相关性：', corrcoef(np.reshape(res_keras, (1, 200)), trueY2))
