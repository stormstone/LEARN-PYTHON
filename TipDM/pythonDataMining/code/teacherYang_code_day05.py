# -*- coding: utf-8 -*-
"""
Created on Sat Oct 21 15:49:59 2017

@author: 45543
"""

## 决策树练习
import pandas as pd
from sklearn.tree import DecisionTreeClassifier as DTC, export_graphviz

data = pd.read_csv('./data/titanic_data.csv', encoding='utf-8')
data.drop(['PassengerId'], axis=1, inplace=True)  # 舍弃ID列，不适合作为特征
# 数据是类别标签，将其转换为数，用1表示男，0表示女。
data.loc[data['Sex'] == 'male', 'Sex'] = 1
data.loc[data['Sex'] == 'female', 'Sex'] = 0
data.fillna(data.Age.mean(), inplace=True)
print(data.head(5))  # 查看数据
X = data.iloc[:, 1:3]  # 为便于展示，未考虑年龄（最后一列）
y = data.iloc[:, 0]
dtc = DTC(criterion='entropy')  # 初始化决策树对象，基于信息熵
dtc.fit(X, y)  # 训练模型
print('输出准确率：', dtc.score(X, y))
# 可视化决策树，导出结果是一个dot文件，需要安装Graphviz才能转换为.pdf或.png格式
with open('./tmp/tree.dot', 'w') as f:
    f = export_graphviz(dtc, feature_names=X.columns, out_file=f)

## 神经网络
from sklearn.datasets import load_iris
from sklearn.neural_network import MLPClassifier
from sklearn.cross_validation import train_test_split
from sklearn.metrics import classification_report, confusion_matrix

iris = load_iris()
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target)
mlp = MLPClassifier(hidden_layer_sizes=8, max_iter=500)
mlp.fit(X_train, y_train)
confusion_matrix(y_test, mlp.predict(X_test))  # 混淆矩阵
print(classification_report(y_test, mlp.predict(X_test)))  # 分类报告

mlp.coefs_  # 权重
mlp.intercepts_  # 偏差
len(mlp.coefs_)  # 2
len(mlp.coefs_[0])  # 4*8
len(mlp.coefs_[1])  # 8*3
len(mlp.intercepts_)  # 2
len(mlp.intercepts_[0])  # 8
len(mlp.intercepts_[1])  # 3

## kNN算法实现
from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import load_iris
from sklearn.cross_validation import train_test_split

iris = load_iris()
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target)
kNN = KNeighborsClassifier(n_neighbors=6)
kNN.fit(X_train, y_train)
kNN.score(X_test, y_test)

## 朴素贝叶斯
# 高斯朴素贝叶斯
import numpy as np

X = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
Y = np.array([1, 1, 1, 2, 2, 2])
from sklearn.naive_bayes import GaussianNB

clf = GaussianNB()
clf.fit(X, Y)
clf.class_prior_  # 每一个类的概率
clf.theta_  # 每个类中各个特征的平均
clf.sigma_  # 每个类中各个特征的方差

# 多项式朴素贝叶斯
import numpy as np

X = np.random.randint(5, size=(6, 100))
y = np.array([1, 2, 3, 4, 5, 6])
from sklearn.naive_bayes import MultinomialNB

clf = MultinomialNB()
clf.fit(X, y)

# 高斯朴素贝叶斯对iris数据集进行分类
from sklearn import datasets

iris = datasets.load_iris()  # 读取iris数据集
from sklearn.naive_bayes import GaussianNB  # 使用高斯贝叶斯模型

clf = GaussianNB()  # 设置分类器
clf.fit(iris.data, iris.target)  # 训练分类器
y_pred = clf.predict(iris.data)  # 预测
print("Number of mislabeled points out of a total %d points : %d" % (iris.data.shape[0], (iris.target != y_pred).sum()))
