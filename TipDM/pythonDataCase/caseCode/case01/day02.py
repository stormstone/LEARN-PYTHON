# -*- coding: utf-8 -*-
# @Time    : 2017-10-30 19:57
# @Author  : Storm
# @File    : day02.py

import os
import pandas as pd
import numpy as np
from sklearn.cluster import DBSCAN
import matplotlib.pyplot as plt
import math
import matplotlib

# 数据预处理
# 设置当前工作路径
os.chdir('D:\Python\TipDM\pythonDataCase\caseCode\case01\data')

df_data = pd.read_csv('gjc.csv', sep=',', encoding='gbk')
db = DBSCAN(eps=0.0011, min_samples=3).fit(df_data.ix[:, :2])
flag = pd.Series(db.labels_, name=('flag'))
df_cluster_result = pd.concat([df_data, flag], axis=1)
df_cluster_result.describe()

plt.scatter(df_data['经度'], df_data['纬度'])

# 去除噪声点
df_cluster_result = df_cluster_result[df_cluster_result['flag'] >= 0]

# 地图
df_station = df_cluster_result.drop_duplicates('flag')
df_station = df_station.reset_index()  # 增加一列
plt.scatter(df_station['经度'], df_station['纬度'], c=df_station['flag'])

# 分时段
df_actual = pd.read_csv('gjc_zd_actual.csv', sep=',', encoding='gbk')
# 分隔日期和时间
T = [df_actual.ix[i, 2].split(' ') for i in list(df_actual.index)]
at1 = []
for i in df_actual.index:
    time = ['2014/06/09', T[i][1]]
    t = ' '.join(time)
    at1.append(t)
at2 = [' '.join(['2014/06/09', T[i][1]]) for i in list(df_actual.index)]

import time

time1 = [time.strptime(i, '%Y/%m/%d %H:%M') for i in at2]
time2 = [time.strftime('%Y-%m-%d %H:%M', j) for j in time1]
df_actual['业务时间'] = time2

# 分时段提取数据
# 设置时间点
point = ['2014/06/09 05:00', '2014/06/09 08:00', '2014/06/09 09:00',
         '2014/06/09 18:00', '2014/06/09 19:00', '2014/06/09 23:59']

time3 = [time.strptime(i, '%Y/%m/%d %H:%M') for i in point]
time4 = [time.strftime('%Y-%m-%d %H:%M', j) for j in time3]

# 设置写出路径
lj = ['./abc/时段1_68.csv', './abc/时段2_68.csv', './abc/时段3_68.csv',
      './abc/时段4_68.csv', './abc/时段5_68.csv']
for k in range(5):
    kk = (df_actual['业务时间'] >= time4[k]) & (df_actual['业务时间'] <= time4[k + 1])
    gic = df_actual.ix[kk == True, :]
    gic.to_csv(lj[k], na_rep='NaN', header=True, index=False)

# 上车人数
df_get_on_num = df_cluster_result.groupby('flag').count().iloc[:, 1]
df_get_on_num.name = ('get_on_num')
df_flag = pd.Series(range(39))
df_result = pd.concat([df_flag, df_get_on_num], axis=1)

# 吸引权重
df_wj = df_result['get_on_num'] / sum(df_result['get_on_num'])
df_wj.name = ('wj')
df_result = pd.concat([df_result, df_wj], axis=1)
