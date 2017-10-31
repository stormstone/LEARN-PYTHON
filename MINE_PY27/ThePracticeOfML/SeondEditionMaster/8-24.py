#8-24.py
import numpy as np
import matplotlib.pyplot as plt
import mlpy
np.random.seed(0)
mean1, cov1, n1 = [1, 5], [[1,1],[1,2]], 200 # 200 points, mean=(1,5)
x1 = np.random.multivariate_normal(mean1, cov1, n1)
mean2, cov2, n2 = [2.5, 2.5], [[1,0],[0,1]], 300 # 300 points, mean=(2.5,2.5)
x2 = np.random.multivariate_normal(mean2, cov2, n2)
mean3, cov3, n3 = [5, 8], [[0.5,0],[0,0.5]], 200 # 200 points, mean=(5,8)
x3 = np.random.multivariate_normal(mean3, cov3, n3)
x = np.concatenate((x1, x2, x3), axis=0) # concatenate the samples
cls, means, steps = mlpy.kmeans(x, k=3, plus=True)
fig = plt.figure(1)
plot1 = plt.scatter(x[:,0], x[:,1], c=cls, alpha=0.75)
plot2 = plt.scatter(means[:,0], means[:,1], c=np.unique(cls), s=128, marker='d') # plot the means
plt.show()
