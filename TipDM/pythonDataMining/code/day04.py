# -*- coding: utf-8 -*-
# @Time    : 2017-10-22 14:12
# @Author  : Storm
# @File    : day04.py

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

X = [[0, 0], [1, 1], [2, 2]]
y = [0, 1, 2]
lm = LinearRegression()
lm.fit(X, y)
lm.predict([[3, 3]])
print(lm.coef_)  # 系数
print('回归曲线为：y = ', lm.coef_, '*x + (', lm.intercept_, ')')
print('确定性系数为：', lm.score(X, y))  # 确定性系数，越接近1（完全拟合），拟合效果越好

x1 = np.array([1, 2, 3, 4])
x2 = x1[np.newaxis]  # 增加X1的维度
X = np.transpose(x2)
y = [1, 4, 9, 12]
lm = LinearRegression()
lm.fit(X, y)
print('回归曲线为：y = ', lm.coef_, '*x + (', lm.intercept_, ')')
print('确定性系数为：', lm.score(X, y))
plt.scatter(X, y)
plt.plot(X, lm.predict(X), color='red')
plt.show()

'''
线性回归，波士顿房价预测
'''
from sklearn.datasets import load_boston

boston = load_boston()
print(boston.keys())
print(boston.feature_names)  # 变量名
X = boston.data[:, np.newaxis, 5]  # 第6列住房平均数，np.newaxis新增维度
y = boston.target
lm = LinearRegression()
lm.fit(X, y)
print('回归曲线为：y = ', lm.coef_, '*x + (', lm.intercept_, ')')
print('确定性系数为：', lm.score(X, y))
plt.scatter(X, y)
plt.plot(X, lm.predict(X), '*r')
plt.show()

'''
逻辑回归，分类，预测研究生是否会被录取，LogisticRegression.csv
'''
data = pd.read_csv('./data/LogisticRegression.csv')
data_dum = pd.get_dummies(data, columns=['rank'])
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

x_train, x_test, y_train, y_test = train_test_split(data_dum.ix[:, 1:], data_dum.ix[:, 0], test_size=0.1,
                                                    random_state=520)
lr = LogisticRegression()
lr.fit(x_train, y_train)
print(lr.score(x_test, y_test))

'''
决策树,分类，回归
'''
from sklearn.tree import DecisionTreeClassifier, DecisionTreeRegressor
from sklearn.tree import export_graphviz
from sklearn.datasets import load_iris, load_boston
from sklearn.model_selection import cross_val_score

##分类
iris = load_iris()
dtc = DecisionTreeClassifier(random_state=1)  # 随机种子,保证实验可重复的效果一样
print(cross_val_score(dtc, iris.data, iris.target, cv=10))  # 计算交叉验证评分

##回归
boston = load_boston()
dtr = DecisionTreeRegressor(random_state=1)
print(cross_val_score(dtr, boston.data, boston.target, cv=10))  # 计算交叉验证评分
