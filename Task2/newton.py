from copy import deepcopy
import math as m
import tio

def newton_divided_difference(mat):
    diff_mat = [[row[1] for row in mat]]
    for i in range(1, len(mat)):
        tmp = []
        for j in range(len(mat) - i):
            tmp.append((diff_mat[i - 1][j + 1] - diff_mat[i - 1][j]) / (mat[i + j][0] - mat[j][0]))
        diff_mat.append(tmp)
    return diff_mat

def newton(mat, n, x):
    new_mat = tio.get_nearest_in_mat(mat, n + 1, x)
    diff_table = newton_divided_difference(new_mat)
    res = diff_table[0][0]
    x_mult = 1
    for i in range(1, n + 1):
        x_mult *= (x - new_mat[i - 1][0])
        res += x_mult * diff_table[i][0]
    return res

def newtonSecondDeriativeThird(mat, x):
    new_mat = tio.get_nearest_in_mat(mat, 4, x)
    diff_table = newton_divided_difference(new_mat)
    return 2 * diff_table[2][0] + diff_table[3][0] * (6 * x - 2 * (new_mat[0][0] + new_mat[1][0] + new_mat[2][0]))
    