# -*- coding: utf-8 -*-
# @Time    : 2017-12-10 16:40
# @Author  : Storm
# @File    : mytest.py

import tensorflow as tf

# tf.constant是一个计算，这个计算的结果为一个张量，保存在变量a中。
a = tf.constant([1.0, 2.0], name="a")
b = tf.constant([2.0, 3.0], name="b")
result = tf.add(a, b, name="add")
print(result)
