#--coding:utf-8--
#code by myhaspl 
#词频分析
#12-7.py

from __future__ import unicode_literals
from __future__ import division


import nltk


import sys
sys.path.append("../")

import jieba


def cutstring(txt):
    #分词
    cutstr = jieba.cut(txt)
    result=" ".join(cutstr)
    return result
    
#读取文件
txtfileobject = open('nltest1.txt','r')

try:
   filestr = txtfileobject.read( )
finally:
   txtfileobject.close( )
 
cutstr=cutstring(filestr)
tokenstr=nltk.word_tokenize(cutstr)
#全文总词数
print u"词总数:",
print len(tokenstr)
#共出现多少词
print u"共出现词数:",
print len(set(tokenstr))
#词汇条目排序表
print u"词汇条目排序表"
for word in sorted(set(tokenstr)):
    print word,
print 
#每个词平均使用次数
print u"每个词平均使用次数:",
print len(tokenstr)/len(set(tokenstr))
#统计词频
fdist1=nltk.FreqDist(tokenstr)
for key,val in sorted(fdist1.iteritems()):
    print key,val,
print
print u".........计算机系统出现次数..............."
print fdist1[u'计算机系统']

#统计出现最多的前5个词
print
print u".........统计出现最多的前5个词..............."
fdist1=nltk.FreqDist(tokenstr)
for key,val in sorted(fdist1.iteritems(),key=lambda x:(x[1],x[0]),reverse=True)[:5]:
    print key,val