# -*- coding: utf-8 -*-
# @Time    : 2017-10-26 19:57
# @Author  : Storm
# @File    : day08.py
# 复习课

# 1.神经网络
from sklearn.datasets import load_iris
from random import sample
from sklearn.neural_network import MLPClassifier

iris = load_iris()
# 训练集，分层抽样
tr_idnex = sample(range(0, 50), 40)
tr_idnex.extend(sample(range(50, 100), 40))
tr_idnex.extend(sample(range(100, 150), 40))
# 测试集
te_idnex = [i for i in range(0, 150) if i not in tr_idnex]

x = iris.data[tr_idnex, :]
y = iris.target[tr_idnex]
net = MLPClassifier(hidden_layer_sizes=10, max_iter=1000).fit(x, y)
res = net.predict(iris.data[te_idnex])
print('预测结果:', res)
print('真实值：', iris.target[te_idnex])

#
