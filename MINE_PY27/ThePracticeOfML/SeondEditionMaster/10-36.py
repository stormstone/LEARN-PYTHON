# -*- coding: utf-8 -*-     
#卷积滤波  
#code:myhaspl@myhaspl.com  
#10-36.py
import cv2  
import numpy as np  
fn="test112.jpg"  
myimg=cv2.imread(fn)  
img=cv2.cvtColor(myimg,cv2.COLOR_BGR2GRAY)  
myh=np.array([[0,1,0],[1,-4,1],[0,1,0]])  
jgimg=cv2.filter2D(img,-1,myh)  
cv2.imshow('src',img)  
cv2.imshow('dst',jgimg)  
cv2.waitKey()  
cv2.destroyAllWindows()  
