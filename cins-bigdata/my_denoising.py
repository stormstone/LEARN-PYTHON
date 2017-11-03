# -*- coding: utf-8 -*-
# @Time    : 2017-11-03 16:30
# @Author  : Storm
# @File    : my_denoising.py

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

dataTrain = pd.read_csv('./data/train.csv', header=-1)  # 读取训练集
trainX = dataTrain.iloc[:, 0:8].as_matrix()
trainY = dataTrain.iloc[:, 8].as_matrix()

# 划分训练集一部分为测试集
trainX_split, testX_split, trainY_split, testY_split = \
    train_test_split(trainX, trainY, test_size=0.33, random_state=18)
