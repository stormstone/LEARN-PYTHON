# -*- coding: utf-8 -*-     
#code:myhaspl@myhaspl.com  
#10-23.py
import cv2  
fn="test112.jpg"  
myimg=cv2.imread(fn)  
img=cv2.cvtColor(myimg,cv2.COLOR_BGR2GRAY)  
newimg=cv2.equalizeHist(img)  
cv2.imshow('src',img)  
cv2.imshow('dst',newimg)  
cv2.waitKey()  
cv2.destroyAllWindows()  
