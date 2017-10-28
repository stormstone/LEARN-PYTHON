# -*- coding: utf-8 -*-
# 使用基于UBCF算法对电影进行推荐
from __future__ import print_function
import pandas as pd


def prediction(df, userdf, Nn=15):  # Nn邻居个数
    corr = df.T.corr();
    rats = userdf.copy()
    for usrid in userdf.index:
        dfnull = df.loc[usrid][df.loc[usrid].isnull()]
        usrv = df.loc[usrid].mean()  # 评价平均值
        for i in range(len(dfnull)):
            nft = (df[dfnull.index[i]]).notnull()
            # 获取邻居列表
            if (Nn <= len(nft)):
                nlist = df[dfnull.index[i]][nft][:Nn]
            else:
                nlist = df[dfnull.index[i]][nft][:len(nft)]
            nlist = nlist[corr.loc[usrid, nlist.index].notnull()]
            nratsum = 0
            corsum = 0
            if (0 != nlist.size):
                nv = df.loc[nlist.index, :].T.mean()  # 邻居评价平均值
                for index in nlist.index:
                    ncor = corr.loc[usrid, index]
                    nratsum += ncor * (df[dfnull.index[i]][index] - nv[index])
                    corsum += abs(ncor)
                if (corsum != 0):
                    rats.at[usrid, dfnull.index[i]] = usrv + nratsum / corsum
                else:
                    rats.at[usrid, dfnull.index[i]] = usrv
            else:
                rats.at[usrid, dfnull.index[i]] = None
    return rats


def recomm(df, userdf, Nn=15, TopN=3):
    ratings = prediction(df, userdf, Nn)  # 获取预测评分
    recomm = []  # 存放推荐结果
    for usrid in userdf.index:
        # 获取按NA值获取未评分项
        ratft = userdf.loc[usrid].isnull()
        ratnull = ratings.loc[usrid][ratft]
        # 对预测评分进行排序
        if (len(ratnull) >= TopN):
            sortlist = (ratnull.sort_values(ascending=False)).index[:TopN]
        else:
            sortlist = ratnull.sort_values(ascending=False).index[:len(ratnull)]
        recomm.append(sortlist)
    return ratings, recomm


############    主程序   ##############
if __name__ == "__main__":
    print("\n--------------使用基于UBCF算法对电影进行推荐 运行中... -----------\n")
    traindata = pd.read_csv('u1.base', sep='\t', header=None, index_col=None)
    testdata = pd.read_csv('u1.test', sep='\t', header=None, index_col=None)
    # 删除时间标签列
    traindata.drop(3, axis=1, inplace=True)
    testdata.drop(3, axis=1, inplace=True)
    # 行与列重新命名
    traindata.rename(columns={0: 'userid', 1: 'movid', 2: 'rat'}, inplace=True)
    testdata.rename(columns={0: 'userid', 1: 'movid', 2: 'rat'}, inplace=True)
    traindf = traindata.pivot(index='userid', columns='movid', values='rat')
    testdf = testdata.pivot(index='userid', columns='movid', values='rat')
    traindf.rename(index={i: 'usr%d' % (i) for i in traindf.index}, inplace=True)
    traindf.rename(columns={i: 'mov%d' % (i) for i in traindf.columns}, inplace=True)
    testdf.rename(index={i: 'usr%d' % (i) for i in testdf.index}, inplace=True)
    testdf.rename(columns={i: 'mov%d' % (i) for i in testdf.columns}, inplace=True)
    userdf = traindf.loc[testdf.index]
    # 获取预测评分和推荐列表
    trainrats, trainrecomm = recomm(traindf, userdf)
