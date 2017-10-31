#--coding:utf-8--
#code by myhaspl 
#12-13.py
from __future__ import unicode_literals
from __future__ import division
import pylab 
import nltk
import urllib
from bs4 import BeautifulSoup

import sys
sys.path.append("../")
pylab.mpl.rcParams['font.sans-serif']=['SimHei']
import jieba


def cutstring(txt):
    #分词
    cutstr = jieba.cut(txt)
    result=" ".join(cutstr)
    return result
 

urls=[(u"科技","http://tech.163.com/16/0203/06/BESLRF5O000915BD.html"),(u"科技","http://tech.163.com/16/0202/01/BEPHEI1200094O5H.html"),(u"科技","http://tech.163.com/16/0203/03/BESBB73B000915BD.html"),(u"科技","http://tech.163.com/16/0203/03/BESAGOPB000915BD.html"),(u"教育","http://edu.163.com/16/0203/05/BESI2S7500294NE9.html"),(u"教育","http://kids.163.com/16/0118/06/BDJEMJ3H00294MO6.html"),(u"教育","http://edu.163.com/16/0128/05/BED4NHBB00294NE9.html"),(u"教育","http://edu.163.com/16/0202/01/BEPHFQ1800294IIH.html")]
samplewords=[]
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
    tokenstr=nltk.word_tokenize(cutstr)
    for word in tokenstr:
        samplewords.append((category,word))
    print "=",

print "=>|"
cfdist=nltk.ConditionalFreqDist(samplewords)   
#知识一词的频率
print cfdist[u'科技'].freq(u'知识')

samplews=[]
#在教育分类中出现最多的20个词
fd=cfdist[u'教育']
edufd20=sorted(fd.iteritems(),key=lambda x:(x[1],x[0]),reverse=True)[:20]
for w,c in edufd20:
    print w,"=>",c,"||",
    samplews.append(w)    
print
#在科技分类中出现最多的20个词
fd=cfdist[u'科技']
techfd20=sorted(fd.iteritems(),key=lambda x:(x[1],x[0]),reverse=True)[:20]
for w,c in techfd20:
    print w,"=>",c,"||",
    samplews.append(w)    
print 
samplews=set(samplews)
#条件频率分布图
cfdist.tabulate(title=u'条件频率分布表',samples=samplews,conditions=[u'科技',u'教育'])  
cfdist.plot(title=u'条件频率分布图',samples=samplews,conditions=[u'科技',u'教育'])  
