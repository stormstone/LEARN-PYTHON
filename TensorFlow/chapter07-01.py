# -*- coding: utf-8 -*-
# @Time    : 2017-12-18 11:56
# @Author  : Storm
# @File    : chapter07-01.py
# 使用TFRecord将MNIST输入数据转化为TFRecord的格式.

import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
import numpy as np


# 1. 将输入转化成TFRecord格式并保存。
# 定义函数转化变量类型。
# 生成整数型的属性
def _int64_feature(value):
    return tf.train.Feature(int64_list=tf.train.Int64List(value=[value]))


# 生成字符串型的属性
def _bytes_feature(value):
    return tf.train.Feature(bytes_list=tf.train.BytesList(value=[value]))


# 读取mnist数据。
mnist = input_data.read_data_sets("datasets/MNIST_data", dtype=tf.uint8, one_hot=True)
images = mnist.train.images
# 训练数据所对应的正确答案，可以作为一个属性保存在TFRecord中。
labels = mnist.train.labels
# 训练数据的图像分辨率，可以作为Example中的一个属性。
pixels = images.shape[1]
num_examples = mnist.train.num_examples

# 输出TFRecord文件的地址。
filename = "datasets/Records/output.tfrecords"
writer = tf.python_io.TFRecordWriter(filename)
for index in range(num_examples):
    # 将图像矩阵转化成一个字符串。
    image_raw = images[index].tostring()

    # 将一个样例转化为Example Protocol Buffer，并将所有的信息写入这个数据结构。
    example = tf.train.Example(features=tf.train.Features(feature={
        'pixels': _int64_feature(pixels),
        'label': _int64_feature(np.argmax(labels[index])),
        'image_raw': _bytes_feature(image_raw)
    }))
    writer.write(example.SerializeToString())
writer.close()
print("TFRecord文件已保存。")


# 2. 读取TFRecord文件
# 读取文件。
reader = tf.TFRecordReader()
# 创建一个队列来维护输入文件列表。
filename_queue = tf.train.string_input_producer(["datasets/Records/output.tfrecords"])
# 从文件中读出一个样例，也可以使用read_up_to函数一次性读取多个样例。
_, serialized_example = reader.read(filename_queue)

# 解析读取的样例。
features = tf.parse_single_example(
    serialized_example,
    features={
        'image_raw': tf.FixedLenFeature([], tf.string),
        'pixels': tf.FixedLenFeature([], tf.int64),
        'label': tf.FixedLenFeature([], tf.int64)
    })

# tf.decode_raw可以将字符串解析成图像对应的像素数组。
images = tf.decode_raw(features['image_raw'], tf.uint8)
labels = tf.cast(features['label'], tf.int32)
pixels = tf.cast(features['pixels'], tf.int32)

sess = tf.Session()

# 启动多线程处理输入数据。
coord = tf.train.Coordinator()
threads = tf.train.start_queue_runners(sess=sess, coord=coord)

for i in range(10):
    image, label, pixel = sess.run([images, labels, pixels])
