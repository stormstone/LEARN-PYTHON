#10-14.py
import cv2  
  
fn="test3.jpg"  
myimg=cv2.imread(fn)  
img=cv2.cvtColor(myimg,cv2.COLOR_BGR2GRAY)  
  
newimg=cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,5,2)  
cv2.imshow('preview',newimg)  
cv2.waitKey()  
cv2.destroyAllWindows()  
