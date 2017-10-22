# -*- coding: utf-8 -*-
# @Time    : 2017-10-18 19:55
# @Author  : Storm
# @File    : day02.py
import pandas as pd
import os

# os.chdir('D:\Python\TipDM\python数据挖掘')
# print(os.getcwd())

data1 = pd.read_table('1.2-1data.txt', sep=',', header=0)
print(data1)
data1.to_csv('data1.csv')
