# -*- coding: utf-8 -*- 
#加性零均值高斯噪声
#code:myhaspl@myhaspl.com
#10-12.py
import cv2
import numpy as np

fn="test112.jpg"
myimg=cv2.imread(fn)
img=myimg

param=30
#灰阶范围
grayscale=256
w=img.shape[1]
h=img.shape[0]
newimg=np.zeros((h,w,3),np.uint8)

for x in xrange(0,h):
    for y in xrange(0,w,2):
        r1=np.random.random_sample()
        r2=np.random.random_sample()
        z1=param*np.cos(2*np.pi*r2)*np.sqrt((-2)*np.log(r1))
        z2=param*np.sin(2*np.pi*r2)*np.sqrt((-2)*np.log(r1))        
        fxy_0=int(img[x,y,0]+z1)
        fxy1_0=int(img[x,y+1,0]+z2)  
        fxy_1=int(img[x,y,1]+z1)
        fxy1_1=int(img[x,y+1,1]+z2)  
        fxy_2=int(img[x,y,2]+z1)
        fxy1_2=int(img[x,y+1,2]+z2)          
        #f(x,y)
        if fxy_0<0:
            fxy_val_0=0
        elif fxy_0>grayscale-1:
            fxy_val_0=grayscale-1
        else:
            fxy_val_0=fxy_0
            
        if fxy_1<0:
            fxy_val_1=0
        elif fxy_1>grayscale-1:
            fxy_val_1=grayscale-1
        else:
            fxy_val_1=fxy_1
            
        if fxy_2<0:
            fxy_val_2=0
        elif fxy_2>grayscale-1:
            fxy_val_2=grayscale-1
        else:
            fxy_val_2=fxy_2
            
        #f(x,y+1)
        if fxy1_0<0:
            fxy1_val_0=0
        elif fxy1_0>grayscale-1:
            fxy1_val_0=grayscale-1
        else:
            fxy1_val_0=fxy1_0
            
        if fxy1_1<0:
            fxy1_val_1=0
        elif fxy1_1>grayscale-1:
            fxy1_val_1=grayscale-1
        else:
            fxy1_val_1=fxy1_1
            
        if fxy1_2<0:
            fxy1_val_2=0
        elif fxy1_2>grayscale-1:
            fxy1_val_2=grayscale-1
        else:
            fxy1_val_2=fxy1_2 
            
        newimg[x,y,0]=fxy_val_0
        newimg[x,y,1]=fxy_val_1
        newimg[x,y,2]=fxy_val_2
        newimg[x,y+1,0]=fxy1_val_0
        newimg[x,y+1,1]=fxy1_val_1
        newimg[x,y+1,2]=fxy1_val_2

cv2.imshow('preview',newimg)
cv2.waitKey()
cv2.destroyAllWindows()
