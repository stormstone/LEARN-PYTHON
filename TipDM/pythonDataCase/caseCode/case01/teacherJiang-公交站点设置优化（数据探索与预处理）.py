# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 09:12:14 2017

@author: Dell
"""

import os
import csv  # 为了讲解读入数据
import pandas as pd
import numpy as np
from sklearn.cluster import DBSCAN
import matplotlib.pyplot as plt
import math
import matplotlib  # 方便改变中文字体

####------------------------------数据预处理-------------------------------####
# 设置当前工作路径
os.chdir('D:\Python\TipDM\pythonDataCase\caseCode\case01\data')
# 读取数据 方法一
data09 = pd.read_csv("./gps/gps_20140609.csv", encoding='gbk', delimiter=',')
data09 = pd.read_csv("./gps/gps_20140609.csv", sep=',', encoding='gbk')
# 读取数据 方法二
# 因为os文件读写可能会产生IOError，一旦出错就不能调用f.close()。为了保证正确地关闭文件
try:
    f = open('./gps/gps_20140609.csv', mode='r+', encoding='gbk')
    # data09 = f.read()  # 不能分隔
    data = csv.reader(f)
    data091 = [shuju for shuju in data]
    data091 = pd.DataFrame(data09)
finally:
    if f:
        f.close()

# 每次都这么写实在太繁琐，所以
with open('./gps/gps_20140609.csv', 'r+', encoding='gbk') as f:
    data = csv.reader(f)
    data091 = [shuju for shuju in data]
    data091 = pd.DataFrame(data09)

data09[data09.notnull()]  # 筛选出数据中的非空值
data09.isnull().any()  # 检查每列是否有空值
data09.dropna()  # 去除任何有空值的行

# 基于业务时间、卡片记录编码、车牌号，对数据去重
# frame.drop_duplicates(['state']),np.unique(data),data.unique()都只能用于一维数据
isduplicated = data09.duplicated(['业务时间', '卡片记录编码', '车牌号'], keep='first')
data09_new = [data09.ix[i,] for i in range(2007) if isduplicated[i] == False]
data09_new = pd.DataFrame(data09_new)  # 转为数据框

# 提取68路的数据
x = data09_new.ix[:, 4] == '68路'
y = data09_new.ix[x == True, :]

# 对文件进行循环预处理

file_list = os.listdir("gps")
for file_name in file_list:
    if file_name.split(".")[-1] == "csv":
        data = pd.read_csv("gps/" + file_name, sep=',', encoding='gbk')
        isduplicated = data.duplicated(['业务时间', '卡片记录编码', '车牌号'], keep='first')
        data_new = [data.ix[i,] for i in list(data.index) if isduplicated[i] == False]
        data_new = pd.DataFrame(data_new)  # 转为数据框
        x = data_new.ix[:, 4] == '68路'
        y = data_new.ix[x == True, :]
    y.to_csv('aaa.csv', na_rep='NaN', header=True, index=False, mode='a+')

####---------------------------数据探索 折线图-----------------------------####
plt.figure(figsize=(8, 4))
file_list = os.listdir("time")
for file_name in file_list:
    if file_name.split(".")[-1] == "csv":
        df_time = pd.read_csv("time/" + file_name)
        plt.plot(df_time["date"], df_time["num"], label=file_name)
plt.xticks([5, 10, 15, 20], ['5:00', '10:00', '15:00', '20:00'])
plt.yticks([0, 100000, 200000, 300000, 400000, 500000, 600000], ['0', '10', '20', '30', '40', '50', '60'])
zhfont1 = matplotlib.font_manager.FontProperties(fname='C:/Windows/Fonts/simsun.ttc')
#  simsun.ttc就是你电脑里面的字体文件，可以更换
plt.xlabel('时间点', fontproperties=zhfont1)  # fontproperties=zhfont1可以解决中文乱码问题
plt.ylabel('刷卡人数（单位：万）', fontproperties=zhfont1)
plt.title('图例', fontproperties=zhfont1)
plt.legend(("2014-06-09", "2014-06-10", "2014-06-11", "2014-06-12", "2014-06-13"), prop=zhfont1)
plt.show()
# ”r”表示后面是纯粹的字符串，不会将后面的反斜杠当作转义字符，“u”代表Unicode
# matplotlib内置有TeX表达式解释器,排版引擎和自带的数学字体,只需要在Latex公式的文本前后各增加一个$符号，Matplotlib就可以自动进行解析    

# 显示中文的方法二
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.xlabel('时间点')
plt.ylabel('刷卡人数（单位：万）')
plt.title('图例')
