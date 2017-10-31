# -*- coding: utf-8 -*-     
#code:myhaspl@myhaspl.com  
#差分运动检测，基于背景图像与当前帧差来检测画面中是否有运动的物体
#12-24.py
import cv2  
import numpy as np  

#读取运动序列图像
fn=[]
for i in xrange(6):
    fn.append("mv"+str(i+1)+".png")

img=[]
colorimg=[]
myimg=[]

for i in xrange(6):
    tmpimg=(cv2.imread(fn[i]))
    colorimg.append(tmpimg)
    myimg=cv2.cvtColor(tmpimg,cv2.COLOR_BGR2GRAY)  
    img.append(myimg)

#差分计算
myimg=colorimg[0].copy()
w=myimg.shape[1]  
h=myimg.shape[0] 

moveimg=np.zeros((h,w,3),np.uint8 )
for ii in xrange(5):

    print u"开始分析第"+str(ii+2)+u"个运动图像..."
    myd=img[ii+1]-img[0]
    #生成差分矩阵
    THRESHOLD=int(np.median(abs(myd)))#取中位数做为阀值
    mymove=np.ones([h,w],np.uint8)
    for i in xrange(h):
        for j in xrange(w):
            if abs(myd[i,j])<THRESHOLD or myd[i,j]==0:
                mymove[i,j]=0
    #如果有物体运动则输出报警            
    if np.sum(mymove)>0 :
        print u"第"+str(ii+2)+u"个运动图像发生了变化!"
        moveimg=colorimg[ii+1]*0.16+colorimg[ii]*0.16+moveimg
        moveimg=np.array(moveimg,np.uint8)
     
#显示移动部分
showimg=moveimg
cv2.imshow("move",showimg)
cv2.waitKey()  
cv2.destroyAllWindows() 