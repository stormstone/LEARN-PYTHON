# -*- coding: utf-8 -*-
# @Time    : 2017-11-06 20:02
# @Author  : Storm
# @File    : day01.py

import pandas as pd
import jieba
from gensim import models, corpora

## 1.导入数据
data = pd.read_csv('./data/huizong.csv', sep=',', encoding='utf-8')
data['品牌'].value_counts()
meidi = data[data.品牌 == '美的']
comment = meidi.评论
print(comment.shape)
comment.drop_duplicates()
print(comment.shape)
print(meidi['型号'].value_counts())


## 2.自定义函数实现机械压缩

## 3.分词

## 4.导入情感评价表

## 5.对评论评分

## 6.把评论划分为两部分：正向评论，负向评论

## 7.构造LDA模型，提取关键字
