import rand_polynomial as fx
import parameters as params
import pseudo_rand_func as G
import random
import math


# Get initial table
def initial_table(poly, pwd):
    alpha = [0] * params.m
    beta = [0] * params.m
    for i in xrange(1, params.m + 1):
        y_0 = fx.get_y(poly, 2 * i, params.m)
        y_1 = fx.get_y(poly, 2 * i + 1, params.m)
        alpha[i - 1] = y_0 + G.prf(params.r, pwd, str(2 * i))
        beta[i - 1] = y_1 + G.prf(params.r, pwd, str(2 * i + 1))
    save(alpha, beta)
    return alpha, beta


# Create table
def create_table(poly, pwd, data):
    alpha = [0 for i in range(0, params.m)]
    beta = [0 for i in range(0, params.m)]
    for i in range(1, params.m + 1):
        mu, std = stats(data[i - 1])
        if is_distinguishing(params.t, mu, std) and len(data[0]) == params.h:
            if mu <= params.t:
                y_0 = fx.get_y(poly, 2 * i, params.m)
                y_1 = random.getrandbits(150)
            else:
                y_0 = random.getrandbits(150)
                y_1 = fx.get_y(poly, 2 * i + 1, params.m)
        else:
            y_0 = fx.get_y(poly, 2 * i, params.m)
            y_1 = fx.get_y(poly, 2 * i + 1, params.m)
        alpha[i - 1] = y_0 + G.prf(params.r, pwd, str(2 * i))
        beta[i - 1] = y_1 + G.prf(params.r, pwd, str(2 * i + 1))
    save(alpha, beta)
    return alpha, beta


# Get the mean and standard deviation of the feature values
def stats(data):
    mu = sum(data) * 1.0 / len(data)
    var = sum([(i - mu) ** 2 for i in data]) / len(data)
    return mu, math.sqrt(var)


# Helper function to check a feature is distinguishing or not.
def is_distinguishing(t, mu, std):
    return abs(mu - t) > params.k * std


# Write to the instruction table file
def save(alpha, beta):
    f = open(params.it_file, 'w')
    for i in range(0, len(alpha)):
        f.write(str(alpha[i]) + ', ' + str(beta[i]) + '\n')



