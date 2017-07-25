# coding=utf-8
# 用itchat包爬去自己微信好友的信息
# 乱码问题未解决
__author__ = 'storm'
import itchat

# 解决Python2.7的UnicodeEncodeError: ‘ascii’ codec can’t encode异常错误
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

itchat.login()
# 爬去自己好友相关信息，返回json文件
friends = itchat.get_friends(update=True)[0:]

# 1.统计男女人数比例
# 初始化计算器
male = female = other = 0
# friends[0]是自己的信息，所以要从friends[1]开始
for i in friends[1:]:
    sex = i["Sex"]
    if sex == 1:
        male += 1
    elif sex == 2:
        female += 1
    else:
        other += 1
# 计算朋友总数
total = len(friends[1:])
# 打印出自己的好友性别比例
print("男性好友; %.2f%%" % (float(male) / total * 100) + "\n" +
      "女性好友; %.2f%%" % (float(female) / total * 100) + "\n" +
      "不明性好友; %.2f%%" % (float(other) / total * 100) + "\n")


# 2.自己微信好友城市分布
# 定义一个函数，用来爬去各个变量
def get_var(var):
    variable = []
    for i in friends:
        value = i[var]
        variable.append(value)
    return variable


# 调用函数得到各变量，并把数据存到CSV文件中
NickName = get_var("NickName")
Sex = get_var("Sex")
Province = get_var("Province")
City = get_var("City")
Signature = get_var("Signature")
from pandas import DataFrame

data = {'NickName': NickName, 'Sex': Sex, 'Province': Province, 'City': City, 'Signature': Signature}
frame = DataFrame(data)
frame.to_csv('wechatdata.csv', index=True)

# 3.自己微信好友个性签名的自定义词云图
import re

siglist = []
for i in friends:
    signature = i["Signature"].strip().replace("span", "").replace("class", "").replace("emoji", "")
    rep = re.compile("1f\d+\w*|[<>/=]")
    signature = rep.sub("", signature)
    siglist.append(signature)
text = "".join(siglist)
# jieba分词
import jieba

wordlist = jieba.cut(text, cut_all=True)
word_space_split = " ".join(wordlist)

# 画图
import matplotlib.pyplot as plt
from wordcloud import WordCloud, ImageColorGenerator
import numpy as np
import PIL.Image as Image
import os

coloring = np.array(Image.open("" + os.getcwd() + "/storm2.png"))
my_wordcloud = WordCloud(background_color="white", max_words=2000, mask=coloring,
                         max_font_size=60, random_state=42, scale=2).generate(word_space_split)

image_colors = ImageColorGenerator(coloring)
plt.imshow(my_wordcloud.recolor(color_func=image_colors))
plt.imshow(my_wordcloud)
plt.axis("off")
plt.show()
