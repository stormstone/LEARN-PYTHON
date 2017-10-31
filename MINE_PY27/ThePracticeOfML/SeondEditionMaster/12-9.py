#--coding:utf-8--
#code by myhaspl 
#12-9.py
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

bigramcolloc=nltk.collocations.BigramCollocationFinder.from_words(tokenstr)
print "----出现最频繁的前10个词-----"
fdist1=bigramcolloc.word_fd
for key,val in sorted(fdist1.iteritems(),key=lambda x:(x[1],x[0]),reverse=True)[:10]:
    print key,":",val

print "----只出现1次的低频词-----"
fdist1=bigramcolloc.word_fd
for w  in fdist1.hapaxes():
    print w.encode("utf-8"),"|",  

#找出文本中搭配词
print
print "----找出双连搭配词-----"
bigramwords=nltk.bigrams(tokenstr)
for fw,sw in set(bigramwords):
    print fw," ",sw,"|",

print       
print "----双连搭配词以及词频-----"
for w,c  in sorted(bigramcolloc.ngram_fd.iteritems(),key=lambda x:(x[1],x[0]),reverse=True):
    fw,sw=w
    print fw," ",sw,"=>",c,"||",
print

trigramcolloc=nltk.collocations.TrigramCollocationFinder.from_words(tokenstr)    
print "----三连搭配词-----"
for fw,sw,tw  in trigramcolloc.ngram_fd:
    print fw.encode("utf-8")," ",sw.encode("utf-8")," ",tw.encode("utf-8"),"|", 
print