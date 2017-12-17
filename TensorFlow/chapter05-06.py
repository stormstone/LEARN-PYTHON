# -*- coding: utf-8 -*-
# @Time    : 2017-12-14 10:15
# @Author  : Storm
# @File    : chapter05-06.py

import tensorflow as tf

v1 = tf.Variable(tf.constant(1.0, shape=[1]), name='v1')
v2 = tf.Variable(tf.constant(2.0, shape=[1]), name='v2')
result1 = v1 + v2

saver = tf.train.Saver()
saver.export_meta_graph("Saved_model/model-0506.ckpt.meda.json", as_text=True)
