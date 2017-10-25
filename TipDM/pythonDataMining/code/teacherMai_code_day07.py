# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 14:27:51 2017

@author: xuan
"""
# k-means

import numpy as np
import matplotlib.pyplot as plt

from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs

plt.figure(figsize=(12, 12))

# 选取样本数量
n_samples = 1500
# 选取随机因子
random_state = 170
# 获取数据集
X, y = make_blobs(n_samples=n_samples, random_state=random_state)

# 聚类数量不正确时的效果
y_pred = KMeans(n_clusters=2, random_state=random_state).fit_predict(X)

plt.subplot(221)
plt.scatter(X[y_pred==0][:, 0], X[y_pred==0][:, 1], marker='x',color='b')
plt.scatter(X[y_pred==1][:, 0], X[y_pred==1][:, 1], marker='+',color='r')
plt.title("Incorrect Number of Blobs")

# 聚类数量正确时的效果
y_pred = KMeans(n_clusters=3, random_state=random_state).fit_predict(X)

plt.subplot(222)
plt.scatter(X[y_pred==0][:, 0], X[y_pred==0][:, 1], marker='x',color='b')
plt.scatter(X[y_pred==1][:, 0], X[y_pred==1][:, 1], marker='+',color='r')
plt.scatter(X[y_pred==2][:, 0], X[y_pred==2][:, 1], marker='1',color='m')
plt.title("Correct Number of Blobs")

# 类间的方差存在差异的效果
X_varied, y_varied = make_blobs(n_samples=n_samples,
                                cluster_std=[1.0, 2.5, 0.5],
                                random_state=random_state)
y_pred = KMeans(n_clusters=3, random_state=random_state).fit_predict(X_varied)

plt.subplot(223)
plt.scatter(X_varied[y_pred==0][:, 0], X_varied[y_pred==0][:, 1], marker='x',color='b')
plt.scatter(X_varied[y_pred==1][:, 0], X_varied[y_pred==1][:, 1], marker='+',color='r')
plt.scatter(X_varied[y_pred==2][:, 0], X_varied[y_pred==2][:, 1], marker='1',color='m')
plt.title("Unequal Variance")

# 类的规模差异较大的效果
X_filtered = np.vstack((X[y == 0][:500], X[y == 1][:100], X[y == 2][:10]))
y_pred = KMeans(n_clusters=3, random_state=random_state).fit_predict(X_filtered)

plt.subplot(224)
plt.scatter(X_filtered[y_pred==0][:, 0], X_filtered[y_pred==0][:, 1], marker='x',color='b')
plt.scatter(X_filtered[y_pred==1][:, 0], X_filtered[y_pred==1][:, 1], marker='+',color='r')
plt.scatter(X_filtered[y_pred==2][:, 0], X_filtered[y_pred==2][:, 1], marker='1',color='m')
plt.title("Unevenly Sized Blobs")

plt.show()

# 系统聚类

import numpy as np
import matplotlib.pyplot as plt

from sklearn.cluster import AgglomerativeClustering
from sklearn.datasets import make_blobs

plt.figure(figsize=(12, 12))

# 选取样本数量
n_samples = 1500
# 选取随机因子
random_state = 170
# 获取数据集
X, y = make_blobs(n_samples=n_samples, random_state=random_state)

# 聚类数量不正确时的效果
y_pred = AgglomerativeClustering(affinity='euclidean',linkage='ward',n_clusters=2).fit_predict(X)
# 选取欧几里德距离和离差平均和法

plt.subplot(221)
plt.scatter(X[y_pred==0][:, 0], X[y_pred==0][:, 1], marker='x',color='b')
plt.scatter(X[y_pred==1][:, 0], X[y_pred==1][:, 1], marker='+',color='r')
plt.title("Incorrect Number of Blobs")

# 聚类数量正确时的效果
y_pred = AgglomerativeClustering(affinity='euclidean',linkage='ward',n_clusters=3).fit_predict(X)

plt.subplot(222)
plt.scatter(X[y_pred==0][:, 0], X[y_pred==0][:, 1], marker='x',color='b')
plt.scatter(X[y_pred==1][:, 0], X[y_pred==1][:, 1], marker='+',color='r')
plt.scatter(X[y_pred==2][:, 0], X[y_pred==2][:, 1], marker='1',color='m')
plt.title("Correct Number of Blobs")

# 类间的方差存在差异的效果
X_varied, y_varied = make_blobs(n_samples=n_samples,
                                cluster_std=[1.0, 2.5, 0.5],
                                random_state=random_state)
y_pred = AgglomerativeClustering(affinity='euclidean',linkage='ward',n_clusters=3).fit_predict(X_varied)

plt.subplot(223)
plt.scatter(X_varied[y_pred==0][:, 0], X_varied[y_pred==0][:, 1], marker='x',color='b')
plt.scatter(X_varied[y_pred==1][:, 0], X_varied[y_pred==1][:, 1], marker='+',color='r')
plt.scatter(X_varied[y_pred==2][:, 0], X_varied[y_pred==2][:, 1], marker='1',color='m')
plt.title("Unequal Variance")

# 类的规模差异较大的效果
X_filtered = np.vstack((X[y == 0][:500], X[y == 1][:100], X[y == 2][:10]))
y_pred = AgglomerativeClustering(affinity='euclidean',linkage='ward',n_clusters=3).fit_predict(X_filtered)

plt.subplot(224)
plt.scatter(X_filtered[y_pred==0][:, 0], X_filtered[y_pred==0][:, 1], marker='x',color='b')
plt.scatter(X_filtered[y_pred==1][:, 0], X_filtered[y_pred==1][:, 1], marker='+',color='r')
plt.scatter(X_filtered[y_pred==2][:, 0], X_filtered[y_pred==2][:, 1], marker='1',color='m')
plt.title("Unevenly Sized Blobs")

plt.show()

# 密度聚类模型

import numpy as np

from sklearn.cluster import DBSCAN
from sklearn import metrics
from sklearn.datasets.samples_generator import make_blobs
from sklearn.preprocessing import StandardScaler


##############################################################################
# 获取make_blobs数据
centers = [[1, 1], [-1, -1], [1, -1]]
X, labels_true = make_blobs(n_samples=750, centers=centers, cluster_std=0.4,
                            random_state=0)
# 数据预处理
X = StandardScaler().fit_transform(X)
#使用sklearn.preprocessing.StandardScaler类，使用该类的好处在于
#可以保存训练集中的参数（均值、方差）直接使用其对象转换测试集数据。
##############################################################################
# 执行DBSCAN算法
db = DBSCAN(eps=0.3, min_samples=10).fit(X)
core_samples_mask = np.zeros_like(db.labels_, dtype=bool)
# 标记核心对象,后面作图需要用到
core_samples_mask[db.core_sample_indices_] = True
# 算法得出的聚类标签,-1代表样本点是噪声点,其余值表示样本点所属的类
labels = db.labels_

# 获取聚类数量
n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)

# 输出算法性能的信息
print('Estimated number of clusters: %d' % n_clusters_)#估计数量的集群
print("Homogeneity: %0.3f" % metrics.homogeneity_score(labels_true, labels))#同质性
print("Completeness: %0.3f" % metrics.completeness_score(labels_true, labels))#完整性
print("V-measure: %0.3f" % metrics.v_measure_score(labels_true, labels))#V-measure
print("Adjusted Rand Index: %0.3f"% metrics.adjusted_rand_score(labels_true, labels))#兰德调整指数
print("Adjusted Mutual Information: %0.3f"% metrics.adjusted_mutual_info_score(labels_true, labels))#调整后的相互信息
print("Silhouette Coefficient: %0.3f"% metrics.silhouette_score(X, labels))#侧影系数
#http://scikit-learn.org/stable/modules/classes.html#module-sklearn.metrics
##############################################################################
# 绘图
import matplotlib.pyplot as plt

# 黑色用作标记噪声点
unique_labels = set(labels)
colors = plt.cm.Spectral(np.linspace(0, 1, len(unique_labels)))

i = -1
# 标记样式,x点表示噪声点
marker = ['v','^','o','x']
for k, col in zip(unique_labels, colors):
    if k == -1:
        # 黑色表示标记噪声点.
        col = 'k'

    class_member_mask = (labels == k)

    i += 1
    if (i>=len(unique_labels)):
        i = 0

    # 绘制核心对象
    xy = X[class_member_mask & core_samples_mask]
    plt.plot(xy[:, 0], xy[:, 1], marker[i], markerfacecolor=col,
             markeredgecolor='k', markersize=14)
    # 绘制非核心对象
    xy = X[class_member_mask & ~core_samples_mask]
    plt.plot(xy[:, 0], xy[:, 1], marker[i], markerfacecolor=col,
             markeredgecolor='k', markersize=6)

plt.title('Estimated number of clusters: %d' % n_clusters_)
plt.show()


###EM算法
import numpy
import scipy.stats
#硬币投掷结果,用1表示H（正面），0表示T（反面）
observations = numpy.array([[1,0,0,0,1,1,0,1,0,1],
                        [1,1,1,1,0,1,1,1,0,1],
                        [1,0,1,1,1,1,1,0,1,1],
                        [1,0,1,0,0,0,1,1,0,0],
                        [0,1,1,1,0,1,1,1,0,1]])

def em_single(priors,observations):

    """
    EM算法的单次迭代
    Arguments
    ------------
    priors:[theta_A,theta_B]
    observation:[m X n matrix]

    Returns
    ---------------
    new_priors:[new_theta_A,new_theta_B]
    :param priors:
    :param observations:
    :return:
    """
    counts = {'A': {'H': 0, 'T': 0}, 'B': {'H': 0, 'T': 0}}
    theta_A = priors[0]
    theta_B = priors[1]
    #E step
    for observation in observations:
        len_observation = len(observation)
        num_heads = observation.sum()
        num_tails = len_observation-num_heads
        #二项分布求解公式
        contribution_A = scipy.stats.binom.pmf(num_heads,len_observation,theta_A)
        contribution_B = scipy.stats.binom.pmf(num_heads,len_observation,theta_B)
        #将两个概率正规化，得到数据来自硬币A，B的概率
        weight_A = contribution_A / (contribution_A + contribution_B)
        weight_B = contribution_B / (contribution_A + contribution_B)
        #更新在当前参数下A，B硬币产生的正反面次数
        counts['A']['H'] += weight_A * num_heads
        counts['A']['T'] += weight_A * num_tails
        counts['B']['H'] += weight_B * num_heads
        counts['B']['T'] += weight_B * num_tails

    # M step 当前模型参数下，AB分别产生正反面的次数估计出来了，计算新的模型参数
    new_theta_A = counts['A']['H'] / (counts['A']['H'] + counts['A']['T'])
    new_theta_B = counts['B']['H'] / (counts['B']['H'] + counts['B']['T'])
    return [new_theta_A,new_theta_B]

def em(observations,prior,tol = 1e-6,iterations=10000):
    """
    EM算法
    ：param observations :观测数据
    ：param prior：模型初值
    ：param tol：迭代结束阈值
    ：param iterations：最大迭代次数
    ：return：局部最优的模型参数
    """
    iteration = 0;
    while iteration < iterations:
        new_prior = em_single(prior,observations)
        delta_change = numpy.abs(prior[0]-new_prior[0])
        if delta_change < tol:
            break
        else:
            prior = new_prior
            iteration +=1
    return [new_prior,iteration]


print(em(observations,[0.6,0.5]))

# -*- coding: utf-8 -*-
"""
Created on Sat Oct 21 13:40:32 2017

@author: xuan
"""
###apriori

import pandas as pd


# 自定义连接函数，用于实现L_{k-1}到C_k的连接
def connect_string(x, ms):
    x = list(map(lambda i: sorted(i.split(ms)), x))
    l = len(x[0])
    r = []
    for i in range(len(x)):
        for j in range(i, len(x)):
            if x[i][:l - 1] == x[j][:l - 1] and x[i][l - 1] != x[j][l - 1]:
                r.append(x[i][:l - 1] + sorted([x[j][l - 1], x[i][l - 1]]))
    return r


# 寻找关联规则的函数
def find_rule(d, support, confidence, ms=u'--'):
    result = pd.DataFrame(index=['support', 'confidence'])  # 定义输出结果

    support_series = 1.0 * d.sum() / len(d)  # 支持度序列
    column = list(support_series[support_series > support].index)  # 初步根据支持度筛选
    k = 0

    while len(column) > 1:
        k = k + 1
        print(u'\n正在进行第%s次搜索...' % k)
        column = connect_string(column, ms)
        print(u'数目：%s...' % len(column))
        sf = lambda i: d[i].prod(axis=1, numeric_only=True)  # 新一批支持度的计算函数

        # 创建连接数据，这一步耗时、耗内存最严重。当数据集较大时，可以考虑并行运算优化。
        d_2 = pd.DataFrame(list(map(sf, column)), index=[ms.join(i) for i in column]).T

        support_series_2 = 1.0 * d_2[[ms.join(i) for i in column]].sum() / len(d)  # 计算连接后的支持度
        column = list(support_series_2[support_series_2 > support].index)  # 新一轮支持度筛选
        support_series = support_series.append(support_series_2)
        column2 = []

        for i in column:  # 遍历可能的推理，如{A,B,C}究竟是A+B-->C还是B+C-->A还是C+A-->B？
            i = i.split(ms)
            for j in range(len(i)):
                column2.append(i[:j] + i[j + 1:] + i[j:j + 1])

        cofidence_series = pd.Series(index=[ms.join(i) for i in column2])  # 定义置信度序列

        for i in column2:  # 计算置信度序列
            cofidence_series[ms.join(i)] = support_series[ms.join(sorted(i))] / support_series[ms.join(i[:len(i) - 1])]

        for i in cofidence_series[cofidence_series > confidence].index:  # 置信度筛选
            result[i] = 0.0
            result[i]['confidence'] = cofidence_series[i]
            result[i]['support'] = support_series[ms.join(sorted(i.split(ms)))]

    result = result.T.sort_values(['confidence', 'support'], ascending=False)  # 结果整理，输出
    print(u'\n结果为：')
    print(result)

    return result


# 使用Apriori算法挖掘菜品订单关联规则

import pandas as pd

inputfile = './data/menu_orders.xls'
outputfile = './data/apriori_rules.xls'  # 结果文件
data = pd.read_excel(inputfile, header=None)

print(u'\n转换原始数据至0-1矩阵...')
ct = lambda x: pd.Series(1, index=x[pd.notnull(x)])  # 转换0-1矩阵的过渡函数
b = map(ct, data.as_matrix())  # 用map方式执行
data = pd.DataFrame(list(b)).fillna(0)  # 实现矩阵转换，空值用0填充
print(u'\n转换完毕。')
del b  # 删除中间变量b，节省内存

support = 0.2  # 最小支持度
confidence = 0.5  # 最小置信度
ms = '---'  # 连接符，默认'--'，用来区分不同元素，如A--B。需要保证原始表格中不含有该字符

find_rule(data, support, confidence, ms).to_excel(outputfile)  # 保存结果
