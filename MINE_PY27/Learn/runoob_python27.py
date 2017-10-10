#!/usr/bin/python
# coding=utf-8
print "你好世界";
print 1 <> 2;
a = 1;
b = 1;
print a is b;
print id(a);
print id(b);
b = 2;
print a is b;
print id(a);
print id(b);
print '-----------------';

fruits = ['banana', 'apple', 'mango']
print range(len(fruits));
for index in range(len(fruits)):
    print '当前水果：', fruits[index]
print 'good bye!'
print '-----------------';

for num in range(10, 20):
    for i in range(2, num):
        if num % i == 0:
            j = num / i
            print '%d 等于 %d * %d' % (num, i, j)
            break
    else:
        print num, '是一个质素'
