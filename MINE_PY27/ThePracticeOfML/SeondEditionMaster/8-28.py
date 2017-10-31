# -*- coding: utf-8 -*-
#code:myhaspl@myhaspl.com
#8-28.py
import numpy as np
import neurolab as nl

#读取数据
import csv
datatarget=[]
file = open("sales4.csv",'r')
file.readline() 
reader = csv.reader(file)
ii=0
for datarow in reader:
    datatarget.append([])
    for data in datarow:
        datatarget[ii].append(int(data))
    ii=ii+1

datatarget=np.array(datatarget)


input = [[1,1,1,1,-1,1,1,-1,-1,-1,-1,-1],
         [1,-1,1,-1,1,-1,1,1,-1,-1,-1,1],
         [1,1,-1,-1,1,-1,-1,-1,-1,1,1,-1]]

# Create and train network
net = nl.net.newhem(datatarget)

output = net.sim(datatarget)
print u"样本数据，结果必须为[0, 1, 2, 3, 4]" 
print np.argmax(output, axis=0) 

output = net.sim(input)
print u"测试数据的神经网络最终输出" 
print output  
print u"测试数据的分类结果如下："
ii=0 
for test in output:
    print  input[ii],
    print  u"分类如下:"
    print np.argmax(test)
    ii+=1