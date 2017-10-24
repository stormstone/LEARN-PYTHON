# -*- coding: utf-8 -*-
# @Time    : 2017-10-24 20:00
# @Author  : Storm
# @File    : day06.py

# kMeans
from pandas import DataFrame, Series

n = 50
x = Series(range(0, n))
y = Series(range(0, n))
center0 = Series([x[0], y[0]])
center1 = Series([x[1], y[1]])
dis = DataFrame(index=range(0, n), columns=['dis0', 'dis1', 'dis2'])


def which_min(x):
    if x[0] < x[1]:
        return 0
    else:
        return 1


while True:
    for i in range(0, n):
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
# print(dis)

# sklearn kMeans
import matplotlib.pyplot as plt

from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs

plt.figure(figsize=(12, 12))

n_samples = 1500
random_state = 170  # 随机因子
X, y = make_blobs(n_samples=n_samples, random_state=random_state)

y_pred = KMeans(n_clusters=2, random_state=random_state).fit_predict(X, y)
plt.subplot(221)
plt.scatter(X[y_pred == 0][:, 0], X[y_pred == 0][:, 1], marker='x', color='b')
plt.scatter(X[y_pred == 1][:, 0], X[y_pred == 1][:, 1], marker='+', color='r')

y_pred = KMeans(n_clusters=3, random_state=random_state).fit_predict(X, y)
plt.subplot(222)
plt.scatter(X[y_pred == 0][:, 0], X[y_pred == 0][:, 1], marker='x', color='b')
plt.scatter(X[y_pred == 1][:, 0], X[y_pred == 1][:, 1], marker='+', color='r')
plt.scatter(X[y_pred == 2][:, 0], X[y_pred == 2][:, 1], marker='1', color='m')
plt.show()

# 系统聚类
from sklearn.cluster import AgglomerativeClustering

n_samples = 1500
random_state = 170  # 随机因子
X, y = make_blobs(n_samples=n_samples, random_state=random_state)
plt.figure(figsize=(12, 12))
y_pred = AgglomerativeClustering(affinity='euclidean', linkage='ward', n_clusters=2).fit_predict(X)
plt.subplot(221)
plt.scatter(X[y_pred == 0][:, 0], X[y_pred == 0][:, 1], marker='x', color='b')
plt.scatter(X[y_pred == 1][:, 0], X[y_pred == 1][:, 1], marker='+', color='r')
y_pred = AgglomerativeClustering(affinity='euclidean', linkage='ward', n_clusters=3).fit_predict(X)
plt.subplot(222)
plt.scatter(X[y_pred == 0][:, 0], X[y_pred == 0][:, 1], marker='x', color='b')
plt.scatter(X[y_pred == 1][:, 0], X[y_pred == 1][:, 1], marker='+', color='r')
plt.scatter(X[y_pred == 2][:, 0], X[y_pred == 2][:, 1], marker='1', color='m')
plt.show()
