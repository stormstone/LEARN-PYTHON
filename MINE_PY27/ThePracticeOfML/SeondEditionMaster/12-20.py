#--coding:utf-8--
#code by myhaspl 
#12-20.py
from __future__ import unicode_literals
from __future__ import division
import pylab 
import nltk
import urllib

import numpy 
import re
import sys

import jieba.analyse

sys.path.append("../")
pylab.mpl.rcParams['font.sans-serif']=['SimHei']

from jieba import posseg


def cutstrpos(txt):
    #分词+词性
    cutstr = posseg.cut(txt)
    result=""
    for word, flag in cutstr:
        result+=word+"/"+flag+' '
    return result

def inittxtw(allwords):
    txtwords={}
    for w in allwords:
        txtwords[w]=0
    return txtwords
    
    
def txtfeatures(allwdt,tokenw):
    #统计词频数
    txtfd=nltk.FreqDist(tokenw)  
    for key,val in sorted(txtfd.iteritems()):
        allwdt[key]=val
    return allwdt.values()

    

    
#根据电影评论将电影聚类
urls=[(u"功夫熊猫3","http://ent.163.com/16/0129/00/BEF5L97P00034R77.html"),(u"唐人街探案","http://ent.163.com/15/1230/15/BC3GSVQ700034R77.html"),(u"恶棍天使","http://ent.163.com/15/1224/07/BBJ60V1H00034R77.html"),(u"老炮儿","http://ent.163.com/15/1224/00/BBIED1QL00034R77.html"),(u"寻龙诀","http://ent.163.com/15/1218/03/BB3A3I2B00034R77.html"),(u"万万没想到","http://ent.163.com/15/1218/03/BB3ACSP700034R77.html"),(u"星球大战7","http://ent.163.com/15/1217/15/BB21INTG00034R77.html"),(u"饥饿游戏3（下）","http://ent.163.com/15/1120/07/B8RKKR9C00034R77.html"),(u"九层妖塔","http://ent.163.com/15/0930/01/B4NN919N00034R77.html"),(u"超能查派","http://ent.163.com/15/0508/06/AP2T6CP400034R77.html"),(u"我是路人甲","http://ent.163.com/15/0702/17/ATHL56DT00034R77.html"),(u"港囧","http://ent.163.com/15/0925/05/B4BA6IJ600034R77.html"),(u"007：幽灵党","http://ent.163.com/15/1113/08/B89PJSGE00034R77.html"),(u"小黄人大眼萌","http://ent.163.com/15/0913/07/B3CI689C00034R77.html")]

allw=[]
tokendocstr=[]
i=0
errorfilm=[]
for (film,myurl) in urls: 
    print "\n***************《"+film+"》关键词**********************" 
    htmlsrc=urllib.urlopen(myurl).read()
    htmlsrc=htmlsrc.decode('gbk')
    pattern=re.compile(r'((class="end-text">)|(<br  /></p><p>))(.*<style>.*--></p>)*(.+?)(</p></div>|<div id=)')    
    match = pattern.findall(repr(htmlsrc))
    matchstr=""
    if match:
        mstr=match[0][4].encode('utf-8').decode("unicode-escape")
        matchstr+=mstr
    else:
        print film,"无法取得评论!"
        errorfilm.append(i)
    i+=1
    txtstr=matchstr.replace("</p>","").replace("<p>","").replace("<span>","").replace("</span>","").replace(r'<b style="mso-bidi-font-weight: normal">','').replace(r'</b>','')

    

    #提取前30位TF/IDF权重最大的关键词
    topK = 30
    tags = jieba.analyse.extract_tags(txtstr, topK=topK)
    cutstr="  ".join(tags)
    print cutstr
    tokendocstr.append(nltk.word_tokenize(cutstr))



for docstr in tokendocstr:
    for w in docstr:
        allw.append(w)
allw=set(allw)



samplefeatures=[]   
  
for docstr in tokendocstr:
    allwdt=inittxtw(allw)
    docfeature=numpy.array(txtfeatures(allwdt,docstr))
    samplefeatures.append(docfeature)



#GAAC聚类
print u"----------------GAAC聚类------------"
txtclassfier=nltk.cluster.gaac.GAAClusterer(num_clusters=5,normalise=True)

txtclassfier.cluster(vectors=samplefeatures)
i=0
for data in samplefeatures:
    print urls[i][0],"聚类编号:"
    print txtclassfier.classify(data)
    i+=1
#kmeans聚类
print u"-------------kmeans聚类--------------"
txtclassfier=nltk.cluster.kmeans.KMeansClusterer(num_means=5,distance=nltk.cluster.util.euclidean_distance)
txtclassfier.cluster(samplefeatures)
i=0
for data in samplefeatures:
    print urls[i][0],"聚类编号:"
    print txtclassfier.classify(data)
    i+=1
