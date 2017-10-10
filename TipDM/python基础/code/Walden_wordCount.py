import re
import time

time0 = time.clock()  # 开始时间
path = 'D:\Python\TipDM\Walden.txt'
file = open(path, 'r')
text = file.read()  # 读取文件，读成一个长字符串
words = text.split()  # 将字符串打断成单词
words1 = [word.lower() for word in words]  # 将大写字母转换成小写的
words2 = [re.sub("[,'.:;]", '', word) for word in words1]  # 去掉标点符号
words_index = set(words)  # 去重复
dic = {index: words2.count(index) for index in words_index}  # 统计词频
sorted(dic.items(), key=lambda asd: asd[1], reverse=True)  # 排序

print(dic)
print(time.clock() - time0)
