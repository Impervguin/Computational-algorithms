import interpolation as inter
import reverse_interpolation as rinter
import system
import tio

EPS=1e-3

newton_res = []
ermit_res = []

def binary_search_root(left, right, mat, n):
    while right - left > EPS:
        middle = (left + right) / 2
        y = inter.newton(mat, n, middle)
        if y > 0:
            right = middle
        else:
            left = middle
    return left

mat = tio.read_matrix("./data/data1.txt")
MAX_N = 4
FIX_X = 1
# tio.print_float_matrix(mat)

# for i in range(1, MAX_N + 1):
#     newton_res.append(inter.newton(mat, i, FIX_X))

# for i in range(1, MAX_N + 1):
#     ermit_res.append(inter.ermit(mat, i, FIX_X))

# print(f"Полином Ньютона для точки {FIX_X}:")

# tio.print_float_matrix([newton_res], header=[f"n={i}"for i in range(1, MAX_N + 1)])
# print()
# print(f"Полином Эрмита для точки {FIX_X}:")
# tio.print_float_matrix([ermit_res], header=[f"n={i}"for i in range(1, MAX_N + 1)])



ROOT_N = 3
print()
print("Нахождение корня функции:")
print(f"Решение полиномом Ньютона при n={ROOT_N}: {rinter.reverse_newton(mat, ROOT_N, 0)}")
# print(f"Решение полиномом Эрмита при n={ROOT_N + 1}: {rinter.reverse_ermit(mat, ROOT_N + 1, 0)}")
# print(f"Решение бинарным поиском: {binary_search_root(mat[0][0], mat[-1][0], mat, 3)}")

# print()


# SYSTEM_N = 3
# mat1 = tio.read_matrix("data/sys1.txt")
# mat2 = tio.read_matrix("data/sys2.txt")

# print(f"Решение системы уравнений при n={SYSTEM_N}: {system.get_system_root_newton(mat1, mat2, SYSTEM_N)}")