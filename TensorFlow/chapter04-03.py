# -*- coding: utf-8 -*-
# @Time    : 2017-12-11 15:16
# @Author  : Storm
# @File    : chapter04-03.py
# 滑动平均模型

import tensorflow as tf

# 定义一个变量用于计算滑动平均
v1 = tf.Variable(0, dtype=tf.float32)
# step变量模拟神经网络中迭代的轮数，可以用于动态控制衰减率
step = tf.Variable(0, trainable=False)

# 定义一个滑动平均的类，初始化时给定衰减率0.99和控制衰减率的变量step
ema = tf.train.ExponentialMovingAverage(0.99, step)
# 定义一个更新变量滑动平均的操作
maintain_averages_op = ema.apply([v1])

with tf.Session() as sess:
    init_op = tf.initialize_all_variables()
    sess.run(init_op)

    # 通过ema.average(v1)获取滑动平均之后变量的值
    print(sess.run([v1, ema.average(v1)]))  # 输出：[0.0, 0.0]

    # 更新变量v1的值到5
    sess.run(tf.assign(v1, 5))
    # 更新v1的滑动平均值。衰减率为min{0.99，(1+step)/(10+step)=0.1}=0.1
    # v1的滑动平均会被更新为 0.1*0+0.9*5=4.5
    sess.run(maintain_averages_op)
    print(sess.run([v1, ema.average(v1)]))  # 输出：[5.0, 4.5]

    # 更新step的值为1000
    sess.run(tf.assign(step, 1000))
    # 更新v1的值为10
    sess.run(tf.assign(v1, 10))
    # 更新v1的滑动平均值
    sess.run(maintain_averages_op)
    print(sess.run([v1, ema.average(v1)]))  # 输出：[10.0, 4.5549998]

    # 再次更新滑动平均值
    sess.run(maintain_averages_op)
    print(sess.run([v1, ema.average(v1)]))  # 输出：[10.0, 4.6094499]
