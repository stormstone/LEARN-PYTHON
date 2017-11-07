# -*- coding: utf-8 -*-
# @Time    : 2017-11-06 20:02
# @Author  : Storm
# @File    : code.py
import jieba
import pandas as pd
from gensim import models, corpora

## 1.导入数据
data = pd.read_csv('./data/huizong.csv', sep=',', encoding='utf-8')
data['品牌'].value_counts()
meidi = data[data.品牌 == '美的']
comment = meidi.评论
cshpe1 = comment.shape
comment.drop_duplicates()
cshpe2 = comment.shape
meidix = meidi['型号'].value_counts()


## 2.自定义函数实现机械压缩
def condense_1(str):
    for i in [1, 2]:
        j = 0
        while j < len(str) - 2 * i:
            if str[j:j + i] == str[j + i:j + 2 * i] and str[j:j + i] == str[j + 2 * i: j + 3 * i]:
                k = j + 2 * i
                while k + i < len(str) and str[j:j + i] == str[k + i: k + 2 * i]:
                    k += i  # k = k + i
                str = str[:j + i] + str[k + i:]
            j += 1
        i += 1
    for i in [3, 4, 5]:
        j = 0
        while j < len(str) - 2 * i:
            if str[j:j + i] == str[j + i:j + 2 * i]:
                k = j + i
                while k + i < len(str) and str[j:j + i] == str[k + i:k + 2 * i]:
                    k += i
                str = str[:j + i] + str[k + i:]
            j += 1
        i += 1
    return str


test_str = condense_1('天真的真的真的真的好漂亮')
# print(condense_1(test_str))
print(comment.iloc[14])
comment.astype('str').apply(lambda x: len(x)).sum()  # 1451934
data1 = comment.astype('str').apply(lambda x: condense_1(x))
print(data1.iloc[14])
data1.astype('str').apply(lambda x: len(x)).sum()  #
data2 = data1.apply(lambda x: len(x))
data3 = pd.concat((data1, data2), axis=1)
data3.columns = ['评论', '长度']
data3['长度'].value_counts().sort_index()[1:10]
data4 = data3.loc[data3['长度'] > 4, '评论']

## 3.分词
list(jieba.cut('我爱中国，天安门国旗'))
data5 = data4.apply(lambda x: list(jieba.cut(x)))
data5.head()
## 去除停用词
stop = pd.read_csv('./data/stoplist1.txt', sep='hui', encoding='utf-8', header=None)
stop = [' '] + list(stop[0])
data6 = data5.apply(lambda x: [i for i in x if i not in stop])
data6.head()

## 4.导入情感评价表
feeling = pd.read_csv('./data/BosonNLP_sentiment_score.txt', sep=' ', encoding='utf-8', header=None)
feeling.columns = ['word', 'score']

feel = list(feeling['word'])


## 5.对评论评分
def classfi(my_list):
    SumScore = 0
    for i in my_list:
        if i in feel:
            SumScore += feeling['score'][feel.index(i)]
    return SumScore


print('-----这里会运行20分钟...')
data7 = data6.apply(lambda x: classfi(x))

## 6.把评论划分为两部分：正向评论，负向评论
pos = data6[data7 >= 0]
neg = data6[data7 < 0]
data6[data7 == 0]

pos.to_csv('./data/pos.txt', encoding='utf-8', index=False, header=False)
neg.to_csv('./data/neg.txt', encoding='utf-8', index=False, header=False)

pos = pd.read_csv('./data/pos.txt', encoding='utf-8', header=None)
neg = pd.read_csv('./data/neg.txt', encoding='utf-8', header=None)

## 7.构造LDA模型，提取关键字
# 建立字典
pos_dic = corpora.Dictionary(pos[1])
# 建立语料库
pos_cor = [pos_dic.doc2bow(i) for i in pos[1]]
# 主题分析
pos_lda = models.LdaModel(pos_cor, num_topics=3, id2word=pos_dic)
# 打印主题
for i in range(3):
    print('正面主题', i, pos_lda.print_topic(i))

neg_dic = corpora.Dictionary(neg[1])
neg_cor = [neg_dic.doc2bow(i) for i in neg[1]]
neg_lda = models.LdaModel(neg_cor, num_topics=3, id2word=neg_dic)
for i in range(3):
    print('负面主题', i, neg_lda.print_topic(i))
