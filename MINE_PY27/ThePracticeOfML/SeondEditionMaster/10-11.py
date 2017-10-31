# -*- coding: utf-8 -*-   
#加性零均值高斯噪声  
#code:myhaspl@myhaspl.com  
#10-11.py
import cv2  
import numpy as np  

fn="test112.jpg"  
myimg=cv2.imread(fn)  
img=cv2.cvtColor(myimg,cv2.COLOR_BGR2GRAY)  
param=30  
#灰阶范围  
grayscale=256  
w=img.shape[1]  
h=img.shape[0]  
newimg=np.zeros((h,w),np.uint8)  
  
  
for x in xrange(0,h):  
    for y in xrange(0,w,2):  
        r1=np.random.random_sample()  
        r2=np.random.random_sample()  
        z1=param*np.cos(2*np.pi*r2)*np.sqrt((-2)*np.log(r1))  
        z2=param*np.sin(2*np.pi*r2)*np.sqrt((-2)*np.log(r1))  
          
        fxy=int(img[x,y]+z1)  
        fxy1=int(img[x,y+1]+z2)         
        #f(x,y)  
        if fxy<0:  
            fxy_val=0  
        elif fxy>grayscale-1:  
            fxy_val=grayscale-1  
        else:  
            fxy_val=fxy  
        #f(x,y+1)  
        if fxy1<0:  
            fxy1_val=0  
        elif fxy1>grayscale-1:  
            fxy1_val=grayscale-1  
        else:  
            fxy1_val=fxy1  
        newimg[x,y]=fxy_val  
        newimg[x,y+1]=fxy1_val  
      
  
cv2.imshow('preview',newimg)  
cv2.waitKey()  
cv2.destroyAllWindows()  

