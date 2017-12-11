# -*- coding: utf-8 -*-
# @Time    : 2017-12-10 21:55
# @Author  : Storm
# @File    : chapter04-01.py
# 损失函数对模型训练结果的影响

import tensorflow as tf
from numpy.random import RandomState

batch_size = 8

# 两个输入节点
x = tf.placeholder(tf.float32, shape=(None, 2), name='x-input')
# 一个输出节点
y_ = tf.placeholder(tf.float32, shape=(None, 1), name='y-input')

w1 = tf.Variable(tf.random_normal([2, 1], stddev=1, seed=1))
y = tf.matmul(x, w1)

# 自定义损失函数
loss_less = 10
loss_more = 1
# tf.where相当于问号表达式，参数一True时选择参数二，否则选择参数三
# tf.greater比较两个张量的大小
loss = tf.reduce_sum(tf.where(tf.greater(y, y_), (y - y_) * loss_more, (y_ - y) * loss_less))

train_step = tf.train.AdamOptimizer(0.001).minimize(loss)

rdm = RandomState(1)
dataset_size = 128
X = rdm.rand(dataset_size, 2)
# 加一个随机量，加入不可预测的噪音，否则不同损失函数的意义就不大了。噪音均值为0的小量。
Y = [[x1 + x2 + rdm.rand() / 10.0 - 0.05] for (x1, x2) in X]

# 训练神经网络
with tf.Session() as sess:
    init_op = tf.initialize_all_variables()
    sess.run(init_op)
    STEPS = 5000
    for i in range(STEPS):
        start = (i * batch_size) % dataset_size
        end = min(start + batch_size, dataset_size)
        sess.run(train_step, feed_dict={x: X[start:end], y_: Y[start:end]})
        print(sess.run(w1))
