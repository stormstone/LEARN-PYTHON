# -*- coding: utf-8 -*-
#8-26.py

import numpy as np
import neurolab as nl
import numpy.random as rand

#每一类的中心
centr = np.array([[0.2, 0.2], [0.4, 0.4], [0.7, 0.8]])
#以每类的中心为基础，产生随机点。
rand_norm = 0.05 * rand.randn(100, 3, 2)
inp = np.array([centr + r for r in rand_norm])
inp.shape = (100 * 3, 2)
rand.shuffle(inp) 

# Create net with 2 inputs and 3 neurons
net = nl.net.newc([[0.0, 1.0],[0.0, 1.0]], 3)
#训练该神经网络
# train with rule: Conscience Winner Take All algoritm (CWTA)
error = net.train(inp, epochs=200, show=20)

# Plot results:
import pylab as pl
pl.title('Classification Problem')
pl.subplot(211)
pl.plot(error)
pl.xlabel('Epoch number')
pl.ylabel('error (default MAE)')
w = net.layers[0].np['w']

#生成100个[0,1)之间的平均分布的随机数
rand_array=np.random.random((100,2))
result=net.sim(rand_array)
plotshape=[]
colorindex=['r','y','g']
for myres in result:
    index=0
    for tmp in myres:
        if tmp==1:
           plotshape.append(colorindex[index]+'p')
           break 
        index+=1
pl.subplot(212)
pl.plot(inp[:,0], inp[:,1], '.')
for i in range(len(result)-1):
    pl.plot(rand_array[i,0],rand_array[i, 1],plotshape[i])

pl.legend(loc=2)
pl.show()