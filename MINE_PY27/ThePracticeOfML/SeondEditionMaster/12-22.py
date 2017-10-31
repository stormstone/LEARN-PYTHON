# -*- coding: utf-8 -*-
#coding:myhaspl@myhaspl.com
#采集视频生成视频帧数组
#12-22.py
import cv2
#设置需要采集视频的设备ID为0,从第个摄像头采集
mycap=cv2.VideoCapture(0)
myframes=[]
while True:
    ret,im=mycap.read()
    cv2.imshow('myvideo',im)
    #采集
    myframes.append(im)
    #每15毫秒采集1次
    key=cv2.waitKey(15)
    #空格键退出
    if key==32:
        break
#生成视频帧数组
myframes=np.array(myframes)

