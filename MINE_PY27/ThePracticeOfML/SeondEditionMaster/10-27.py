# -*- coding: utf-8 -*-     
#code:myhaspl@myhaspl.com  
#归一化块滤波  
#10-27.py
import cv2  
import numpy as np  
fn="test3.jpg"  
myimg=cv2.imread(fn)  
img=cv2.cvtColor(myimg,cv2.COLOR_BGR2GRAY)  
  
#加上椒盐噪声  
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
  
  
#滤波去噪  
lbimg=cv2.blur(newimg,(5,5))  
cv2.imshow('src',newimg)  
cv2.imshow('dst',lbimg)  
cv2.waitKey()  
cv2.destroyAllWindows() 
