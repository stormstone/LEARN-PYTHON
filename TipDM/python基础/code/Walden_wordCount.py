'''
统计Walden的词频
'''
import re
import time

time0 = time.clock()  # 开始时间
path = 'D:\Python\TipDM\Walden.txt'
file = open(path, 'r')
text = file.read()  # 读取文件，读成一个长字符串
words = text.split()  # 将字符串打断成单词
words1 = [word.lower() for word in words]  # 将大写字母转换成小写的
words2 = [re.sub("[,'.:;]", '', word) for word in words1]  # 去掉标点符号
print('文本单词总数为：' + str(len(words2)))
words_index = set(words2)  # 去重复
print('不同单词个数为：' + str(len(words_index)))
dic = {index: words2.count(index) for index in words_index}  # 统计词频
res = sorted(dic.items(), key=lambda asd: asd[1], reverse=True)  # 排序 asd[1]表示按照value单词个数
print(res)

path2 = 'D:\Python\TipDM\WaldenWordCount.txt'
filewordcount = open(path2, 'w')
filewordcount.write(str(res))
filewordcount.close()

print('运行时间（s）：' + str((time.clock() - time0)))
