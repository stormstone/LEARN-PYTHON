#--coding:utf-8--
#code by myhaspl 
#12-15.py
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


#停用词字典
f_stop = open('stopwords.txt')  
try:  
    f_stop_text = f_stop.read( )
    f_stop_text=unicode(f_stop_text,'utf-8')
finally:  
    f_stop.close( ) 
f_stop_seg_list=f_stop_text.split('\n')

def cutstring(txt):
    #分词
    cutstr = jieba.cut(txt)
    result=" ".join(cutstr)
    return result

def wordfeatures(word):
    return {"cnword":word,"wcnlen":len(word) }


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
    for myword in tokenstr:
        if not(myword.strip() in f_stop_seg_list) and len(myword.strip())>1:
            samplewords.append((myword,category))
            print "=",

#通过apply_features方法，返回链表，不在内存中存储所有特征集，节约内存
samplelen=len(samplewords)
trlen=int(samplelen*2/3)#训练样本长度
random.shuffle(samplewords)
traintxt=nltk.classify.apply_features(wordfeatures,samplewords[:trlen])
testtxt=nltk.classify.apply_features(wordfeatures,samplewords[trlen:])
print "=>|"

classifier=nltk.NaiveBayesClassifier.train(traintxt)
#大学所属的类别
print u"----大学所属的类别-----"
print classifier.classify({"cnword":u"大学","wcnlen":len(u"大学")})
#大脑所属的类别
print u"----大脑所属的类别-----"
print classifier.classify({"cnword":u"大脑","wcnlen":len(u"大脑")})
#测试数据分类准确率
print nltk.classify.accuracy(classifier,testtxt)

#特征分类最有效的10个特征
for wf,mostword in classifier.most_informative_features(10):
    print mostword,
print


#为显示utf-8，将show_most_informative_features代码进行修改
#classifier.show_most_informative_features(10)  #也可直接调用这句，但是UTF8显示有问题   
cpdist = classifier._feature_probdist
print('Most Informative Features')

for (fname, fval) in classifier.most_informative_features(10):
    def labelprob(l):
        return cpdist[l, fname].prob(fval)

    labels = sorted([l for l in classifier._labels
                     if fval in cpdist[l, fname].samples()],
                    key=labelprob)
    if len(labels) == 1:
        continue
    l0 = labels[0]
    l1 = labels[-1]
    if cpdist[l0, fname].prob(fval) == 0:
        ratio = 'INF'
    else:
        ratio = '%8.1f' % (cpdist[l1, fname].prob(fval) /
                           cpdist[l0, fname].prob(fval))
    print fname,
    print "=",
    print fval, 
    print(('%6s : %-6s = %s : 1.0' % (("%s" % l1)[:6], ("%s" % l0)[:6], ratio)))    