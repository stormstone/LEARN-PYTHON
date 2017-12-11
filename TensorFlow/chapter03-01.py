# -*- coding: utf-8 -*-
# @Time    : 2017-12-10 18:08
# @Author  : Storm
# @File    : chapter03-01.py
# TensorFlow基础，张量，计算图，会话等

import tensorflow as tf

# tf.constant是一个计算，这个计算的结果为一个张量，保存在变量a中。
a = tf.constant([1.0, 2.0], name="a")
b = tf.constant([2.0, 3.0], name="b")
result = tf.add(a, b, name="add")
print(result)
'''
输出为：
    Tensor("add:0", shape=(2,), dtype=float32)

一个张量中主要保存了三个属性：名字（name）、维度（shape）、类型（type）。
'''

g1 = tf.Graph()
with g1.as_default():
    # 在计算图g1中定义变量“v”,并设置初始值为0。
    v = tf.get_variable("v", shape=[1], initializer=tf.zeros_initializer())

g2 = tf.Graph()
with g2.as_default():
    # 在计算图g2中定义变量“v”,并设置初始值为1。
    v = tf.get_variable("v", shape=[1], initializer=tf.ones_initializer())

# 在计算图g1中读取变量“v”的值。
with tf.Session(graph=g1) as sess:
    tf.initialize_all_variables().run()
    with tf.variable_scope("", reuse=True):
        # 在计算图g1中，取变量“v”的值为0，输出为[0.]。
        print(sess.run(tf.get_variable("v")))

# 在计算图g2中读取变量“v”的值。
with tf.Session(graph=g2) as sess:
    tf.initialize_all_variables().run()
    with tf.variable_scope("", reuse=True):
        # 在计算图g2中，取变量“v”的值为1，输出为[1.]。
        print(sess.run(tf.get_variable("v")))

# 创建一个会话
sess = tf.Session()
# 使用这个创建好的会话来得到结果
sess.run(result)
# 关闭会话使得本次运行中的资源可以被释放
sess.close()

# 创建一个会话，并通过python中的上下文管理器来管理这个会话
with tf.Session() as sess:
    sess.run(result)
# 不在需要调用Session.close()函数来关闭会话，
# 当上下文退出时会话关闭和资源释放自动完成

sess = tf.Session()
with sess.as_default():
    print(result.eval())
# 以下代码可以完成相同的功能
print(sess.run(result))
print(result.eval(session=sess))

sess = tf.InteractiveSession()
print(result.eval())
sess.close()

config = tf.ConfigProto(allow_soft_placement=True, log_device_placement=True)
sess1 = tf.InteractiveSession(config=config)
sess2 = tf.Session(config=config)
