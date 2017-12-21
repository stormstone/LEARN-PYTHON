# -*- coding: utf-8 -*-
# @Time    : 2017-12-21 18:34
# @Author  : Storm
# @File    : chapter09-01.py
# TensorBoard简介

import tensorflow as tf

input1 = tf.constant([1.0, 2.0, 3.0], name="input1")
input2 = tf.Variable(tf.random_uniform([3]), name="input2")
output = tf.add_n([input1, input2], name="add")

# 生成一个写日志的writer，并将当前的TensorFlow计算图写入日志。
writer = tf.summary.FileWriter("TensorBoard/to/log", tf.get_default_graph())
writer.close()

#  不同的命名空间
with tf.variable_scope("foo"):
    a = tf.get_variable("bar", [1])
    print(a.name)

with tf.variable_scope("bar"):
    b = tf.get_variable("bar", [1])
    print(b.name)

#  tf.Variable和tf.get_variable的区别
with tf.name_scope("a"):
    a = tf.Variable([1])
    print(a.name)

    a = tf.get_variable("b", [1])
    print(a.name)

# TensorBoard可以根据命名空间来整理可视化效果图上的节点
with tf.name_scope("input1"):
    input1 = tf.constant([1.0, 2.0, 3.0], name="input2")
with tf.name_scope("input2"):
    input2 = tf.Variable(tf.random_uniform([3]), name="input2")
output = tf.add_n([input1, input2], name="add")

writer = tf.summary.FileWriter("TensorBoard/log/simple_example.log", tf.get_default_graph())
writer.close()
