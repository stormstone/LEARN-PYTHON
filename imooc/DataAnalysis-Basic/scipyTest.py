# -*- coding: utf-8 -*-
# @Time    : 2017-10-17 15:26
# @Author  : Storm
# @File    : scipyTest.py
import numpy as np
from scipy.integrate import quad, dblquad, nquad
from scipy.optimize import minimize


def main():
    # 1--Integral积分
    print(quad(lambda x: np.exp(-x), 0, np.inf))  # 0到无穷大，结果为值和误差范围
    # dblquad,二元积分
    print(dblquad(lambda t, x: np.exp(-x * t) / t ** 3, 0, np.inf, lambda x: 1, lambda x: np.inf))

    # n重积分
    def f(x, y):
        return x * y

    def bound_y():
        return [0, 0.5]

    def bound_x(y):
        return [0, 1 - 2 * y]

    print("NQUAD", nquad(f, [bound_x, bound_y]))

    # 2--Optimizer优化器
    def rosen(x):
        return sum(100.0 * (x[1:] - x[:-1] ** 2.0) ** 2.0 + (1 - x[:1]) ** 2.0)

    x0 = np.array([1.3, 0.7, 0.8, 1.9, 1.2])
    res = minimize(rosen, x0, method="nelder-mead", options={"xtol": 1e-8, "disp": True})
    print("rosen:",rosen(x0))
    print("ROSE MINI:", res)


if __name__ == '__main__':
    main()
