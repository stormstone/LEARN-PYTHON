# -*- coding: utf-8 -*-
# @Time    : 2017-10-24 16:55
# @Author  : Storm
# @File    : mytest.py

from pandas import DataFrame, Series
import numpy as np
import matplotlib.pyplot as plt

from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs

plt.figure(figsize=(12, 12))

n_samples = 1500
random_state = 170  # 随机因子
X, y = make_blobs(n_samples=n_samples, random_state=random_state)

y_pred = KMeans(n_clusters=2, random_state=random_state).fit_predict(X)
plt.subplot(221)
plt.scatter(X[y_pred == 0][:, 0], X[y_pred == 0][:, 1], marker='x', color='b')
plt.scatter(X[y_pred == 1][:, 0], X[y_pred == 1][:, 1], marker='+', color='r')

y_pred = KMeans(n_clusters=3, random_state=random_state).fit_predict(X)
plt.subplot(222)
plt.scatter(X[y_pred == 0][:, 0], X[y_pred == 0][:, 1], marker='x', color='b')
plt.scatter(X[y_pred == 1][:, 0], X[y_pred == 1][:, 1], marker='+', color='r')
plt.scatter(X[y_pred == 2][:, 0], X[y_pred == 2][:, 1], marker='1', color='m')
plt.show()

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
