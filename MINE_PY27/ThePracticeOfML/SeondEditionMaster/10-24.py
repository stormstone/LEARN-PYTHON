# -*- coding: utf-8 -*-   
#code:myhaspl@myhaspl.com
#直方图均衡化
#10-24.py
import cv2
import numpy as np
fn="test5.jpg"
myimg=cv2.imread(fn)
img=cv2.cvtColor(myimg,cv2.COLOR_BGR2GRAY)
h=img.shape[0]
w=img.shape[1]
newimg=np.zeros((h,w),np.uint8)
scount=0.0
#原始图像灰度级
scol={}
#目标图像灰度级
dcol={}
#原始图像频度
Ps={}
#累计概率
Cs={}

#统计原始图像灰度级
for m in xrange(h):
    for n in xrange(w):
        scol[img[m,n]]=scol.setdefault(img[m,n],0)+1
        scount+=1
        
#计算原始图像频度
for key in scol:
    Ps[key]=scol[key]/scount

#计算图像灰度的离散随机变量累计概率
keys=Ps.keys()
keys.sort()
for skey in scol:
    Cs.setdefault(skey,0)
    for key in keys:
        if key>skey :
            break            
        Cs[skey]+=Ps[key]
 #建立输入与输出之间的映射       
d_max=np.max(keys)
d_min=np.min(keys)
for skey in keys:
    dcol[skey]=int((d_max-d_min)*Cs[skey]+d_min)
    
for m in xrange(h):
    for n in xrange(w):
        newimg[m,n]=dcol[img[m,n]]


cv2.imshow('src',img)
cv2.imshow('dst',newimg)
cv2.waitKey()
cv2.destroyAllWindows()
