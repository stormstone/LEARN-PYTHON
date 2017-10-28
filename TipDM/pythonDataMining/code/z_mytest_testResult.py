# -*- coding: utf-8 -*-
# @Time    : 2017-10-27 21:44
# @Author  : Storm
# @File    : z_mytest_testResult.py

import random
import pandas as pd
import numpy as np

n = 200
data = pd.read_csv('./data/mytest_testData.csv')
# o=a+10*sin(f*f)+random()*(c+d)
for i in range(n):
    data.loc[i, 'o'] = data.loc[i, 'a'] + np.sin(
        data.loc[i, 'b'] + data.loc[i, 'f'] * data.loc[i, 'f']) * 10 + random.random() * (
        data.loc[i, 'c'] + data.loc[i, 'd'])
data = data[['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'o']]
data.to_csv('./data/mytest_trueResult.csv')
