import interpolation as inter
import reverse_interpolation as rinter
import tio

def get_sub_table_newton(mat1, mat2, n):
    res = []

    for row in mat1:
        res.append([row[0], inter.newton(mat2, n, row[0]) - row[1]])
    
    for row in mat2:
        res.append([row[0], row[1] - inter.newton(mat1, n, row[0])])
    
    return sorted(res)

def get_system_root_newton(mat1, mat2, n):
    sub_table = get_sub_table_newton(mat1, mat2, n)

    return rinter.reverse_newton(sub_table, n, 0)

if __name__ == "__main__":
    mat1 = tio.read_matrix("data/sys1.txt")
    mat2 = tio.read_matrix("data/sys2.txt")
    tio.print_float_matrix(get_sub_table_newton(mat1, mat2, 4))
    print(get_system_root_newton(mat1, mat2, 4))