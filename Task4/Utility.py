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

def get_xyzpdata(xs, xe, xstep, ys, ye, ystep,  ps, pe, func):
    x = []
    y = []
    z = []
    p = []
    for xi in linspace(xs, xe, xstep):
        for yi in linspace(ys, ye, ystep):
            x.append(xi)
            y.append(yi)
            z.append(func(xi, yi))
            p.append(random() * (pe - ps) + ps)
    return x, y, z, p

def read_xypzdata(filename):
        with open(filename, "r") as f:
            data = f.read().splitlines()
        for i in range(len(data)):
            data[i] = data[i].split()
        z, y, x, p = zip(*data[1:])
        x = list(map(float, x))
        y = list(map(float, y))
        z = list(map(float, z))
        p = list(map(float, p))
        return x, y, z, p

# get_xyzpdata(-10, 10, 20, -10, 10, 20, 0, 1, lambda x, y: x + y)