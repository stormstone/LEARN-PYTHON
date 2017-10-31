# -*- coding: utf-8 -*-   
#10-16.py
import cv2  
  
fn="test112.jpg"  
img=cv2.imread(fn)  
w=img.shape[1]    
h=img.shape[0]    
  
#放大,双立方插值  
newimg1=cv2.resize(img,(w*2,h*2),interpolation=cv2.INTER_CUBIC)  
#放大, 最近邻插值  
newimg2=cv2.resize(img,(w*2,h*2),interpolation=cv2.INTER_NEAREST)  
#放大, 象素关系重采样  
newimg3=cv2.resize(img,(w*2,h*2),interpolation=cv2.INTER_AREA)  
#缩小, 象素关系重采样  
newimg4=cv2.resize(img,(300,200),interpolation=cv2.INTER_AREA)  
  
  
cv2.imshow('preview1',newimg1)  
cv2.imshow('preview2',newimg2)  
cv2.imshow('preview3',newimg3)  
cv2.imshow('preview4',newimg4)  
cv2.waitKey()  
cv2.destroyAllWindows()  
