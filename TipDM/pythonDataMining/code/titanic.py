# -*- coding: utf-8 -*-
# @Time    : 2017-10-24 17:27
# @Author  : Storm
# @File    : titanic.py

import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier, DecisionTreeRegressor
from sklearn.tree import export_graphviz

data = pd.read_csv('./data/titanic_data.csv', encoding='utf-8')
data.drop(['PassengerId'], axis=1, inplace=True)  # 剔除PassengerId这一列
data.fillna(data.Age.mean(), inplace=True)  # 插值法填补缺失值
data.loc[data['Sex'] == 'male', 'Sex'] = 1  # 性别为男替换为1
data.loc[data['Sex'] == 'female', 'Sex'] = 0  # 性别为女替换为0

# X = data.iloc[:, 1:4]  # 取第2道第4列，1:4 顾头不顾尾
X = data.iloc[:, 1:3]  # 为便于展示，未考虑年龄
y = data.iloc[:, 0]
dtc = DecisionTreeClassifier(criterion='entropy')  # 初始化决策树对象，基于信息熵
dtc.fit(X, y)  # 训练模型

print('输出准确率：', dtc.score(X, y))
# 可视化决策树，导出结果是一个dot文件，需要安装Graphviz才能转换为.pdf或.png格式
with open('./tmp/tree.dot', 'w') as f:
    f = export_graphviz(dtc, feature_names=X.columns, out_file=f)

dtc.score(X, y)
