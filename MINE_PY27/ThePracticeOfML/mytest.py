# -*- coding: utf-8 -*-
# @Time    : 2017-10-31 16:52
# @Author  : Storm
# @File    : mytest.py

import cv2
fn="test1.jpg"

img = cv2.imread(fn)
cv2.imshow('preview',img)
cv2.waitKey()
cv2.destroyAllWindows()
