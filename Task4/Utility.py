from numpy import linspace
from random import random

def read_xypdata(filename):
    with open(filename, "r") as f:
        data = f.read().splitlines()
    for i in range(len(data)):
        data[i] = data[i].split()
    x, y, p = zip(*data[1:])
    x = list(map(float, x))
    y = list(map(float, y))
    p = list(map(float, p))
    return x, y, p

def get_xypdata(xs, xe, xstep, ps, pe, func):
    x = list(linspace(xs, xe, xstep))
    y = [func(xi) for xi in x]
    pcoef = (pe - ps)
    p = [random() * pcoef + ps for _ in range(len(x))]

    return x, y, p
