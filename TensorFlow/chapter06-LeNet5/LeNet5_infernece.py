# -*- coding: utf-8 -*-
# @Time    : 2017-12-17 18:45
# @Author  : Storm
# @File    : LeNet5_infernece.py

import tensorflow as tf

# 配置神经网络参数
INPUT_NODE = 784
OUTPUT_NODE = 10

IMAGE_SIZE = 28
NUM_CHANNELS = 1
NUM_LABELS = 10

# 第一层卷积层的尺寸和深度
CONV1_DEEP = 32
CONV1_SIZE = 5

# 第二层卷积层的尺寸和深度
CONV2_DEEP = 64
CONV2_SIZE = 5

# 全连接层的节点数
FC_SIZE = 512


def inference(input_tensor, train, regularizer):
    # 通过使用不同的命名空间来隔离不同层的变量。
    # 第一层卷积层的实现。和标准的LeNet-5模型不大一样，这里定义的卷积层输入为28*28*1的原始MNIST图片像素。
    # 因为卷积层中使用了全0填充，所以输出为28*28*32的矩阵。
    with tf.variable_scope('layer1-conv1'):
        conv1_weights = tf.get_variable(
            "weight", [CONV1_SIZE, CONV1_SIZE, NUM_CHANNELS, CONV1_DEEP],
            initializer=tf.truncated_normal_initializer(stddev=0.1))
        conv1_biases = tf.get_variable("bias", [CONV1_DEEP], initializer=tf.constant_initializer(0.0))
        # 使用边长为5,深度为32的过滤器,步长为1,使用全0填充
        conv1 = tf.nn.conv2d(input_tensor, conv1_weights, strides=[1, 1, 1, 1], padding='SAME')
        relu1 = tf.nn.relu(tf.nn.bias_add(conv1, conv1_biases))

    # 第二层池化层的实现。
    # 选用最大池化层，过滤器边长为2，步长为2，使用全0填充。
    # 这一层输入是上一层的输出，28*28*32，输出为14*14*32。
    with tf.name_scope("layer2-pool1"):
        pool1 = tf.nn.max_pool(relu1, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding="SAME")

    # 第三层卷积层的实现。输出为14*14*64。
    with tf.variable_scope("layer3-conv2"):
        conv2_weights = tf.get_variable(
            "weight", [CONV2_SIZE, CONV2_SIZE, CONV1_DEEP, CONV2_DEEP],
            initializer=tf.truncated_normal_initializer(stddev=0.1))
        conv2_biases = tf.get_variable("bias", [CONV2_DEEP], initializer=tf.constant_initializer(0.0))
        conv2 = tf.nn.conv2d(pool1, conv2_weights, strides=[1, 1, 1, 1], padding='SAME')
        relu2 = tf.nn.relu(tf.nn.bias_add(conv2, conv2_biases))

    # 第四层池化层的实现。输出为7*7*64。
    with tf.name_scope("layer4-pool2"):
        pool2 = tf.nn.max_pool(relu2, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME')
        # 将第四层池化层的输出转化为第五层全连接层的输入格式。
        pool_shape = pool2.get_shape().as_list()
        # 计算将矩阵拉直成向量之后的长度，长宽和深度的乘积。
        # pool_shape[0]为一个batch中数据的个数
        nodes = pool_shape[1] * pool_shape[2] * pool_shape[3]
        # 通过tf.reshape函数将第四层的输出变成一个batch的向量。
        reshaped = tf.reshape(pool2, [pool_shape[0], nodes])

    # 第五次全连接层的实现。输入向量长度为3136，输出为长度为512的向量。
    # dropout随机失活。
    with tf.variable_scope('layer5-fc1'):
        fc1_weights = tf.get_variable("weight", [nodes, FC_SIZE],
                                      initializer=tf.truncated_normal_initializer(stddev=0.1))
        # 只有全连接层的权重需要加入正则化。
        if regularizer != None: tf.add_to_collection('losses', regularizer(fc1_weights))
        fc1_biases = tf.get_variable("bias", [FC_SIZE], initializer=tf.constant_initializer(0.1))

        fc1 = tf.nn.relu(tf.matmul(reshaped, fc1_weights) + fc1_biases)
        if train: fc1 = tf.nn.dropout(fc1, 0.5)

    # 第六层全连接层的实现。输出为长度为10的向量。通过softmax之后就得到了最后的分类结果。
    with tf.variable_scope('layer6-fc2'):
        fc2_weights = tf.get_variable("weight", [FC_SIZE, NUM_LABELS],
                                      initializer=tf.truncated_normal_initializer(stddev=0.1))
        if regularizer != None: tf.add_to_collection('losses', regularizer(fc2_weights))
        fc2_biases = tf.get_variable("bias", [NUM_LABELS], initializer=tf.constant_initializer(0.1))
        logit = tf.matmul(fc1, fc2_weights) + fc2_biases

    return logit
