import random
import parameters as params
from mpmath import *


def rand_poly(m):
    coefficients = [0] * m
    for i in xrange(0, m):
        coefficients[i] = random.getrandbits(160) % params.q
    return coefficients


def get_y(fx, x, m):
    y = 0
    for i in range(0, m):
        y += fx[i] * (x ** i)
    return y


def round_value(m):
    if ceil(m) - m < 0.5:
        return ceil(m)
    else:
        return floor(m)


def lagrange_interpolation(points):
    def P(x):
        mp.dps = 1000
        total = mpf(0)
        n = len(points)
        for i in xrange(n):
            xi, yi = points[i]

            def g(i, n):
                tot_mul = mpf(1)
                for j in xrange(n):
                    if i == j:
                        continue
                    xj, yj = points[j]
                    tot_mul = tot_mul * (x - xj) / (xi - xj)
                return tot_mul

            total += (g(i, n) * yi)
        return int(round_value(total))

    return P
