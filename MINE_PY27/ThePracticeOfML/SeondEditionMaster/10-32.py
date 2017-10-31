# -*- coding: utf-8 -*-   
#code:myhaspl@myhaspl.com
#中值滤波
#10-32.py
import cv2
import numpy as np
fn="test3.jpg"
myimg=cv2.imread(fn)
img=cv2.cvtColor(myimg,cv2.COLOR_BGR2GRAY)

#灰阶范围
w=img.shape[1]
h=img.shape[0]
newimg=np.array(img)


#加上高斯噪声
param=20
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


#滤波去噪
lbimg=cv2.medianBlur(newimg,3)
cv2.imshow('src',newimg)
cv2.imshow('dst',lbimg)
cv2.waitKey()
cv2.destroyAllWindows()   
