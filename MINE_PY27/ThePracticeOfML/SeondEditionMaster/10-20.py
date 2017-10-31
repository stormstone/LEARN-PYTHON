#10-20.py
import cv2
import numpy as np
fn="test3.jpg"
myimg=cv2.imread(fn)
img=cv2.cvtColor(myimg,cv2.COLOR_BGR2GRAY)  
jg_img=np.array(40*np.log(img+1),np.uint8)
cv2.imshow('src',img)
cv2.imshow('dst',jg_img)
cv2.waitKey()
cv2.destroyAllWindows()
