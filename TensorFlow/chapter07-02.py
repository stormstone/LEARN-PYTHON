# -*- coding: utf-8 -*-
# @Time    : 2017-12-18 16:17
# @Author  : Storm
# @File    : chapter07-02.py
# 图像数据处理

import matplotlib.pyplot as plt
import tensorflow as tf
import numpy as np
import os

# 路径
IMG_DIR = 'datasets/cat'
IMG_NAME = 'cat.jpg'

# 读取图像的原始数据
image_raw_data = tf.gfile.FastGFile(os.path.join(IMG_DIR, IMG_NAME), 'rb').read()

with tf.Session() as sess:
    # 1.图像编码处理
    # 将图像使用jpeg的格式解码从而得到对应的三维矩阵。
    img_data = tf.image.decode_jpeg(image_raw_data)

    print(img_data.eval())
    # 显示图像
    plt.imshow(img_data.eval())
    plt.show()

    # 将数据的类型转化成实数方便处理
    img_data = tf.image.convert_image_dtype(img_data, dtype=tf.uint8)

    # 将表示一张图像的三维矩阵从新安装jpeg格式编码存入文件中。
    encoded_image = tf.image.encode_jpeg(img_data)
    with tf.gfile.GFile(os.path.join(IMG_DIR, 'cat_jpeg.jpeg'), 'wb')as f:
        f.write(encoded_image.eval())

    # 2.图像大小调整
    resized = tf.image.resize_images(img_data, [300, 300], method=0)
    # TensorFlow的函数处理图片后存储的数据是float32格式的，需要转换成uint8才能正确打印图片。
    print("Digital type: ", resized.dtype)
    cat = np.asarray(resized.eval(), dtype='uint8')
    # tf.image.convert_image_dtype(rgb_image, tf.float32)
    plt.imshow(cat)
    plt.savefig("datasets/cat/cat-大小调整.jpg")
    plt.show()

    # 裁剪和填充图片
    croped = tf.image.resize_image_with_crop_or_pad(img_data, 1000, 1000)
    padded = tf.image.resize_image_with_crop_or_pad(img_data, 3000, 3000)
    plt.imshow(croped.eval())
    plt.savefig("datasets/cat/cat-裁剪图片.jpg")
    plt.show()
    plt.imshow(padded.eval())
    plt.savefig("datasets/cat/cat-填充图片.jpg")
    plt.show()
    # 截取图片
    central_cropped = tf.image.central_crop(img_data, 0.5)
    plt.imshow(central_cropped.eval())
    plt.savefig("datasets/cat/cat-截取图片.jpg")
    plt.show()

    # 3.图像翻转
    # 上下翻转
    flipped1 = tf.image.flip_up_down(img_data)
    plt.imshow(flipped1.eval())
    plt.savefig("datasets/cat/cat-上下翻转.jpg")
    # 左右翻转
    flipped2 = tf.image.flip_left_right(img_data)
    plt.imshow(flipped2.eval())
    plt.savefig("datasets/cat/cat-左右翻转.jpg")

    # 对角线翻转
    transposed = tf.image.transpose_image(img_data)
    plt.imshow(transposed.eval())
    plt.savefig("datasets/cat/cat-对角翻转.jpg")
    plt.show()

    # 以一定概率上下翻转图片。
    flipped3 = tf.image.random_flip_up_down(img_data)
    plt.imshow(flipped3.eval())
    plt.savefig("datasets/cat/cat-一定概率上下翻转.jpg")
    # 以一定概率左右翻转图片。
    flipped4 = tf.image.random_flip_left_right(img_data)
    plt.imshow(flipped4.eval())
    plt.savefig("datasets/cat/cat-一定概率左右翻转.jpg")

    # 4.图像色彩调整
    # 将图片的亮度-0.5。
    adjusted = tf.image.adjust_brightness(img_data, -0.5)
    plt.imshow(adjusted.eval())
    plt.savefig("datasets/cat/cat-亮度减0.5.jpg")

    # 将图片的亮度+0.5
    adjusted = tf.image.adjust_brightness(img_data, 0.5)
    plt.imshow(adjusted.eval())
    plt.savefig("datasets/cat/cat-亮度加0.5.jpg")

    # 在[-max_delta, max_delta)的范围随机调整图片的亮度。
    adjusted = tf.image.random_brightness(img_data, max_delta=0.5)
    plt.imshow(adjusted.eval())
    plt.savefig("datasets/cat/cat-随机调整亮度.jpg")

    # 将图片的对比度-5
    adjusted = tf.image.adjust_contrast(img_data, -5)
    plt.imshow(adjusted.eval())
    plt.savefig("datasets/cat/cat-对比度减0.5.jpg")

    # 将图片的对比度+5
    adjusted = tf.image.adjust_contrast(img_data, 5)
    plt.imshow(adjusted.eval())
    plt.savefig("datasets/cat/cat-对比度加0.5.jpg")

    # 在[lower, upper]的范围随机调整图的对比度。
    lower = 1
    upper = 5
    adjusted = tf.image.random_contrast(img_data, lower, upper)
    plt.imshow(adjusted.eval())
    plt.savefig("datasets/cat/cat-随机调整对比度.jpg")
    plt.show()

    # 添加色相和饱和度
    adjusted = tf.image.adjust_hue(img_data, 0.1)
    plt.imshow(adjusted.eval())
    plt.savefig("datasets/cat/cat-色相加0.1.jpg")
    adjusted = tf.image.adjust_hue(img_data, 0.3)
    plt.imshow(adjusted.eval())
    plt.savefig("datasets/cat/cat-色相加0.3.jpg")
    adjusted = tf.image.adjust_hue(img_data, 0.6)
    plt.imshow(adjusted.eval())
    plt.savefig("datasets/cat/cat-色相加0.6.jpg")
    adjusted = tf.image.adjust_hue(img_data, 0.9)
    plt.imshow(adjusted.eval())
    plt.savefig("datasets/cat/cat-色相加0.9.jpg")

    # 在[-max_delta, max_delta]的范围随机调整图片的色相。max_delta的取值在[0, 0.5]之间。
    max_delta = 0.3
    adjusted = tf.image.random_hue(img_data, max_delta)
    plt.imshow(adjusted.eval())
    plt.savefig("datasets/cat/cat-随机调整色相.jpg")

    # 将图片的饱和度-5。
    adjusted = tf.image.adjust_saturation(img_data, -5)
    plt.imshow(adjusted.eval())
    plt.savefig("datasets/cat/cat-饱和度减5.jpg")
    # 将图片的饱和度+5。
    adjusted = tf.image.adjust_saturation(img_data, 5)
    plt.imshow(adjusted.eval())
    plt.savefig("datasets/cat/cat-饱和度加5.jpg")
    # 在[lower, upper]的范围随机调整图的饱和度。
    adjusted = tf.image.random_saturation(img_data, lower, upper)
    plt.imshow(adjusted.eval())
    plt.savefig("datasets/cat/cat-随机调整饱和度.jpg")
    plt.show()

    # 5.处理标注框
    boxes = tf.constant([[[0.05, 0.05, 0.9, 0.7], [0.35, 0.47, 0.5, 0.56]]])

    begin, size, bbox_for_draw = tf.image.sample_distorted_bounding_box(
        tf.shape(img_data), bounding_boxes=boxes)

    batched = tf.expand_dims(tf.image.convert_image_dtype(img_data, tf.float32), 0)
    image_with_box = tf.image.draw_bounding_boxes(batched, bbox_for_draw)

    distorted_image = tf.slice(img_data, begin, size)
    plt.imshow(distorted_image.eval())
    plt.savefig("datasets/cat/cat-标注框.jpg")
    plt.show()
