#--coding:utf-8--
#code by myhaspl
#12-11.py
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

#以词频递减顺序访问所有以“神”开头的词
print "以词频递减顺序访问所有以“神”开头的词"
mywords=[w for w in fdist.keys() if w.startswith(u"神")]
for word in mywords:
    print word,"||",

#以词频递减顺序访问所有以“学”结尾的词
print
print "以词频递减顺序访问所有以“学”结尾的词"
mywords=[w for w in fdist.keys() if w.endswith(u"学")]
for word in mywords:
    print word,"||",


#以词频递减顺序访问所有包含“美国”的搭配词
print
print "以词频递减顺序访问所有包含“美国”的搭配词"
bigramwords=nltk.bigrams(tokenstr)
mywords=[w for w in set(bigramwords) if u"美国" in w]
for fw,sw in mywords:
    print fw," ",sw,"|",
