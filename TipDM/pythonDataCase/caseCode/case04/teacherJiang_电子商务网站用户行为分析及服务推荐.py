# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 10:12:11 2017

@author: Administrator
"""

import os
import pandas as pd
import numpy as np
from random import sample
from pandas import DataFrame,Series
import re
os.getcwd()
os.chdir('E:/培训部/2017.11.01 郑州轻工业学院（10天）/电子商务智能推荐服务')
# 读入数据
# 在cmd中 （提前设置环境变量） pip install pymysql
import pymysql as pm
con = pm.connect('localhost','root','123456','tipdm',charset='gbk')
data = pd.read_sql('select * from all_gzdata',con=con)
con.close()           #关闭连接
data.to_csv('aa.csv')
# 0.0网页类型统计
urlId=['101','199','107','301','102','106','103']
count=[]
for pattern in urlId:
    index=sum([re.search(pattern,str(i))!=None for i in data.ix[:,'fullURLId']])
    count.append(index)
urlId_count={'urlId':urlId,'count':count}
urlId_count=DataFrame(urlId_count)

# 0.1点击次数统计
# pd.value_counts()  属于高级方法，返回一个Series，其索引值为唯一值，其值为频率，按其计数的降序排列
res=data.ix[:,'realIP'].value_counts()     # 对IP进行统计：每个IP点击了多少次
res1=res.value_counts()                    # 对点击次数的IP统计：例如点击了2次的ip有多少个
IP_count=DataFrame({'a_IP':list(res1.index),'count':list(res1)})
IP_total=sum(IP_count.ix[:,1])
IP_count.ix[:,'pers']=[index/IP_total for index in IP_count.ix[:,1]]
IP_count['pers']=IP_count.ix[:,1]/sum(IP_count.ix[:,1])

# 0.2高频点击网址统计
res=data.ix[:,'fullURL'].value_counts()
URL_Frame=DataFrame({'a_URL':list(res.index),'count':list(res)})

# 0.3网址点击次数统计
res=data.ix[:,'fullURL'].value_counts()
res1=res.value_counts()
URL_count=DataFrame({'a_URL':list(res1.index),'count':list(res1)})
URL_total=sum(URL_count.ix[:,1])
URL_count.ix[:,'pers']=[index/URL_total for index in URL_count.ix[:,1]]

# 1.0读入数据
 # 1.1取出107类型数据
# 读入数据 方法一
data_107 = pd.read_csv('data_107.csv')
# 读取数据 方法二
import csv
# 因为os文件读写可能会产生IOError，一旦出错就不能调用f.close()。为了保证正确地关闭文件
try:
    f = open('./data_107.csv',mode='r+',encoding = 'utf-8')
    # data0 = f.read()  # 不能分隔
    data0 = csv.reader(f)
    data0 = [shuju for shuju in data0]
    data0 = pd.DataFrame(data0)
finally:
    if f:
        f.close()

# 每次都这么写实在太繁琐，所以
with open('./data_107.csv', 'r+',encoding='utf-8') as f:
    data0 = csv.reader(f)
    data0 = [shuju for shuju in data0]
    data0 = pd.DataFrame(data0)
   
# 1.2在107类型中筛选出婚姻类数据
index=[re.search('hunyin',str(i))!=None for i in data_107.ix[:,'fullURL']]
data_hunyin=data_107.ix[index,:]
# 1.3提取所需字段(realIP、fullURL)
info = data_hunyin.ix[:,['realIP','fullURL']]

# 2.0去除网址中“？”及其后面内容
da=[re.sub('\?.*','',str(i)) for i in info.ix[:,'fullURL']]
info.ix[:,'fullURL']=da     # 将info中‘fullURL’那列换成da
# 2.1去除无html网址
index=[re.search('\.html',str(i))!=None for i in info.ix[:,'fullURL']]
index.count(True)   # True 或者 1 ， False 或者 0
info1=info.ix[index,:]
# 2.2找出翻页和非翻页网址
index=[re.search('/\d+_\d+\.html',i)!=None for i in info1.ix[:,'fullURL']]
index1=[i==False for i in index]
info1_1=info1.ix[index,:]   # 带翻页网址
info1_2=info1.ix[index1,:]  # 无翻页网址
# 2.3将翻页网址还原
da=[re.sub('_\d+\.html','.html',str(i)) for i in info1_1.ix[:,'fullURL']]
info1_1.ix[:,'fullURL']=da
# 2.4翻页与非翻页网址合并
frames = [info1_1,info1_2]
info2 = pd.concat(frames)
# 或者
info2 = pd.concat([info1_1,info1_2],axis = 0)   # 默认为0，即行合并
# 2.5去重（realIP和fullURL两列相同）
info3=info2.drop_duplicates()
# 2.6将IP转换成字符型数据
info3.ix[:,0]=[str(index) for index in info3.ix[:,0]]
info3.ix[:,1]=[str(index) for index in info3.ix[:,1]]
len(info3)

#==============
info3=info3.ix[info3.index[0:1000],:]
len(info3)
#===============

# 3.0筛选满足一定浏览次数的IP==================
IP_count=info3['realIP'].value_counts()
#3.1找出IP集合
IP=list(IP_count.index)
count=list(IP_count.values)
# 3.2统计每个IP的浏览次数，并存放进IP_count数据框中,第一列为IP，第二列为浏览次数
IP_count=DataFrame({'IP':IP,'count':count})
# 3.3筛选出浏览网址在n次以上的IP集合
n=2
index=IP_count.ix[:,'count']>n
IP_index=IP_count.ix[index,'IP']
# 3.4划分IP集合为训练集和测试集
index_tr=sample(range(0,len(IP_index)),int(len(IP_index)*0.8))    # 或者np.random.sample
index_te=[i for i in range(0,len(IP_index)) if i not in index_tr]
IP_tr=IP_index[index_tr]
IP_te=IP_index[index_te]
# 3.5将对应数据集划分为训练集和测试集
index_tr=[i in list(IP_tr) for i in info3.ix[:,'realIP']]
index_te=[i in list(IP_te) for i in info3.ix[:,'realIP']]
data_tr=info3.ix[index_tr,:]
data_te=info3.ix[index_te,:]
print(len(data_tr))
IP_tr = data_tr.ix[:,0]   # 训练集IP
url_tr = data_tr.ix[:,1]  # 训练集网址
IP_tr = list(set(IP_tr))     # 去重处理
url_tr = list(set(url_tr))   # 去重处理
len(url_tr)

# 4.0利用训练集数据构建模型====================
UI_matrix_tr = DataFrame(0,index=IP_tr,columns=url_tr)
# 4.1求用户－物品矩阵
for i in data_tr.index:
    UI_matrix_tr.ix[data_tr.ix[i,'realIP'],data_tr.ix[i,'fullURL']] = 1
sum(UI_matrix_tr.sum(axis=1))

# 4.2求物品相似度矩阵
Item_matrix_tr = DataFrame(0,index=url_tr,columns=url_tr)
for i in Item_matrix_tr.index:
    for j in Item_matrix_tr.index:
        a = sum(UI_matrix_tr.ix[:,[i,j]].sum(axis=1)==2)
        b = sum(UI_matrix_tr.ix[:,[i,j]].sum(axis=1)!=0)
        Item_matrix_tr.ix[i,j] = a/b

# 4.3将物品相似度矩阵对角线处理为零
for i in Item_matrix_tr.index:
    Item_matrix_tr.ix[i,i]=0

# 5.0利用测试集数据对模型评价===================
IP_te = data_te.ix[:,0]
url_te = data_te.ix[:,1]
IP_te = list(set(IP_te))
url_te = list(set(url_te))

# 5.1测试集数据用户物品矩阵
UI_matrix_te = DataFrame(0,index=IP_te,columns=url_te)
for i in data_te.index:
    UI_matrix_te.ix[data_te.ix[i,'realIP'],data_te.ix[i,'fullURL']] = 1

# 5.2对测试集IP进行推荐
Res = DataFrame('NaN',index=data_te.index,columns=['IP','已浏览网址','推荐网址','T/F'])
Res.ix[:,'IP']=list(data_te.ix[:,0])
Res.ix[:,'已浏览网址']=list(data_te.ix[:,1])

# 开始推荐
for i in Res.index:
    if Res.ix[i,'已浏览网址'] in list(Item_matrix_tr.index):
        Res.ix[i,'推荐网址'] = Item_matrix_tr.ix[Res.ix[i,'已浏览网址'],:].argmax()
        if Res.ix[i,'推荐网址'] in url_te:
            Res.ix[i,'T/F']=UI_matrix_te.ix[Res.ix[i,'IP'],Res.ix[i,'推荐网址']]==1
        else:
            Res.ix[i,'T/F'] = False

# 5.3计算推荐准确率
sum(Res.ix[:,'T/F']==True)/(len(Res.index)-sum(Res.ix[:,'T/F']=='NaN'))
