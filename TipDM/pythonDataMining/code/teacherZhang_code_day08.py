#=======神经网络======
from random import sample     #导入抽样函数
from sklearn.datasets import load_iris           #导入鸢尾花数据集
from sklearn.neural_network import MLPClassifier #导入神经网络包
iris = load_iris()   #读取数据
tr_index = sample(range(0,50),40)
tr_index.extend(sample(range(50,100),40))
tr_index.extend(sample(range(100,150),40))                 #训练集样本序号
te_index = [i for i in range(0,150) if i not in tr_index]  #测试集样本序号
tr_in = iris.data[tr_index,:]  #训练集输入
tr_out = iris.target[tr_index] #训练集目标输出
te_in = iris.data[te_index,:]  #测试集输入
net = MLPClassifier(hidden_layer_sizes=10,max_iter=1000).fit(tr_in,tr_out) #神经网络模型
res_net = net.predict(te_in)
print(res_net)                   #模型输出
print(iris.target[te_index])     #实际值
print(sum(res_net==iris.target[te_index])/len(res_net)) #准确率

#=======K-Means，调用sklearn库======
from pandas import DataFrame
from sklearn.cluster import KMeans
from sklearn import datasets
iris = datasets.load_iris()
x = iris.data
y = iris.target
print(x,y)

kModel = KMeans(n_clusters=3)
kModel.fit(x) # 训练模型
print(kModel.cluster_centers_) # 查看聚类中心
a = {
    'True':[i for i in y],
    'Pred':[j for j in kModel.labels_]
}
dat = DataFrame(a)
print(dat) # 查看聚类结果和实际分类的区别

#=======K-Medoids======
from pandas import DataFrame,Series #导入所需要的两个函数
n = 50    #待聚类样本个数
x = Series(range(1,n+1))      #样本的x坐标值
y = Series(range(n,n+n))      #样本的y坐标值
center0 = Series([x[0],y[0]]) #初始第一个类中心
center1 = Series([x[1],y[1]]) #初始第二个类中心
dis = DataFrame(index=range(0,n),columns=['dis_cen0','dis_cen1','class']) #初始数据框
#=自定义求最小值位置的函数=
def which_min(x):
    if x[0] <= x[1]:
        z=0
    else:
        z=1
    return z
#=主循环开始=
while True:
    for i in range(0,n):       #求各样本至各类中心的距离
        dis.ix[i,0] = ((x[i]-center0[0])**2+(y[i]-center0[1])**2)**0.5
        dis.ix[i,1] = ((x[i]-center1[0])**2+(y[i]-center1[1])**2)**0.5
        dis.ix[i,2] = which_min(dis.ix[i,0:2]) #样本归类
    index0 = dis.ix[:,2] == 0  #第一类样本序号
    index1 = dis.ix[:,2] == 1  #第二类样本序号
    #====求新类中心===
    

    #====判定类中心是否发生变化,若否则中止while循环====
    if sum(center0==center0_new)+sum(center1==center1_new)==4:
        break
    #====更新类中心
    center0 = center0_new
    center1 = center1_new
print(dis) #输出结果


#=======层次聚类(系谱聚类 Hierarchical Clustering, HC)======
from pandas import DataFrame
from sklearn.cluster import AgglomerativeClustering
from sklearn import datasets
iris = datasets.load_iris()
x = iris.data
y = iris.target
y_pred = AgglomerativeClustering(affinity='euclidean',linkage='ward',n_clusters=3).fit_predict(x)
print(y_pred)
a = {
    'True':[i for i in y],
    'Pred':[j for j in y_pred]
}
dat = DataFrame(a)
print(dat) # 查看聚类结果和实际分类的区别


#=======DBSCAN（密度聚类）======
from sklearn import datasets
from sklearn.cluster import dbscan
iris = datasets.load_iris()
x = iris.data
y = iris.target
Dmodle=dbscan(x,eps=0.4999,min_samples=2)
print(Dmodle[1])

#=======EM======

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

#=====关联规则=====
import os
print(os.getcwd())
from apyori import apriori
#Put apyori.py into your project. or Run python setup.py install.
transactions = [
    ['a','c','e'],
    ['b','d'],
    ['b','c'],
    ['a','b','c','d'],
    ['a','b'],
    ['b','c'],
    ['a','b'],
    ['a','b','c','e'],
    ['a','b','c'],
    ['a','c','c'],
]
res = apriori(transactions,min_support=0.3,max_length=3)
results = list(res)
print(results[:2])






