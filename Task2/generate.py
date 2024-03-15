import csv
import math as m
# def f(x):
#     return x ** 2 - m.cos(x) * 4

def f(x):
    return 4 * m.cos(x) + x / 5
MIN_X = -10
MAX_X = 15
COUNT = 100
fname = "./data/test3"

x = [MIN_X + x * (MAX_X - MIN_X) / COUNT for x in range(COUNT)]
y = [f(X) for X in x]

with open(fname, "w", encoding="utf-8") as f:
    writer = csv.writer(f, delimiter="\t")
    for i in range(len(x)):
        writer.writerow((x[i], y[i]))

# f = open(fname, "w")
# for i in range(len(x)):
#     f.write(f"{x[i]}\t{y[i]}\n")
# f.close()