# -*- coding: utf-8 -*-
#10-37.py
import cv2  
import numpy as np  
from scipy import signal  
fn="test6.jpg"  
myimg=cv2.imread(fn)  
img=cv2.cvtColor(myimg,cv2.COLOR_BGR2GRAY)  
srcimg=np.array(img,np.double)  
myh=np.array([[0,1,0],[1,-4,1],[0,1,0]])  
  
myj=signal.convolve2d(srcimg,myh,mode="same")  
jgimg=img-myj  
cv2.imshow('src',img)  
cv2.imshow('dst',jgimg)  
cv2.waitKey()  
cv2.destroyAllWindows()  
