# -*- coding: utf-8 -*-
#8-25.py

import numpy as np
import neurolab as nl
import numpy.random as rand

#每一类的中心
centr = np.array([[0.2, 0.2], [0.4, 0.4], [0.7, 0.3]])
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

pl.subplot(212)
pl.plot(inp[:,0], inp[:,1], '.', \
        centr[:,0], centr[:, 1] , 'yv', \
        w[:,0], w[:,1], 'p')
pl.legend(['train samples', 'real centers', 'train centers'],loc=2)
pl.show()