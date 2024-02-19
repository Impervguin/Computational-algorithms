import interpolation as inter
import tio

def check_func_root(mat, y):
    for i in range(1, len(mat)):
        if (mat[i - 1][1] > y and mat[i][1] < y) or (mat[i - 1][1] < y and mat[i][1] > y):
            return i - 1
    return -1

# def find_monotonic_around_point(mat, ind):
#     left, right = ind - 1, ind + 1
#     inc = True if (right < len(mat) and mat[right][1] > mat[ind][1]) or (left >= 0 and mat[left][1] < mat[ind][1]) else False
#     mono = [mat[ind]]
#     left_stop, right_stop = False, False
#     while not left_stop or not right_stop:
#         if left >= 0 and ((inc and mat[left][1] < mat[left + 1][1]) or (not inc and mat[left][1] > mat[left + 1][1])):
#             mono.append(mat[left])
#             left -= 1
#         else:
#             left_stop =True
#         if right < len(mat) and ((inc and mat[right][1] > mat[right - 1][1]) or (not inc and mat[right][1] < mat[right - 1][1])):
#             mono.append(mat[right])
#             right += 1
#         else:
#             right_stop = True
#     return mono

# Максимум до второй производной считает
def get_reverse_table(mat):
    rev = []
    for row in mat:
        now = []
        now.extend((row[1], row[0]))
        if (len(row) >= 3):
            now.append(1 / row[2]) # Обратная первая производная
        if (len(row) >= 4):
            now.append(row[3] / row[2] ** 3) # Обратная вторая производная
        rev.append(now)
    return rev

def reverse_newton(mat, n, y):
    ind = check_func_root(mat, y)
    if (ind < 0):
        raise ValueError("У функции нет корня.")
    
    rev = get_reverse_table(mat)

    return inter.newton(rev, n, y)

def reverse_ermit(mat, n, y):
    
    rev = get_reverse_table(mat)

    return inter.ermit(rev, n, y)

if __name__ == "__main__":
    mat = tio.read_matrix("data/data.txt")

    # tio.print_float_matrix(get_reverse_table(mat), header=["y", "x", "x'", "x''"])
    print(reverse_ermit(mat, 0, 0), sep="\n")