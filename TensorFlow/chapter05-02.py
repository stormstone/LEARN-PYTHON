# -*- coding: utf-8 -*-
# @Time    : 2017-12-12 16:14
# @Author  : Storm
# @File    : chapter05-02.py
# 变量管理

import tensorflow as tf

# 1. 在上下文管理器“foo”中创建变量“v”。
# 在名字为foo的命名空间内创建名字为v的变量
with tf.variable_scope("foo"):
    v = tf.get_variable("v", [1], initializer=tf.constant_initializer(1.0))

# 因为在命名空间foo中已经存在名字为v的变量，所以下面的代码会出错
# with tf.variable_scope("foo"):
# v = tf.get_variable("v", [1])

# 在生成上下文管理器时，将参数reuse设置为True。这样tf.get_variable函数将直接获取已经声明的变量。
with tf.variable_scope("foo", reuse=True):
    v1 = tf.get_variable("v", [1])
print(v == v1)  # True

# 将参数reuse设置为True时，tf.get_variable将只能获取已经创建过的变量。下面的语句会出错。
# with tf.variable_scope("bar", reuse=True):
# v = tf.get_variable("v", [1])


# 2. 嵌套上下文管理器中的reuse参数的使用。
with tf.variable_scope("root"):
    print(tf.get_variable_scope().reuse)

    with tf.variable_scope("foo", reuse=True):
        print(tf.get_variable_scope().reuse)

        # 新建一个嵌套的上下文管理器，不指定reuse，这是reuse会与外面一层保持一致
        with tf.variable_scope("bar"):
            print(tf.get_variable_scope().reuse)

    print(tf.get_variable_scope().reuse)
# False
# True
# True
# False

# 3.通过variable_scope来管理变量,可以通过变量的名称来获取变量
v1 = tf.get_variable("v", [1])
print(v1.name)  # v:0

with tf.variable_scope("foo", reuse=True):
    v2 = tf.get_variable("v", [1])
print(v2.name)  # foo/v:0

with tf.variable_scope("foo"):
    with tf.variable_scope("bar"):
        v3 = tf.get_variable("v", [1])
        print(v3.name)  # foo/bar/v:0

v4 = tf.get_variable("v1", [1])
print(v4.name)  # v1:0

with tf.variable_scope("", reuse=True):
    v5 = tf.get_variable("foo/bar/v", [1])
    print(v5 == v3)  # True
    v6 = tf.get_variable("v1", [1])
    print(v6 == v4)  # True
