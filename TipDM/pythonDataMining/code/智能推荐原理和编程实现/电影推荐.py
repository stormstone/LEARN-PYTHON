# -*- coding: utf-8 -*-
"""
Created on Fri Aug 18 10:50:07 2017

@author: Administrator
"""

import pandas as pd
import numpy as np

# 读取数据  
data = {'Lisa Rose': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.5,
                      'Just My Luck': 3.0, 'Superman Returns': 3.5, 'You, Me and Dupree': 2.5},
        'Gene Seymour': {'Lady in the Water': 3.0, 'Snakes on a Plane': 3.5,
                         'Just My Luck': 1.5, 'The Night Listener': 3.0},
        'Michael Phillips': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.0,
                             'Superman Returns': 3.5, 'The Night Listener': 4.0},
        'Claudia Puig': {'Snakes on a Plane': 3.5, 'Just My Luck': 3.0,
                         'The Night Listener': 4.5, 'You, Me and Dupree': 2.5},
        'Mick LaSalle': {'Just My Luck': 2.0, 'Lady in the Water': 3.0, 'Superman Returns': 3.0,
                         'The Night Listener': 3.0, 'You, Me and Dupree': 2.0},
        'Jack Matthews': {'Snakes on a Plane': 4.0, 'The Night Listener': 3.0, 'Superman Returns': 5.0,
                          'You, Me and Dupree': 3.5},
        'Toby': {'Snakes on a Plane': 4.5, 'You, Me and Dupree': 1.0, 'Superman Returns': 4.0}}

# 转换为数据框  
data = pd.DataFrame(data)
# 将数据中的空值nan变为0  
data = data.fillna(0)
# 转置，每一列代表一个电影  
mdata = data.T

# 计算不同电影的相似度，将数据规范化为[ 0，1 ]  
corr = mdata.corr(method='pearson')
corr = 0.5 + corr * 0.5
d1 = mdata.ix[:, 0]
d2 = mdata.ix[:, 1]
d1.corr(d2, method='pearson')
# 或者
mcors = np.corrcoef(mdata, rowvar=0)
mcors = 0.5 + mcors * 0.5
mcors = pd.DataFrame(mcors, columns=mdata.columns, index=mdata.columns)


# 计算每个用户的每个电影的分数 ：为没有用户评分的电影用相似度估算
# matrix:用户-电影矩阵  
# mcors:电影相关矩阵 
# score:得分   
def cal_score(matrix, mcors, item, user):
    totscore = 0
    totsims = 0
    score = 0
    if pd.isnull(matrix[item][user]) or matrix[item][user] == 0:
        for mitem in matrix.columns:
            if matrix[mitem][user] == 0:
                continue
            else:
                totscore += matrix[mitem][user] * mcors[item][mitem]
                totsims += mcors[item][mitem]
        score = totscore / totsims
    else:
        score = matrix[item][user]
    return score


cal_score(mdata, mcors, 'Just My Luck', 'Jack Matthews')
cal_score(mdata, mcors, 'Just My Luck', 'Toby')


# 计算得分矩阵
# score_matrix:不同用户的电影得分矩阵
def cal_matscore(matrix, mcors):
    score_matrix = pd.DataFrame(np.zeros(matrix.shape), columns=matrix.columns, index=matrix.index)
    for mitem in score_matrix.columns:
        for muser in score_matrix.index:
            score_matrix[mitem][muser] = cal_score(matrix, mcors, mitem, muser)
    return score_matrix


# give recommendations: depending on the score matrix  
# matrix: 矩阵:用户-电影矩阵
# score_matrix:不同用户的电影得分矩阵   
# n: 推荐系数
def recommend(matrix, score_matrix, user, n):
    user_ratings = matrix.ix[user]
    not_rated_item = user_ratings[user_ratings == 0]
    recom_items = {}
    for item in not_rated_item.index:
        recom_items[item] = score_matrix[item][user]
    recom_items = pd.Series(recom_items)
    recom_items = recom_items.sort_values(ascending=False)
    return recom_items[:n]


# main
score_matrix = cal_matscore(mdata, mcors)
for i in range(10):
    user = input(str(i) + 'please input the name of user:')
    print(recommend(mdata, score_matrix, user, 2))

#### 检验
user = 'Toby'
user_ratings = mdata.ix[user]
not_rated_item = user_ratings[user_ratings == 0]
recom_items = {}
for item in not_rated_item.index:
    recom_items[item] = score_matrix[item][user]
recom_items = pd.Series(recom_items)
recom_items = recom_items.sort_values(ascending=False)

score_matrix = np.zeros(mdata.shape)
score_matrix = pd.DataFrame(score_matrix, columns=mdata.columns, index=mdata.index)
for mitem in score_matrix.columns:
    for muser in score_matrix.index:
        score_matrix[mitem][muser] = cal_score(mdata, mcors, mitem, muser)

totscore = 0
totsims = 0
score = 0
if pd.isnull(mdata[item][user]) or mdata[item][user] == 0:
    for mitem in mdata.columns:
        if mdata[mitem][user] == 0:
            continue
        else:
            totscore += mdata[mitem][user] * mcors[item][mitem]
            totsims += mcors[item][mitem]
    score = totscore / totsims
else:
    score = mdata[item][user]
item = 'Superman Returns'
mitem = 'You, Me and Dupree'
