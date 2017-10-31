# -*- coding: utf-8 -*-   
#code:myhaspl@myhaspl.com
#领域平均法滤波3*3
#10-28.py
import cv2
import numpy as np
fn="test3.jpg"
myimg=cv2.imread(fn)
img=cv2.cvtColor(myimg,cv2.COLOR_BGR2GRAY)

#加上椒盐噪声
param=20
#灰阶范围
w=img.shape[1]
h=img.shape[0]
newimg=np.array(img)
#噪声点数量
noisecount=100000
for k in xrange(0,noisecount):
    xi=int(np.random.uniform(0,newimg.shape[1]))
    xj=int(np.random.uniform(0,newimg.shape[0]))
    newimg[xj,xi]=255

#领域平均法去噪
#脉冲响应函数，核函数
#图像四个边的像素处理
lbimg=np.zeros((h+2,w+2),np.float32)
tmpimg=np.zeros((h+2,w+2))
myh=h+2
myw=w+2
tmpimg[1:myh-1,1:myw-1]=newimg[0:myh,0:myw]
#用领域平均法的，设半径为2，脉冲响应函数
a=1/8.0
kernel=a*np.array([[1,1,1],[1,0,1],[1,1,1]])
for y in xrange(1,myh-1):
    for x in xrange(1,myw-1):
        lbimg[y,x]=np.sum(kernel*tmpimg[y-1:y+2,x-1:x+2])
    print ".",
resultimg=np.array(lbimg[1:myh-1,1:myw-1],np.uint8)        
cv2.imshow('src',newimg)
cv2.imshow('dst',resultimg)
cv2.waitKey()
cv2.destroyAllWindows()

