#! -*- coding:utf-8 -*-
__author__ = 'storm'
'''
python集训营-python基础-day2:2017-10-10
'''

Dic = {'key1': 'A', 'key2': 123, 'key3': True, 123: 'C'}
print(Dic)
print(Dic['key1'] + Dic[123])
Dic['key1'] = False
print(Dic)
Dic['key4'] = 0
print(Dic)
Dic.update({'1': 'F', 2: 3})
print(Dic)
print('---------------------------------')

for i in range(11):
    print(i, end='')
i = 1
while i < 10:
    print(i, end='-')
    i += 1

a = []
for i in range(1, 11):
    a.append(i)
    print(a)
print('---------------------------------')

# range生成列表应用
a = [i for i in range(1, 11)]
print(a)
b = [i ** 2 for i in range(1, 11)]
print(b)
c = [i for i in range(1, 101) if i % 2 == 1]
print(c)
dic = {i: i ** 2 for i in range(1, 11)}
print(dic)
print('---------------------------------')

# 九九乘法表
for i in range(1, 10):
    for j in range(1, i + 1):
        print("%d * %d = %d" % (i, j, i * j), end='\t')
    print()
print('---------------------------------')

# 计算运行时间
import time

time0 = time.clock()
a = []
for i in range(1, 20000):
    a.append(i)
time.clock() - time0
print('---------------------------------')

# 求sin(x)在0-2pi与x轴围成的面积，极限法
import math

n = 1000000  # 分成n份
width = 2 * math.pi / n  # 每一小部分的宽度
x = [i * width for i in range(0, n)]  # x的值列表
y = [abs(math.sin(i)) for i in x]  # y的值的绝对值列表
area = sum(y) * width  # 面积等于每一小部分面积的和
print(area)
print('---------------------------------')


# 函数
def count(x):
    z = 0
    for i in x:
        if i % 2 == 1:
            z += 1
    return z


nu = [1, 2, 3, 4]
print(count(nu))

# lambda函数
y = lambda x: x + 1
y(1.3)
y = lambda x: x ** 3
y(2)
print('---------------------------------')

# 文件
f = open('helloworld.txt', 'w')
f.write('hello word \n jdslfjls')
f.close

f = open('helloworld.txt', 'r')
te = f.read()  # 读完游标已经到最后
line = f.readlines()  # 再读已经是文档最后了，读不到内容了
f.close
print(te)
print(line)
print('---------------------------------')
