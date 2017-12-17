# -*- coding: utf-8 -*-
# @Time    : 2017-12-12 20:50
# @Author  : Storm
# @File    : chapter05-05.py
# variables_to_restore函数的使用样例

import tensorflow as tf

v = tf.Variable(0, dtype=tf.float32, name="v")
ema = tf.train.ExponentialMovingAverage(0.99)
print(ema.variables_to_restore())
# {'v/ExponentialMovingAverage': <tf.Variable 'v:0' shape=() dtype=float32_ref>}

saver = tf.train.Saver({"v/ExponentialMovingAverage": v})
with tf.Session() as sess:
    saver.restore(sess, "Saved_model/model2.ckpt")
    print(sess.run(v))
# 0.0999999
