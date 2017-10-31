# -*- coding: utf-8 -*-
#coding:myhaspl@myhaspl.com
#光流法
#12-25.py
import cv2
import numpy as np

def flowdraw(im,flow,step=14):
    #绘制光流
    h,w=im.shape[:2]
    y,x=np.mgrid[step/2:h:step,step/2:w:step].reshape(2,-1)
    fx,fy=flow[y,x].T
    #线终点
    lines=np.vstack([x,y,x+fx,y+fy]).T.reshape(-1,2,2)
    lines=np.int32(lines)
    #创建图像
    myvis=cv2.cvtColor(im,cv2.COLOR_GRAY2BGR)
    for (x1,y1),(x2,y2) in lines:
        cv2.line(myvis,(x1,y1),(x2,y2),(0,255,0),1)
        cv2.circle(myvis,(x1,y1),1,(0,255,0),-1)
    return myvis


#设置需要采集视频的设备ID为0,从第个摄像头采集
mycap=cv2.VideoCapture(0)
#前一个图像
ret,im=mycap.read()
prev_pic=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)

while True:
    ret,im=mycap.read()
    #采集
    pic=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)    
    #计算流
    myflow=cv2.calcOpticalFlowFarneback(prev_pic,pic,0.5,3,15,3,5,1,0)
    #上帧图像赋值
    prev_pic=pic
    #绘制流矢量
    cv2.imshow('myvideo flow ',flowdraw(pic,myflow))    
    #每15毫秒采集1次
    key=cv2.waitKey(15)    
    #空格键退出
    if key==32:
        break

     
    

