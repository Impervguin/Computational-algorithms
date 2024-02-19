from copy import deepcopy
import math as m
import tio

def newton_divided_difference(mat):
    diff_mat = [[row[1] for row in mat]]
    # print(diff_mat)
    for i in range(1, len(mat)):
        tmp = []
        for j in range(len(mat) - i):
            tmp.append((diff_mat[i - 1][j + 1] - diff_mat[i - 1][j]) / (mat[i + j][0] - mat[j][0]))
        diff_mat.append(tmp)
    return diff_mat


def ermit_divided_difference(mat):
    diff_mat = [[row[1][1] for row in mat]]
    for i in range(1, len(mat)):
        tmp = []
        for j in range(len(mat) - i):
            for k in range(j, i + j):
                if mat[k][0] != mat[k + 1][0]:
                    break
            else:
                if (len(mat[j][1]) - 2 >= i):
                    tmp.append(mat[j][1][i + 1] / m.factorial(i)) # Добавляем производную при одинаковых строках
                    continue
            tmp.append((diff_mat[i - 1][j + 1] - diff_mat[i - 1][j]) / (mat[i + j][1][0] - mat[j][1][0]))
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

def ermit(mat, n, x):
    new_mat = tio.get_nearest_in_mat(mat, n, x)
    zip_mat = list(zip(range(1, n + 2), new_mat))
    new_mat = []
    i = 0
    for row in zip_mat:
        new_mat.append(row)
        num = len(row[1]) - 2 # Количество производных у i-ой точки
        if num:
            new_mat.extend([deepcopy(row) for _ in range(num)])
    
    diff_table = ermit_divided_difference(new_mat)
    # print("Ermit")
    
    # tio.print_float_matrix(diff_table)
    res = diff_table[0][0]
    x_mult = 1
    for i in range(1, len(diff_table)):
        x_mult *= (x - new_mat[i - 1][1][0])
        res += x_mult * diff_table[i][0]
    return res

if __name__ == "__main__":
    mat = tio.read_matrix("data/data.txt")
    print(mat)
    print(ermit(mat, 0, 2.3), sep="\n")