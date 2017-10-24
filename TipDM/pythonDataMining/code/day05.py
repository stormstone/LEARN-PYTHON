# -*- coding: utf-8 -*-
# @Time    : 2017-10-24 16:44
# @Author  : Storm
# @File    : day05.py


## 神经网络
from sklearn.datasets import load_iris
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix

iris = load_iris()
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target)
mlp = MLPClassifier(hidden_layer_sizes=8, max_iter=1000)
mlp.fit(X_train, y_train)
confusion_matrix = confusion_matrix(y_test, mlp.predict(X_test))  # 混淆矩阵
# print(confusion_matrix)
print(classification_report(y_test, mlp.predict(X_test)))  # 分类报告

mlp.coefs_  # 权重
mlp.intercepts_  # 偏差
len(mlp.coefs_)  # 2
a = mlp.coefs_[0]  # 4*8
b = mlp.coefs_[1]  # 8*3
len(mlp.intercepts_)  # 2
c = mlp.intercepts_[0]  # 8
d = mlp.intercepts_[1]  # 3

# kNN
from sklearn.neighbors import KNeighborsClassifier

iris = load_iris()
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target)
kNN = KNeighborsClassifier(n_neighbors=6)
kNN.fit(X_train, y_train)
# confusion_matrix(y_test,kNN.predict(X_test))
print('kNN:', kNN.score(X_test, y_test))
print(classification_report(y_test, kNN.predict(X_test)))  # 分类报告

## 朴素贝叶斯
# 高斯朴素贝叶斯
import numpy as np
from sklearn.naive_bayes import GaussianNB

X = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
Y = np.array([1, 1, 1, 2, 2, 2])
gnb = GaussianNB()
gnb.fit(X, Y)
print(gnb.predict([[4, 2]]))  # 预测
print(gnb.class_prior_)  # 每一类的概率

# 多项式朴素贝叶斯
from sklearn.naive_bayes import MultinomialNB

X = np.random.randint(5, size=(6, 100))
y = np.array([1, 2, 3, 4, 5, 6])
mnb = MultinomialNB()
mnb.fit(X, y)
X1 = np.random.randint(5, size=(6, 100))
print(mnb.predict(X1))

# 高斯朴素贝叶斯对iris数据集进行分类
from sklearn import datasets
from sklearn.naive_bayes import GaussianNB  # 使用高斯贝叶斯模型

iris = datasets.load_iris()  # 读取iris数据集
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target)
gnb = GaussianNB()  # 设置分类器
gnb.fit(iris.data, iris.target)  # 训练分类器
y_pred = gnb.predict(iris.data)  # 预测
print("Number of mislabeled points out of a total %d points : %d" % (iris.data.shape[0], (iris.target != y_pred).sum()))
