from copy import deepcopy
import math as m
import tio
import matrix3d as m3
import matrix4d as m4
import plotly.graph_objects as go

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

def newton3d(mat: m3.Matrix3d, nx, ny, x, y):
    # neary = [i[0] for i in tio.get_nearest_in_mat(mat.getZYfromX(0), ny + 1, y)]
    neary = mat.getNearestYIndex(y, ny + 1)
    neary, nearyindexes = zip(*neary)
    zy = []
    for yi in nearyindexes:
        zy.append(newton(mat.getZXfromY(yi), nx, x))
    return newton(list(zip(neary, zy)), ny, y)

def newton4d(mat: m4.Matrix4d, nx, ny, nz, x, y, z):
    # nearz = [i[0] for i in tio.get_nearest_in_mat([[z] for z in mat.z], nz + 1, z)]
    nearz = mat.getNearestZIndex(z, nz + 1)
    nearz, nearzindexes = zip(*nearz)
    fz = []
    for zi in nearzindexes:
        fz.append(newton3d(mat.getZSlice(zi), nx, ny, x, y))
    return newton(list(zip(nearz, fz)), nz, z)



if __name__ == "__main__":
    # m = m3.Matrix3d("./data/test3d.txt")
    m = m4.Matrix4d("./data/data.txt")
    m1 = m.f[3]
    m2 = m.f[4]
    z = 4
    newx = [4 * (i / 100) for i in range(101)]
    newy = [4 * (i / 100) for i in range(101)]
    # print(newx)
    newz = []
    for x in newx:
        newz.append([])
        for y in newy:
            newz[-1].append(newton4d(m, 3, 3, 3, x, y, z))
    data = [
        go.Surface(x = m1.x, y = m1.y, z = m1.z),
        go.Surface(x=m2.x, y=m2.y, z=m2.z, colorscale='Blues', showscale=False),
        go.Surface(x=newx, y=newy, z=newz, colorscale="Viridis", showscale=False)
    ]
    fig = go.Figure(data=data)
    fig.show()
    # newx = [((max(m.x) - min(m.x)) * (i / 100)) + min(m.x) for i in range(101)]
    # newy = [((max(m.y) - min(m.y)) * (i / 100)) + min(m.y) for i in range(101)]
    # # print(newx)
    # newz = []
    # for x in newx:
    #     newz.append([])
    #     for y in newy:
    #         newz[-1].append(newton3d(m, 3, 3, x, y))
    # data = [
    #     go.Surface(x = m.x, y = m.y, z = m.z),
    #     go.Surface(x=newx, y=newy, z=newz, colorscale='Blues', showscale=False),
    # ]
    # fig = go.Figure(data=data)
    # fig.show()
    # print(newton4d(m, 3, 3, 3, 1.5, 1.5, 1.5))
