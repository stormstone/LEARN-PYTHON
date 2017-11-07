# -*- coding: utf-8 -*-
"""
Created on Sat Nov  4 20:03:59 2017

@author: 45543
"""
## 导入所需库
import pandas as pd
import jieba

## 读取文件
data = pd.read_csv('./data/huizong.csv', sep=',', encoding='utf-8')

data['品牌'].value_counts()  # 查看商品类型
## 提取“美的”商品的评论
meidi = data[data.品牌 == '美的']
meidi.head()

comment = meidi.评论  # 提取评论
comment.shape  # 长度,len(comment)
comment.drop_duplicates()  # 去重
comment.shape

meidi['型号'].value_counts()  # 型号统计


def condense_1(str):
    # 这里i代表每次处理的字符单位数，如i=1时处理“好好好好”的情况，i=2时处理“很好很好很好”的情况
    # i=1&i=2时用一种处理方式，即当重复数量>2时才进行压缩，因为出现“滔滔不绝”、“美的的确好”
    # 跟“容我思考思考”“这真的真的好看”等不好归为冗余的情况。但当出现3次及以上时基本就是冗余了。
    for i in [1, 2]:
        j = 0
        while j < len(str) - 2 * i:
            # 判断重复了至少两次
            if str[j: j + i] == str[j + i: j + 2 * i] and str[j: j + i] == str[j + 2 * i: j + 3 * i]:
                k = j + 2 * i
                while k + i < len(str) and str[j: j + i] == str[k + i: k + 2 * i]:
                    k += i
                str = str[: j + i] + str[k + i:]
            j += 1
        i += 1

    # i=3&i=4时用一种处理方式，当重复>1时就进行压缩，因为3个字以上时重复不再构成成语或其他常用语，
    # 基本上即使冗余了。因为大于五个字的重复比较少出现，为了减少算法复杂度可以只处理到i=4。
    for i in [3, 4, 5]:
        j = 0
        while j < len(str) - 2 * i:
            # 判断重复了至少一次
            if str[j: j + i] == str[j + i: j + 2 * i]:
                k = j + i
                while k + i < len(str) and str[j: j + i] == str[k + i: k + 2 * i]:
                    k += i
                str = str[: j + i] + str[k + i:]
            j += 1
        i += 1

    return str


condense_1('天真的真的真的好蓝')
condense_1('天呵呵呵呵好蓝')
comment.iloc[14]  # 例子
comment.astype('str').apply(lambda x: len(x)).sum()  # 统计总评论的字符长度
data1 = comment.astype('str').apply(lambda x: condense_1(x))  # 去除重复词
data1.apply(lambda x: len(x)).sum()
data1.iloc[14]  # 转换后效果
data2 = data1.apply(lambda x: len(x))
data3 = pd.concat((data1, data2), axis=1)  # 合并
data3.columns = ['评论', '长度']
data3.head()

data3['长度'].value_counts().sort_index()[:10]  # 长度前十的数量统计
data4 = data3.loc[data3['长度'] > 4, '评论']  # 筛选长度大于4的评论
data4.shape

## 分词
list(jieba.cut('我爱北京天安门，天安门前国旗升'))
data5 = data4.apply(lambda x: list(jieba.cut(x)))
data5.head()

## 加载停止词
stop = pd.read_csv('./data/stoplist1.txt', sep='yang', encoding='utf-8', header=None)
# sep设置为文档内不包含的内容，否则出错
stop = [' ', ''] + list(stop[0])  # Pandas自动过滤了空格符，这里手动添加
data6 = data5.apply(lambda x: [i for i in x if i not in stop])
# 去除停止词前后对比
data6.apply(lambda x: len(x)).sum()
data5.apply(lambda x: len(x)).sum()

## 加载情感词表
feeling = pd.read_csv('./data/BosonNLP_sentiment_score.txt', sep=' ', header=None)
feeling.columns = ['word', 'score']
feeling.head()

feel = list(feeling['word'])


def classfi(list1):
    SumScore = 0
    for i in list1:
        if i in feel:
            SumScore += feeling['score'][feel.index(i)]
    return SumScore


print('-----这里会运行20分钟...')
date7 = data6.apply(lambda x: classfi(x))  # 对评论情感打分

pos = data6[date7 >= 0]
neg = data6[date7 < 0]
data6[date7 == 0]
pos.to_csv('./data/meidi_jd_pos_delStop1.txt', encoding='utf-8', index=False, header=False)
neg.to_csv('./data/meidi_jd_neg_delStop1.txt', encoding='utf-8', index=False, header=False)

negfile = './data/meidi_jd_neg_delStop.txt'
posfile = './data/meidi_jd_pos_delStop.txt'

neg = pd.read_csv(negfile, encoding='utf-8', header=None)  # 读入数据
pos = pd.read_csv(posfile, encoding='utf-8', header=None)

neg[1] = neg[0].apply(lambda s: s.split(' '))  # 定义一个分割函数，然后用 apply 广播
pos[1] = pos[0].apply(lambda s: s.split(' '))

from gensim import corpora, models

## 负面主题分析
neg_dict = corpora.Dictionary(neg[1])  # 建立词典
neg_corpus = [neg_dict.doc2bow(i) for i in neg[1]]  # 建立语料库
neg_lda = models.LdaModel(neg_corpus, num_topics=3, id2word=neg_dict)  # LDA 模型训练
print("\n负面评价")
for i in range(3):
    print("主题%d : " % i)
    print(neg_lda.print_topic(i))  # 输出每个主题

## 正面主题分析
pos_dict = corpora.Dictionary(pos[1])
pos_corpus = [pos_dict.doc2bow(i) for i in pos[1]]
pos_lda = models.LdaModel(pos_corpus, num_topics=3, id2word=pos_dict)
print("\n正面评价")
for i in range(3):
    print("主题%d : " % i)
    print(pos_lda.print_topic(i))  # 输出每个主题
