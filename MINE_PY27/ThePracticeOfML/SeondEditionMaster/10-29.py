# -*- coding: utf-8 -*-   
#code:myhaspl@myhaspl.com
#领域平均法滤波
#10-29.py
import cv2
import numpy as np
fn="test3.jpg"
myimg=cv2.imread(fn)
img=cv2.cvtColor(myimg,cv2.COLOR_BGR2GRAY)

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
    print "-",


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
