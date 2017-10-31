# -*- coding: utf-8 -*-
#coding:myhaspl@myhaspl.com
#采集视频
#12-21.py
import cv2
#设置需要采集视频的设备ID为0,从第个摄像头采集
mycap=cv2.VideoCapture(0)
id=0
while True:
    ret,im=mycap.read()
    cv2.imshow('myvideo',im)
    #每15毫秒采集1次
    key=cv2.waitKey(15)
    #空格键退出
    if key==32:
        break
    #c键采集
    elif key==ord('c'):
        cv2.imwrite('vd_'+str(id)+'.png',im)
        id+=1
    