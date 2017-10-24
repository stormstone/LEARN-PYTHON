# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 21:47:39 2017

@author: 45543
"""


import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

## 两个输入
x = [[0, 0], [1, 1], [2, 2]]
y = [0, 1, 2]
lm = LinearRegression()
lm.fit(x, y) # 拟合
print(lm.predict([[3, 3]]))  # 预测
print(lm.coef_)  # 系数

## 一个输入
x = np.array([1, 2, 3, 4])
# x = np.linspace(1, 4, 4)
x1 = x[np.newaxis] #插入新的维度
x2 = np.transpose(x1)
y = [1, 4, 9, 12]
lm = LinearRegression()
lm.fit(x2, y)
print(lm.predict([[5]]))
print(lm.coef_)
# 画图
plt.scatter(x2, y)
plt.plot(x2, lm.predict(x2), color = 'green')

## 波士顿房价
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.datasets import load_boston
import numpy as np

boston = load_boston()
print(boston.keys())  # 查看键
print(boston.feature_names)  # 查看变量名
x1 = boston.data[:, 5]
x2 = x1[np.newaxis]  #插入新的维度
x = np.transpose(x2)
# x = boston.data[:, np.newaxis, 5] # 效果同上
y = boston.target
lm = LinearRegression()
lm.fit(x, y)
print('回归方程的确定性系数为：', lm.score(x, y))
print('回归方程的斜率为：', lm.coef_)
print('回归方程的截距为：', lm.intercept_)
print('回归方程为：y = ', lm.coef_, '*x + (', lm.intercept_, ')')
#绘图
plt.scatter(x,y)
plt.plot(x, lm.predict(x), color = 'blue', linewidth = 3)
plt.plot(x, x*lm.coef_ + lm.intercept_, color = 'red')

## Logistic Regression
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.cross_validation import train_test_split

data = pd.read_csv('C:\\Users\\45543\\Desktop\\LogisticRegression.csv')
#data_dum = pd.get_dummies(data, prefix = 'rank', columns = ['rank'], drop_first = True)
data_dum = pd.get_dummies(data, columns = ['rank'])  # 独热编码
print(data_dum.tail(5))

#划分训练集与测试集
x_train, x_test, y_train, y_test = train_test_split(data_dum.ix[:, 1:], data_dum.ix[:, 0], test_size=.1, random_state=520)
lr = LogisticRegression()    # 建立LR模型
lr.fit(x_train, y_train)    # 用处理好的数据训练模型
print ('逻辑回归的准确率为：{0:.2f}%'.format(lr.score(x_test, y_test) *100))

## 决策树分类
from sklearn.datasets import load_iris 
from sklearn.cross_validation import cross_val_score 
from sklearn.tree import DecisionTreeClassifier 
iris = load_iris() 
clf = DecisionTreeClassifier(random_state=0) 
cross_val_score(clf, iris.data, iris.target, cv=10) 

## 决策树回归
from sklearn.datasets import load_boston 
from sklearn.cross_validation import cross_val_score 
from sklearn.tree import DecisionTreeRegressor 
boston = load_boston() 
regressor = DecisionTreeRegressor(random_state=0) 
cross_val_score(regressor, boston.data, boston.target, cv=10) #计算交叉验证评分