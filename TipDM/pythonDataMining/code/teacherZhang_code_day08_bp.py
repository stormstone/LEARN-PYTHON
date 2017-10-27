import math
import numpy as np
import pandas as pd
from pandas import DataFrame,Series
def sigmoid(x):  #映射函数
    return 1/(1+math.exp(-x))

#中间层神经元输入和输出层神经元输入
Net_in = DataFrame(0.6,index=['input1','input2','theata'],columns=['a'])
Out_in = DataFrame(0,index=['input1','input2','input3','input4','theata'],columns=['a'])
Net_in.ix[2,0] = -1
Out_in.ix[4,0] = -1

#中间层和输出层神经元权值
W_mid = DataFrame(0.5,index=['input1','input2','theata'],columns=['mid1','mid2','mid3','mid4'])
W_out = DataFrame(0.5,index=['input1','input2','input3','input4','theata'],columns=['a'])
W_mid_delta = DataFrame(0,index=['input1','input2','theata'],columns=['mid1','mid2','mid3','mid4'])
W_out_delta = DataFrame(0,index=['input1','input2','input3','input4','theata'],columns=['a'])
yita = 0.5

#读入数据
data_tr = pd.read_table('./data/data_tr.txt',sep=',')  #训练集数据
data_te = pd.read_table('./data/data_te.txt',sep=',')  #测试集数据
#===网络训练==============
for n in range(0,10):
    for j in range(0, len(data_tr.index)):
        Net_in.ix[0:2, 0] = list(data_tr.ix[j, 0:2])  # 网络输入
        real = data_tr.ix[j, 2]  # 目标输出
        #中间层的输出
        for i in range(0,4):
            Out_in.ix[i,0] = sigmoid(sum(W_mid.ix[:,i]*Net_in.ix[:,0]))
        #输出层的输出/网络输出
        res = sigmoid(sum(Out_in.ix[:,0]*W_out.ix[:,0]))
        error = abs(res-real)/real

        #输出层权值变化量
        W_out_delta.ix[:,0] = yita*res*(1-res)*(real-res)*Out_in.ix[:,0]
        W_out_delta.ix[4,0] = -(yita*res*(1-res)*(real-res))
        W_out = W_out + W_out_delta #输出层权值更新

        #中间层权值变化量
        for i in range(0,4):
            W_mid_delta.ix[:,i] = yita*Out_in.ix[i,0]*(1-Out_in.ix[i,0])*W_out.ix[i,0]*res*(1-res)*(real-res)*Net_in.ix[:,0]
            W_mid_delta.ix[2,i] = -(yita*Out_in.ix[i,0]*(1-Out_in.ix[i,0])*W_out.ix[i,0]*res*(1-res)*(real-res))
        W_mid = W_mid + W_mid_delta #中间层权值更新
        #print('第',n*500+j,'次训练     ','第', j, '个训练样本误差:', error * 100, '%', '       真实值:', real, '预测值:', res)

print('===='*20,'开始测试','===='*20)
#===模型测试==================
for j in range(0, len(data_te.index)):
    Net_in.ix[0:2, 0] = list(data_tr.ix[j, 0:2])  # 网络输入
    real = data_tr.ix[j, 2]  # 目标输出
    #中间层的输出
    for i in range(0,4):
        Out_in.ix[i,0] = sigmoid(sum(W_mid.ix[:,i]*Net_in.ix[:,0]))
    #输出层的输出/网络输出
    res = sigmoid(sum(Out_in.ix[:,0]*W_out.ix[:,0]))
    error = abs(res-real)/real
    print('第', j, '个测试样本误差:', error * 100, '%', '       真实值:', real, '预测值:', res)
