# -*- coding: utf-8 -*-
"""
Created on Mon May  1 09:33:09 2017

@author: kevin
"""
import os
import csv  # 为了讲解读入数据
import pandas as pd
import numpy as np
from sklearn.cluster import DBSCAN
import matplotlib.pyplot as plt  
import math
import matplotlib   # 方便改变中文字体

####------------------------------数据预处理-------------------------------####
# 设置当前工作路径
os.chdir('E:/培训部/网课孵化项目/Python集训营第一届 2017.10.09~11.09/城市公交站点设置的优化分析/data')
# 读取数据 方法一
data09 = pd.read_csv("./gps/gps_20140609.csv",encoding = 'gbk',delimiter = ',')
data09 = pd.read_csv("./gps/gps_20140609.csv",sep = ',',encoding = 'gbk')
# 读取数据 方法二
# 因为os文件读写可能会产生IOError，一旦出错就不能调用f.close()。为了保证正确地关闭文件
try:
    f = open('./gps/gps_20140609.csv',mode='r+',encoding = 'gbk')
    # data09 = f.read()  # 不能分隔
    data = csv.reader(f)
    data091 = [shuju for shuju in data]
    data091 = pd.DataFrame(data09)
finally:
    if f:
        f.close()

# 每次都这么写实在太繁琐，所以
with open('./gps/gps_20140609.csv', 'r+',encoding='gbk') as f:
    data = csv.reader(f)
    data091 = [shuju for shuju in data]
    data091 = pd.DataFrame(data09)
   
data09[data09.notnull()]    # 筛选出数据中的非空值 
data09.isnull().any()      # 检查每列是否有空值
data09.dropna()           #去除任何有空值的行

# 基于业务时间、卡片记录编码、车牌号，对数据去重
# frame.drop_duplicates(['state']),np.unique(data),data.unique()都只能用于一维数据
isduplicated = data09.duplicated(['业务时间','卡片记录编码','车牌号'],keep='first')
data09_new = [data09.ix[i,] for i in range(2007) if isduplicated[i]==False]
data09_new = pd.DataFrame(data09_new)       # 转为数据框

# 提取68路的数据
x = data09_new.ix[:,4]=='68路'
y = data09_new.ix[x==True,:]

# 对文件进行循环预处理

file_list = os.listdir("gps")
for file_name in file_list:
    if file_name.split(".")[-1] == "csv":
        data = pd.read_csv("gps/" + file_name,sep = ',',encoding = 'gbk')
        isduplicated = data.duplicated(['业务时间','卡片记录编码','车牌号'],keep='first')
        data_new = [data.ix[i,] for i in list(data.index) if isduplicated[i]==False]
        data_new = pd.DataFrame(data_new)       # 转为数据框
        x = data_new.ix[:,4]=='68路'
        y = data_new.ix[x==True,:]
    y.to_csv('aaa.csv',na_rep='NaN',header=True,index=False,mode= 'a+')
        
####---------------------------数据探索 折线图-----------------------------####
plt.figure(figsize=(8,4))
file_list = os.listdir("time")
for file_name in file_list:
    if file_name.split(".")[-1] == "csv":
        df_time = pd.read_csv("time/" + file_name)
        plt.plot(df_time["date"], df_time["num"], label=file_name)
plt.xticks([5,10,15,20],['5:00','10:00','15:00','20:00'])
plt.yticks([0,100000,200000,300000 ,400000,500000,600000],['0','10','20','30','40','50','60'])
zhfont1 = matplotlib.font_manager.FontProperties(fname='C:/Windows/Fonts/simsun.ttc')
#  simsun.ttc就是你电脑里面的字体文件，可以更换
plt.xlabel('时间点',fontproperties=zhfont1)     # fontproperties=zhfont1可以解决中文乱码问题
plt.ylabel('刷卡人数（单位：万）',fontproperties=zhfont1)
plt.title('图例',fontproperties=zhfont1)
plt.legend(("2014-06-09","2014-06-10","2014-06-11","2014-06-12","2014-06-13"),prop=zhfont1) 
plt.show()
# ”r”表示后面是纯粹的字符串，不会将后面的反斜杠当作转义字符，“u”代表Unicode
# matplotlib内置有TeX表达式解释器,排版引擎和自带的数学字体,只需要在Latex公式的文本前后各增加一个$符号，Matplotlib就可以自动进行解析    

# 显示中文的方法二
plt.rcParams['font.sans-serif'] = ['SimHei'] 
plt.xlabel('时间点')     
plt.ylabel('刷卡人数（单位：万）')
plt.title('图例')
# 绘制散点图
df_data = pd.read_csv("gjc.csv",sep = ',',encoding = 'gbk')
plt.figure(figsize=(8,4))
plt.scatter(df_data["经度"],df_data["纬度"])

####--------------------------------密度聚类------------------------------####
df_data = pd.read_csv("gjc.csv",'r+',encoding = 'gbk',delimiter = ',')
df_data = pd.read_csv("gjc.csv",sep = ',',encoding = 'gbk')
# 聚类，半径为0.0011（度），3代表聚类中点的区域必须至少有3个才能聚成一类
db = DBSCAN(eps=0.0011, min_samples=3).fit(df_data.iloc[:,:2])
flag = pd.Series(db.labels_, name=('flag'))
# axis中0是横向合并，1是纵向合并，若属性不对应就不会合并
df_cluster_result = pd.concat([df_data, flag], axis=1)    
df_cluster_result.describe()

# 去掉噪声点  
df_cluster_result = df_cluster_result[df_cluster_result["flag"] >= 0]

# 站点聚类后散点图
df_station = df_cluster_result.drop_duplicates("flag")  # 去重
df_station = df_station.reset_index()     # 增加了一列序列
plt.scatter(df_station["经度"],df_station["纬度"],c=df_station["flag"])

####---------------------------------分时段-------------------------------####
# 按实际站点顺序排序 ，之后按分好的时间段拆分开来
# 已经将聚出来的类（即站点）按实际站点地理位置进行排序，并成为“实际站点”列
df_actual = pd.read_csv("gjc_zd_actual.csv",sep = ',',encoding = 'gbk')
# 分割日期和时间，按空格号分开
T = [df_actual.ix[i,2].split(" ") for i in list(df_actual.index)]
# 提取时间,并将日期赋予同一个值2014/06/09，方便分时段
# T是列表，time[i] = T[[i]][2]表示T中第i个列表的第二列赋值给time的第i个
at1 = []
for i in df_actual.index:
    time = ["2014/06/09",T[i][1]]
    t = ' '.join(time)        ##合并公式
    at1.append(t)
# 或者用列表推导式的方法
at2 = [' '.join(["2014/06/09",T[i][1]]) for i in df_actual.index]

import time
time1 = [time.strptime(i,'%Y/%m/%d %H:%M') for i in at2]
time2 = [time.strftime('%Y-%m-%d %H:%M',j) for j in time1]
df_actual['业务时间'] = time2

#分时段提取数据
#设置时间点
point = ["2014/06/09 05:00", "2014/06/09 08:00", "2014/06/09 09:00",
           "2014/06/09 18:00", "2014/06/09 19:00", "2014/06/09 23:59"]
time3 = [time.strptime(i,'%Y/%m/%d %H:%M') for i in point]
time4 = [time.strftime('%Y-%m-%d %H:%M',j) for j in time3]

#设置写出路径
lj = [".\\bbb\\时段1_68.csv", ".\\bbb\\时段2_68.csv", ".\\bbb\\时段3_68.csv",
        ".\\bbb\\时段4_68.csv", ".\\bbb\\时段5_68.csv"]
for k in range(0,5):
    kk = (df_actual['业务时间'] >= time4[k]) & (df_actual['业务时间'] < time4[k+1])
    gjc = df_actual.ix[kk==True,:]
    gjc.to_csv(lj[k],na_rep='NaN',header=True,index=False)

####------------------------------计算上车人数----------------------------####
df_get_on_num = df_cluster_result.groupby('flag').count().iloc[:,1]
# dataframe和Series没有计数函数，转化为列表太麻烦
df_get_on_num = df_cluster_result.groupby('flag').count().ix[:,1]   
df_get_on_num.name=('get_on_num')     # 改名

df_flag = df_station['flag']
df_flag.index = df_flag
df_result = pd.concat([df_flag, df_get_on_num], axis=1)

####-------------------------------吸引权重-------------------------------####
df_wj = df_result['get_on_num']/sum(df_result['get_on_num'])
df_wj.name = ('wj')
df_result = pd.concat([df_result, df_wj], axis=1)

####-------------------------------下车人数-------------------------------####
'''
k = 0
for i in range(38):
    k = k + i +1
k/38
'''
# 构建泊松分布的函数
lmd = 19.5 #居民公交出行途径站数的数学期望 (1+2+3+..+38)/38    
k = len(df_result)
pro = pd.DataFrame(np.zeros((k,k+1)))
for i in range(k):
    for j in range(k):
        if (i < j):
            f = ((math.e)**(-lmd) * lmd**(j-i)) / math.factorial(j-i)
            pro.iloc[i,j] = f
    pro.iloc[i,k] = sum(pro.iloc[i,:k] * df_wj)   
    # 这里最好不要用ix，因为行名，列名都为1：:39数字，会混淆。最好用iloc位置索引

####------------------------------OD矩阵----------------------------------####
# 构建OD矩阵,求出一个站点到另一个站点的下车人数
# 创建数据框
df_OD = pd.DataFrame(np.zeros((k+1,k+1)))
for i in range(k):
    for j in range(k):
        if (i < j):
            p = pro.iloc[i,j]*df_wj.iloc[j] / pro.iloc[i,k]
            df_OD.iloc[i,j] = round(p * df_result.iloc[i,1])

# 求出OD数据框每列的人数的总和，即为每个站点下车的总人数
list_get_off_num = list()
for j in range(k):
    list_get_off_num.append(sum(df_OD.iloc[:k,j]))
df_get_off_num = pd.DataFrame(list_get_off_num, columns=['get_off_num'], index = df_result.index)

df_result = pd.concat([df_result, df_get_off_num], axis = 1)


# 各站点下车人数
for i in range(k):
    df_OD.iloc[k, i] = sum(df_OD.iloc[:k,i])    
# 各站点上车人数
for i in range(k):
    df_OD.iloc[i, k] = sum(df_OD.iloc[i,:k])

# 上车总人数
sum(df_OD.iloc[:k,k])
# 下车总人数
sum(df_OD.iloc[k,:k])

df_OD.iloc[k,k] = sum(df_OD.iloc[k,:k])

# 保存结果
df_OD.to_csv('68_OD.csv')
