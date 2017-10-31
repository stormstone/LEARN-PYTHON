# -*- coding: utf-8 -*- 
#10-19.py
import cv2
import numpy as np
fn="test112.jpg"
img=cv2.imread(fn)
w=img.shape[1]  
h=img.shape[0]  
#得到透射变换矩阵
src=np.array([[0,0],[w-1,0],[w-1,h-1],[0,h-1]], dtype = np.float32)
dst=np.array([[w*0.08,h*0.01],[w*0.8,h*0.25],[w*0.8,h*0.9],[w*0.05,h*0.8]],dtype = np.float32)
transform_matrix=cv2.getPerspectiveTransform(src,dst)
print transform_matrix
#透射变换完成变形
newimg=cv2.warpPerspective(img,transform_matrix,(w,h))
cv2.imshow('preview',newimg)

cv2.waitKey()
cv2.destroyAllWindows()


