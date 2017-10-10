__author__ = 'storm'

# 函数式编程，模块，面向对象，继承，定制类

# 在Python 3里，reduce()函数已经被从全局名字空间里移除了，它现在被放置在fucntools模块里用的话要 先引入
from functools import reduce


# 内置高阶函数（可以传入函数当参数）
# map()函数
def f(x):
    return x * x


print(map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9]))


def format_name(s):
    return s[0].upper() + s[1:].lower()


print(map(format_name, ['adam', 'LISA', 'barT']))


# reduce()函数
def prod(x, y):
    return x * y


print(reduce(prod, [2, 4, 5, 7, 12]))
# filter()函数
import math


def is_sqr(x):
    r = int(math.sqrt(x))
    return r * r == x


print(filter(is_sqr, range(1, 101)))


# 请编写一个函数calc_prod(lst)，它接收一个list，返回一个函数，返回函数可以计算参数的乘积。
def calc_prod(lst):
    def cj():
        def f(x, y):
            return x * y

        return reduce(f, lst, 1)

    return cj


f = calc_prod([1, 2, 3, 4])
print(f())


# 希望一次返回3个函数，分别计算1x1,2x2,3x3:
def count():
    fs = []
    for i in range(1, 4):
        def f(j):
            def g():
                return j * j

            return g

        r = f(i)
        fs.append(r)
    return fs


f1, f2, f3 = count()
print(f1(), f2(), f3())

# 装饰器 decorator
# 请编写一个@performance，它可以打印出函数调用的时间。
import time


def performance(f):
    def fn(*args, **kw):
        t1 = time.time()
        r = f(*args, **kw)
        t2 = time.time()
        print('call %s() in %fs' % (f.__name__, (t2 - t1)))
        return r

    return fn


@performance
def factorial(n):
    return reduce(lambda x, y: x * y, range(1, n + 1))


print(factorial(10))

# 带参数的decorator
import time


def performance(unit):
    def perf_decorator(f):
        def wrapper(*args, **kw):
            t1 = time.time()
            r = f(*args, **kw)
            t2 = time.time()
            t = (t2 - t1) * 1000 if unit == 'ms' else (t2 - t1)
            print('call %s() in %f %s' % (f.__name__, t, unit))
            return r

        return wrapper

    return perf_decorator


@performance('ms')
def factorial(n):
    return reduce(lambda x, y: x * y, range(1, n + 1))


print(factorial(10))

# @functools.wraps
import time, functools


def performance(unit):
    def perf_decorator(f):
        @functools.wraps(f)
        def wrapper(*args, **kw):
            t1 = time.time()
            r = f(*args, **kw)
            t2 = time.time()
            t = (t2 - t1) * 1000 if unit == 'ms' else (t2 - t1)
            print('call %s() in %f %s' % (f.__name__, t, unit))
            return r

        return wrapper

    return perf_decorator


@performance('ms')
def factorial(n):
    return reduce(lambda x, y: x * y, range(1, n + 1))


print(factorial.__name__)


# 完善Rational类，实现四则运算。
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


class Rational(object):
    def __init__(self, p, q):
        self.p = p
        self.q = q

    def __add__(self, r):
        return Rational(self.p * r.q + self.q * r.p, self.q * r.q)

    def __sub__(self, r):
        return Rational(self.p * r.q - self.q * r.p, self.q * r.q)

    def __mul__(self, r):
        return Rational(self.p * r.p, self.q * r.q)

    def __div__(self, r):
        return Rational(self.p * r.q, self.q * r.p)

    def __str__(self):
        g = gcd(self.p, self.q)
        return '%s/%s' % (self.p / g, self.q / g)

    __repr__ = __str__


r1 = Rational(1, 2)
r2 = Rational(1, 4)
print(r1 + r2)
print(r1 - r2)
print(r1 * r2)
print(r1 / r2)  # 报错。。。
