# -*- coding: utf-8 -*-
# @Time    : 2017-10-18 20:00
# @Author  : Storm
# @File    : day03.py

import numpy as np
import pandas as pd
from pandas import DataFrame, Series

'''
numpy 平面上有100个点，求任意两点之间的距离
'''
x = range(20, 120)
y = range(20, 120)
dis = np.zeros([100, 100])
for i in range(0, 100):
    for j in range(0, 100):
        dis[i, j] = ((x[i] - x[j]) ** 2 + (y[i] - y[j]) ** 2) ** 0.5  # 欧氏距离
# print(dis)

'''
鸢尾花
练习4：数据索引
1. 将iris.data与iris.target合并成一个数据框，要求列名分别为：‘sepal length’、‘sepal
width’、‘petal length’、‘petal width’；并将第5列前50、中间50、最后50个元素分别赋
值为：'setosa'、'versicolor'、'virginica'
2. 找出iris数据集中virginica种类的样本数据
3. 找出iris数据集中Sepal.Width大于4的样本数据
'''
# from sklearn import datasets
#
# iris = datasets.load_iris()
# x = iris.data
# y = iris.target
# da = DataFrame(x, columns=['sepal length', 'sepal width', 'petal length', 'petal width'])
# da.ix[:, 'Species'] = y
# da.ix[0:50, 'Species'] = 'setosa'
# da.ix[50:100, 'Species'] = 'versicolor'
# da.ix[100:150, 'Species'] = 'virginica'

'''
对平面上的100个点进行聚类，要求聚为2类，其横纵坐标都为0到99；
Ø K-means算法流程：
1、随机选取k个样本作为初始类中心；
2、求各样本至各类中心的距离；
3、将样本归为距离其最近的类中心所属类；
4、计算各类样本均值作为新类中心；
5、判断类中心有无变换，有则跳至第2步，若无则结束算法。
'''
n = 100  # 待聚类样本个数
x = Series(range(0, n))
y = Series(range(0, n))

center0 = Series([x[0], y[0]])
center1 = Series([x[1], y[1]])

dis = DataFrame(index=range(0, 100), columns=['dis0', 'dis1', 'dis2'])


def which_min(x):
    if x[0] < x[1]:
        return 0
    else:
        return 1


while True:
    for i in range(0, 100):
        dis.ix[i, 0] = ((x[i] - center0[0]) ** 2 + (y[i] - center0[1]) ** 2) ** 0.5
        dis.ix[i, 1] = ((x[i] - center1[0]) ** 2 + (y[i] - center1[1]) ** 2) ** 0.5
        dis.ix[i, 2] = which_min(dis.ix[i, 0:2])
    index0 = dis.ix[:, 2] == 0
    index1 = dis.ix[:, 2] == 1
    center0_new = Series([x[index0].mean(), y[index0].mean()])
    center1_new = Series([x[index1].mean(), y[index1].mean()])
    if (sum(center0 == center0_new) + sum(center1 == center1_new) == 4):
        break
    center0 = center0_new
    center1 = center1_new
print(dis)
