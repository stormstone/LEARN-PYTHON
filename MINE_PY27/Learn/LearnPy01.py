__author__ = 'storm'

# Python基础，包括 List Tuple Dict Set等类型，条件判断和循环，函数dif，切片，迭代，列表生成式


print("hello world")
print(u'中文\n日文\n韩文')

print(u'''Python的Unicode字符串支持"中文",
"日文",
"韩文"等多种语言''')
print('\n')

# 列表[]
L = ['Michael', 'Bob', 'Tracy']
L.append('storm')  # 添加元素到末尾
print(L)
L.insert(2, 'Paul')  # 插入元素到指定位置
print(L)
L.pop(1)  # 删除指定位置元素
print(L)

# 不可更改的tuple()
t = (0, -9, 10)
print(t)
t = (1,)  # 加一个,确保创建了一个tuple
print(t)
t = (1, 2, 'a', 'b', ['A', 'B'])
print(t)
print(t[4])
print('\n')

age = 10
if age >= 30:
    print('your age is', age)
    print('old')
elif age >= 18:
    print('adult')
else:
    print('young')
print('END')
print('\n')

L = [75, 92, 59, 68]
sum = 0.0
for score in L:
    sum += score
print(sum / 4)

sum = 0
x = 1
while x <= 100:
    sum += x
    x = x + 2
print(sum)

sum = 0
x = 1
n = 1
while True:
    sum += pow(2, x - 1)
    x = x + 1
    n = n + 1
    # print(sum)
    if n > 20:
        break;
print(sum, '\n')

import math


def quadratic_equation(a, b, c):
    x1 = (-b + math.sqrt(b * b - 4 * a * c)) / (2 * a)
    x2 = (-b - math.sqrt(b * b - 4 * a * c)) / (2 * a)
    return x1, x2


print(quadratic_equation(2, 3, 0))
print(quadratic_equation(1, -6, 5))
print('\n')


def move(n, a, b, c):
    if n == 1:
        print(a, '-->', c)
        return
    move(n - 1, a, c, b)
    print(a, '-->', c)
    move(n - 1, b, a, c)


move(3, 'A', 'B', 'C')
print("\n")


def average(*args):
    sum = 0.0
    if len(args) == 0:
        return sum
    for x in args:
        sum = sum + x
    return sum / len(args)


print(average())
print(average(1, 2))
print(average(1, 2, 2, 3, 4))
print("\n")

L = ['Adam', 'Lisa', 'Bart', 'Paul']
for index, name in zip(range(1, len(L) + 1), L):  # zip(L1,L2)将两个list合并成键值对形式， range(1,y)生成递增序列
    print(index, '-', name)
print("\n")

d = {'Adam': 95, 'Lisa': 85, 'Bart': 59, 'Paul': 74}
sum = 0.0
for k, v in d.items():
    sum = sum + v
    print(k, ':', v)
print('average', ':', sum / len(d))
print('\n')

# 生成列表
print([x * (x + 1) for x in range(1, 100, 2)])
print('\n')

d = {'Adam': 95, 'Lisa': 85, 'Bart': 59}


def generate_tr(name, score):
    if score < 60:
        return '<tr><td>%s</td><td style="color:red">%s</td></tr>' % (name, score)
    return '<tr><td>%s</td><td>%s</td></tr>' % (name, score)


tds = [generate_tr(name, score) for name, score in d.items()]
print('<table border="1">')
print('<tr><th>Name</th><th>Score</th><tr>')
print('\n'.join(tds))
print('</table>')
print('\n')

# 利用 3 层for循环的列表生成式，找出对称的 3 位数。例如，121 就是对称数，因为从右到左倒过来还是 121。
print([100 * n1 + 10 * n2 + n3 for n1 in range(1, 10) for n2 in range(10) for n3 in range(10) if n1 == n3])
