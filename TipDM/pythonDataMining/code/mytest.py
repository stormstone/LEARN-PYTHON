# -*- coding: utf-8 -*-
# @Time    : 2017-10-24 16:55
# @Author  : Storm
# @File    : mytest.py
from sklearn.datasets import load_iris
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix

iris = load_iris()
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target)
mlp = MLPClassifier(hidden_layer_sizes=8, max_iter=1000)
mlp.fit(X_train, y_train)
confusion_matrix = confusion_matrix(y_test, mlp.predict(X_test))  # 混淆矩阵
print(confusion_matrix)
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
