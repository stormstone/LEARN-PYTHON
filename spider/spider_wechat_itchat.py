# coding=utf-8
# 用itchat包爬去自己微信好友的信息
__author__ = 'storm'
import itchat

itchat.login()
# 爬去自己好友相关信息，返回json文件
friends = itchat.get_friends(update=True)[0:]

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
print("男性好友; %.2f%%" % (float(male)/total*100) + "\n" +
"女性好友; %.2f%%" % (float(female)/total*100) + "\n" +
"不明性好友; %.2f%%" % (float(other)/total*100) + "\n" )

