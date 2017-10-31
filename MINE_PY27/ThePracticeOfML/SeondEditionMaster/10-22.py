# -*- coding: utf-8 -*-   
#指数非线性变换
#code:myhaspl@myhaspl.com
#10-22.py
import cv2
import numpy as np
fn="test5.jpg"
myimg=cv2.imread(fn)
img=cv2.cvtColor(myimg,cv2.COLOR_BGR2GRAY)
b=1.2
c=0.2
a=0.2
newimg=np.array(np.power(b,c*(img-a))-1,np.uint8)
cv2.imshow('src',img)
cv2.imshow('dst',newimg)
cv2.waitKey()
cv2.destroyAllWindows()

