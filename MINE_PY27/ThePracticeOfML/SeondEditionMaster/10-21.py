# -*- coding: utf-8 -*-   
#分段线性变换
#code:myhaspl@myhaspl.com
#10-21.py
import cv2
import numpy as np
fn="test4.jpg"
myimg=cv2.imread(fn)
img=cv2.cvtColor(myimg,cv2.COLOR_BGR2GRAY)

w=img.shape[1]
h=img.shape[0]
newimg=np.zeros((h,w),np.uint8)
#源
Ds_min=0
Ds_internal=80#中间
Ds_max=255
#目标
Dd_min=0
Dd_internal=160#中间
Dd_max=255
for m in xrange(h):
    for n in xrange(w):
        if img[m,n]>Ds_min and img[m,n]<=Ds_internal:
            newimg[m,n]=int((Dd_internal-Dd_min)/(Ds_internal-Ds_min)*(img[m,n]-Ds_min)+Dd_min)
        else:
            newimg[m,n]=int((Dd_max-Dd_internal)/(Ds_max-Ds_internal)*(img[m,n]-Ds_internal)+Dd_internal)
    print ".",        

        

cv2.imshow('src',img)
cv2.imshow('dst',newimg)
cv2.waitKey()
cv2.destroyAllWindows()
