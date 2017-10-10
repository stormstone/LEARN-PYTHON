# 菜鸟教程 python2.7 学习记录
# coding=utf-8
print "你好世界"
print 1 <> 2  # 已经弃用
a = 1
b = 1
print a is b  # TRUE
# id(变量)得到引用
print id(a)
print id(b)
b = 2
print a is b  # FALSE
print id(a)
print id(b)
print '-----------------'

fruits = ['banana', 'apple', 'mango']
print range(len(fruits))  # range()
for index in range(len(fruits)):
    print '当前水果：', fruits[index]
print 'good bye!'
print '-----------------'

# 循环
for num in range(10, 20):  # 迭代 10 到 20 之间的数字
    for i in range(2, num):  # 根据因子迭代
        if num % i == 0:  # 确定第一个因子
            j = num / i  # 计算第二个因子
            print '%d 等于 %d * %d' % (num, i, j)
            break  # 跳出当前循环
    else:  # 循环的 else 部分
        print num, '是一个质数'
print '-----------------'

# 循环嵌套
i = 2
while i < 100:
    j = 2
    while j <= (i / j):
        if not (i % j):
            break
        j = j + 1
    if j > i / j:
        print i, '是素数'
    i = i + 1
print '-----------------'

'''
pass是空语句，是为了保持程序结构的完整性。
pass 不做任何事情，一般用做占位语句。
'''
for letter in 'Python':
    if letter == 'h':
        pass
        print '这是 pass 块'
    print '当前字母 :', letter
print '-----------------'

'''
Python Number 数据类型用于存储数值。
数据类型是不允许改变的,这就意味着如果改变 Number 数据类型的值，将重新分配内存空间。
可以使用del语句删除一些 Number 对象引用。
'''

