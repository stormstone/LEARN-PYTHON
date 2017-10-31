#--coding:utf-8--
#code by myhaspl 
#12-8.py
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
txtfileobject = open('nltest2.txt','r')

try:
   filestr = txtfileobject.read( )
finally:
   txtfileobject.close( )
 
cutstr=cutstring(filestr)
tokenstr=nltk.word_tokenize(cutstr)

fdist1=nltk.FreqDist(tokenstr)
#只出现了一次的低频词 
print "----只出现了一次的低频词-----"
for word in fdist1.hapaxes():
    print word,
#找出文本中的长词 
print
print "----文本中的长词-----"
for word in [w for w in set(tokenstr) if len(w)>3]:
    print word,
#找出文本中出现2次以上的长词 
print
print "----文本中出现2次以上的长词-----"
for word in [w for w in set(tokenstr) if len(w)>3 and fdist1[w]>2]:
        print word,