#encoding=utf-8
#--coding:utf-8--
#code by myhaspl 
#分词，词性
#12-6.py
from __future__ import unicode_literals

import nltk
import sys
sys.path.append("../")

import jieba
from jieba import posseg

def cutstrpos(txt):
    #分词+词性
    cutstr = posseg.cut(txt)
    result=""
    for word, flag in cutstr:
        result+=word+"/"+flag+' '
    return result

def cutstring(txt):
    #分词
    cutstr = jieba.cut(txt)
    result=" ".join(cutstr)
    return result
    
#读取文件
txtfileobject = open('nltest1.txt')
textstr=""
try:
   filestr = txtfileobject.read( )
finally:
   txtfileobject.close( )


#中文分词并标注词性
posstr=cutstrpos(filestr)
strtag=[nltk.tag.str2tuple(word) for word in posstr.split()]
for word,tag in strtag:
    print word,"/",tag,"|",
    
#进入语料库   
cutstr=cutstring(filestr)
mytext=nltk.text.Text(cutstr)
#在该语料库中查找包括“人”的语句
print(mytext.concordance(u"人"))


