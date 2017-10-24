# -*- coding: utf-8 -*-
# @Time    : 2017-10-24 16:55
# @Author  : Storm
# @File    : mytest.py

import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier, DecisionTreeRegressor
from sklearn.tree import export_graphviz

data = pd.read_csv('D:\\Python\\TipDM\\pythonDataMining\\code\\data\\titanic_data.csv',encoding='utf-8')
data.drop(['PassengerId'], axis=1, inplace=True)#剔除PassengerId这一列
