#--coding:utf-8--
#code by myhaspl 
#12-16.py
from __future__ import unicode_literals
from __future__ import division
import pylab 
import nltk
import urllib
from bs4 import BeautifulSoup
import random



import sys
sys.path.append("../")
pylab.mpl.rcParams['font.sans-serif']=['SimHei']
import jieba


def cutstring(txt):
    #分词
    cutstr = jieba.cut(txt)
    result=" ".join(cutstr)
    return result

def txtfeatures(allwords,tokenw,stopseg):
    features={}
    for myword in set(allwords):
        if not(myword.strip() in stopseg) and len(myword.strip())>1:
           features["cnword-"+myword]=(myword in set(tokenw))
           print "=",    
    return features


#停用词字典
f_stop = open('stopwords.txt')  
try:  
    f_stop_text = f_stop.read( )
    f_stop_text=unicode(f_stop_text,'utf-8')
finally:  
    f_stop.close( ) 
f_stop_seg_list=f_stop_text.split('\n')



urls=[(u"科技","http://tech.163.com/16/0203/06/BESLRF5O000915BD.html"),(u"科技","http://tech.163.com/16/0202/01/BEPHEI1200094O5H.html"),(u"科技","http://tech.163.com/16/0203/03/BESBB73B000915BD.html"),(u"科技","http://tech.163.com/16/0203/03/BESAGOPB000915BD.html"),(u"教育","http://edu.163.com/16/0203/05/BESI2S7500294NE9.html"),(u"教育","http://kids.163.com/16/0118/06/BDJEMJ3H00294MO6.html"),(u"教育","http://edu.163.com/16/0128/05/BED4NHBB00294NE9.html"),(u"教育","http://edu.163.com/16/0202/01/BEPHFQ1800294IIH.html")]
samplewords=[]
allw=[]
tokendocstr=[]
print "|=",
for (category,myurl) in urls: 
    htmlsrc=urllib.urlopen(myurl).read()
    htmlsrc=htmlsrc.decode('gbk')
    soup = BeautifulSoup(htmlsrc, 'html.parser')
    txtsrc=soup.find_all(id="endText" )
    txtsoup=BeautifulSoup(repr(txtsrc[0]))
    txtstr=txtsoup.get_text()
    txtstr=txtstr.decode('gbk').decode("unicode-escape").encode('utf-8')
    cutstr=cutstring(txtstr)
    tokendocstr.append(nltk.word_tokenize(cutstr))
 
for docstr in tokendocstr:
    for w in docstr:
        allw.append(w)
allw=set(allw)

samplefeatures=[]   
i=0   
for docstr in tokendocstr:
    docfeature=txtfeatures(allw,docstr,f_stop_seg_list)
    samplefeatures.append((docfeature,urls[i][0]))
    i=i+1

    
samplelen=len(samplefeatures)
trlen=int(samplelen*2/3)#训练样本长度
random.shuffle(samplefeatures)

traintxt=samplefeatures[:trlen]
testtxt=samplefeatures[trlen:]
print "=>|"

classifier=nltk.NaiveBayesClassifier.train(traintxt)
#测试数据分类准确率
print nltk.classify.accuracy(classifier,testtxt)
classifier.show_most_informative_features(15) 