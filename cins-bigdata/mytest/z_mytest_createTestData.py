# -*- coding: utf-8 -*-
# @Time    : 2017-10-27 21:41
# @Author  : Storm
# @File    : z_mytest_createTestData.py

from pandas import DataFrame
import numpy as np

n = 200
data = DataFrame(np.random.random((n, 8)), columns=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])
a = np.random.random((n, 1))
data.to_csv('./data/mytest_testData.csv')
