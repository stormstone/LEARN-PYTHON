#--coding:utf-8--
#code by myhaspl 
#12-10.py
from __future__ import unicode_literals
from __future__ import division
import pylab 


import nltk


import sys
sys.path.append("../")
pylab.mpl.rcParams['font.sans-serif']=['SimHei']
import jieba


def cutstring(txt):
    #分词
    cutstr = jieba.cut(txt)
    result=" ".join(cutstr)
    return result
    
#读取文件
txtfileobject = open('nltest2.txt','r')

try:
   filestr = txtfileobject.read( )
finally:
   txtfileobject.close( )

cutstr=cutstring(filestr)
tokenstr=nltk.word_tokenize(cutstr)

fdist=nltk.FreqDist(tokenstr)

#以词长为元素，计算不同词长的频率    
print "----词频-----"
fdist1=nltk.FreqDist([len(w) for w in tokenstr])
for w,c  in fdist1.items():
    print w,"=>",c,"||",
#词长
print
print "----词长-----"
print fdist1.keys()

#词
print 
print u"---词频---"
fdist2=nltk.FreqDist(tokenstr)
for w,c  in fdist2.items():
    print w,"=>",c,"||",



print
print  u"---无意识出现的次数---"
print fdist2[u"无意识"]
print  u"---神经学家出现的次数---"
print fdist2[u"神经学家"]


#其它基本指标
sample=cutstring(u"据悉，这辆汽车绰号野兽，野兽很可能于2017年1月份美国第45任总统就职时使用。目前，野兽的详细规格都属于绝密信息，但谍照显示野兽采用了凯迪拉克的最新护栅和前灯设计。")
tokenstr=nltk.word_tokenize(sample)
fdist3=nltk.FreqDist(tokenstr)
print u"---美国出现的次数---"
print fdist3[u"美国"]
print u"---样本总数---"
print fdist3.N()
print u"---数值最大的样本---"
print fdist3.max()
#频率分布表
fdist3.tabulate()
#频率分布图
fdist3.plot()
#前10个高频词的累积频率分布图
fdist3.plot(10,cumulative=True)