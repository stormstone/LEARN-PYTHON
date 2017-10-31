# -*- coding: utf-8 -*- 
#10-17.py  
import cv2  
  
fn="test3.jpg"  
img=cv2.imread(fn)  
w=img.shape[1]    
h=img.shape[0]    
#得到仿射变换矩阵，完成旋转  
#中心  
mycenter=(h/2,w/2)  
#旋转角度  
myangle=90  
#缩放尺度  
myscale=0.5  
#仿射变换完成缩小并旋转  
transform_matrix=cv2.getRotationMatrix2D(mycenter,myangle,myscale)  
  
newimg=cv2.warpAffine(img,transform_matrix,(w,h))  
cv2.imshow('preview',newimg)  
  
cv2.waitKey()  
cv2.destroyAllWindows()  
