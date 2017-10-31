#10-13.py
import cv2  

fn="test3.jpg"  
myimg=cv2.imread(fn)  
img=cv2.cvtColor(myimg,cv2.COLOR_BGR2GRAY)  

retval, newimg=cv2.threshold(img,40,255,cv2.THRESH_BINARY)  
cv2.imshow('preview',newimg)  
cv2.waitKey()  
cv2.destroyAllWindows() 
