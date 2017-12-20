# -*- coding: utf-8 -*-
# @Time    : 2017-12-19 15:33
# @Author  : Storm
# @File    : chapter07-04.py
# 队列操作

import tensorflow as tf
import numpy as np
import threading
import time

# 1. 创建队列，并操作里面的元素。
# 指定队列中最多可以保存两个元素，并指定类型为整数。
q = tf.FIFOQueue(2, "int32")
# 初始化队列中的元素。
init = q.enqueue_many(([0, 10],))
# 使用dequeue函数将队列中的第一个元素取出。
x = q.dequeue()
y = x + 1
# 将加一后的值再重新加入队列。
q_inc = q.enqueue([y])
with tf.Session() as sess:
    # 运行队列初始化操作。
    init.run()
    for _ in range(5):
        # 运行q_inc将执行数据出队列，出队的元素加一，重新加入队列的过程。
        v, _ = sess.run([x, q_inc])
        print(v)


# 2. 每隔1秒判断是否需要停止并打印自己的ID。
def MyLoop(coord, worker_id):
    while not coord.should_stop():
        if np.random.rand() < 0.1:
            print("Stoping from id: %d\n" % worker_id, )
            coord.request_stop()
        else:
            print("Working on id: %d\n" % worker_id, )
        time.sleep(1)


# 3. 创建、启动并退出线程。
coord = tf.train.Coordinator()
# 声明创建5个线程
threads = [threading.Thread(target=MyLoop, args=(coord, i,)) for i in range(5)]
for t in threads: t.start()
coord.join(threads)

# 4.多线程队列操作
queue = tf.FIFOQueue(100, "float")
# 定义队列的入队操作
enqueue_op = queue.enqueue([tf.random_normal([1])])
# tf.train.QueueRunner来创建多个线程运行队列的入队操作。
qr = tf.train.QueueRunner(queue, [enqueue_op] * 5)
# 将定义过的QueueRunner加入TensorFlow计算图上指定的集合。
tf.train.add_queue_runner(qr)
# 定义出队操作
out_tensor = queue.dequeue()
with tf.Session() as sess:
    coord = tf.train.Coordinator()
    # 使用tf.train.QueueRunner时，需要调用tf.train.start_queue_runners来启动所有线程。
    threads = tf.train.start_queue_runners(sess=sess, coord=coord)
    for _ in range(3): print(sess.run(out_tensor)[0])
    coord.request_stop()
    coord.join(threads)
