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
q = tf.FIFOQueue(2, "int32")
init = q.enqueue_many(([0, 10],))
x = q.dequeue()
y = x + 1
q_inc = q.enqueue([y])
with tf.Session() as sess:
    init.run()
    for _ in range(5):
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
threads = [threading.Thread(target=MyLoop, args=(coord, i,)) for i in range(5)]
for t in threads: t.start()
coord.join(threads)

# 4.多线程队列操作
queue = tf.FIFOQueue(100, "float")
enqueue_op = queue.enqueue([tf.random_normal([1])])
qr = tf.train.QueueRunner(queue, [enqueue_op] * 5)
tf.train.add_queue_runner(qr)
out_tensor = queue.dequeue()
with tf.Session() as sess:
    coord = tf.train.Coordinator()
    threads = tf.train.start_queue_runners(sess=sess, coord=coord)
    for _ in range(3): print(sess.run(out_tensor)[0])
    coord.request_stop()
    coord.join(threads)
