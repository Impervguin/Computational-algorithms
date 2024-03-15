import csv



def read_matrix(fname):
    mat = []
    with open(fname, "r", encoding="utf-8") as fio:
        reader = csv.reader(fio, delimiter="\t")
        mat = [row for row in reader][1:]
    return sorted([list(map(float, row)) for row in mat], key=lambda x: x[0])

def get_nearest_in_mat(mat, n, x):
    if len(mat) < n:
        raise ValueError("Not enough matrix size")
    # diff = x - mat[0][0]
    i = 1
    while i < len(mat) and x - mat[i][0] > 0:
        # diff = mat[i][0] - x
        i += 1
    if i == len(mat):
        return mat[-n:]
    # print(i)
    res = []
    j = i - 1
    while len(res) < n:
        if (i >= len(mat) and j < 0):
            raise ValueError("Not enough matrix size")
        if (j >= 0):
            res.append(mat[j])
            j -= 1
        if (i < len(mat) and len(res) < n):
            res.append(mat[i])
            i += 1
        
    
    return sorted(res, key=lambda x: x[0])
        
def print_float_matrix(mat, header=None):
    max_len = 0
    for row in mat:
        for el in row:
            max_len = max(max_len, len(f"{el:.5g}"))
    if header:
        for el in header:
            max_len = max(max_len, len(el))
        print(" ", end="")
        for el in header:
            print(" " * (max_len - len(el) + 1) + el, end="")
        print()
    for row in mat:
        print(" ", end="")
        for el in row:
            s_el = f"{el:.5g}"
            print(" " * (max_len - len(s_el) + 1) + s_el, end="")
        print()

if __name__ == "__main__":
    mat = read_matrix("data/data.txt")
    print(*mat, sep="\n")
    print()
    print(*get_nearest_in_mat(mat, 6, 3.35), sep="\n")
    
