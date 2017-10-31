# -*- coding: utf-8 -*-     
#线性锐化滤波，拉普拉斯图像变换  
#code:myhaspl@myhaspl.com  
#10-38.py
import cv2  
  
fn="test6.jpg"  
myimg=cv2.imread(fn)  
img=cv2.cvtColor(myimg,cv2.COLOR_BGR2GRAY)  
  
jgimg=cv2.Laplacian(img,-1)  
cv2.imshow('src',img)  
cv2.imshow('dst',jgimg)  
cv2.waitKey()  
cv2.destroyAllWindows()  
