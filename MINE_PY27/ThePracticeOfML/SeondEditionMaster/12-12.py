#--coding:utf-8--
#code by myhaspl 
#12-12.py
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
    

samples=[('nltest1.txt',u'科技'),('nltest2.txt',u'科技'),('nltest3.txt',u'财经'),('nltest4.txt',u'财经')]
samplewords=[]
for (filename,categories) in samples:
    #读取文件
    txtfileobject = open(filename,'r')    
    try:
       filestr = txtfileobject.read( )
    finally:
       txtfileobject.close( )
    
    cutstr=cutstring(filestr)
    tokenstr=nltk.word_tokenize(cutstr)

    mywords=[w for w in tokenstr]
    for word in mywords:
        samplewords.append((categories,word))
#条件频率，每个词条在不同分类中出现的频率
print "------------------"
cfd=nltk.ConditionalFreqDist(samplewords)   
fdist=cfd[u'财经']
for word in fdist:
    print word
print "---------流动性出现次数-----------"
print cfd[u'财经'][u'流动性']
print "----------条件:分类----------"
for cnd in cfd.conditions():
    print cnd
print "---------------------------"
#频数最大的样本
print cfd[u'财经'].max()
#条件频率分布
print "----------条件频率分布表----------"
cfd.tabulate(title=u'条件频率分布表',conditions=[u'科技',u'财经'])
cfd.plot(title=u'条件频率分布图',conditions=[u'科技',u'财经'])




