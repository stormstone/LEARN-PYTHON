# -*- coding: utf-8 -*-     
#非线性锐化滤波，sobel算子变换  
#code:myhaspl@myhaspl.com  
#10-39.py
import cv2  
  
fn="test6.jpg"  
myimg=cv2.imread(fn)  
img=cv2.cvtColor(myimg,cv2.COLOR_BGR2GRAY)  
  
jgimg=cv2.Sobel(img,0,1,1)  
cv2.imshow('src',img)  
cv2.imshow('dst',jgimg)  
cv2.waitKey()  
cv2.destroyAllWindows() 
