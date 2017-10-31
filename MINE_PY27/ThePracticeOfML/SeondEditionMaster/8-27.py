# -*- coding: utf-8 -*-
#8-27.py

import numpy as np
import neurolab as nl


#读取数据
import csv
datacluster=[]
file = open("access_area.csv",'r')
file.readline() 
reader = csv.reader(file)
for datarow in reader:
    datacluster.append([float(datarow[1]),float(datarow[2])])
    
accessdata=np.array(datacluster)



# Create net with 2 inputs and 7 neurons，分为7类
net = nl.net.newc([[0.0, max(accessdata[:,0])],[0.0, max(accessdata[:,1])]],7)
#训练该神经网络
# train with rule: Conscience Winner Take All algoritm (CWTA)
error = net.train(accessdata, epochs=200, show=20)

# Plot results:
import pylab as pl
pl.title('Classification Problem')
pl.subplot(211)
pl.plot(error)
pl.xlabel('Epoch number')
pl.ylabel('error (default MAE)')
w = net.layers[0].np['w']

#生成100个平均分布的随机数
rand_array=np.random.random((100,2))*np.array([max(accessdata[:,0]),max(accessdata[:,1])])
result=net.sim(rand_array)
plotshape=[]
colorindex=['r','y','g','c ','m','k','b']
for myres in result:
    index=0
    for tmp in myres:
        if tmp==1:
           plotshape.append(colorindex[index]+'p')
           break 
        index+=1
w = net.layers[0].np['w']
pl.subplot(212)
pl.xlabel('PV')
pl.ylabel('UV')
pl.plot(accessdata[:,0], accessdata[:,1], '.')

for i in range(len(result)-1):
    pl.plot(rand_array[i,0],rand_array[i, 1],plotshape[i])
for i in xrange(7):    
    pl.plot(w[i,0], w[i,1],colorindex[i]+'v')

pl.show()