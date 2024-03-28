from tio import read_matrix, print_float_matrix
import plotly.graph_objects as go
import newton
import matrix3d as m3
import matrix4d as m4

class Spline:
    def __init__(self, matrix, start, end) -> None:
        self.mat = matrix
        self.a = self.getaCoeffs()
        self.c = self.getcCoeffs(start, end)
        self.b = self.getbCoeffs(start, end)
        self.d = self.getdCoeffs(start, end)
    
    def getaCoeffs(self):
        a = [0] * (len(self.mat) - 1)
        for i in range(1, len(self.mat)):
            a[i - 1] = self.mat[i - 1][1]
        return a
    
    def getcCoeffs(self, start, end):
        c = [0] * (len(self.mat) - 1)
        ksiarr = [0] * (len(self.mat))
        tetaarr = [0] * (len(self.mat))

        c[0] = start / 2
        ksiarr[1] = 0
        tetaarr[1] = start / 2

        for i in range(2, len(self.mat)):
            h_i = self.mat[i][0] - self.mat[i - 1][0]
            h_i1 = self.mat[i - 1][0] - self.mat[i - 2][0]
            
            
            ksiarr[i] = ksi(ksiarr[i - 1], h_i, h_i1)
            dy = self.mat[i][1] - self.mat[i - 1][1]
            dy1 = self.mat[i - 1][1] - self.mat[i - 2][1]

            tetaarr[i] = teta(dy, dy1, h_i, h_i1, tetaarr[i - 1], ksiarr[i - 1])
        c[-1] = tetaarr[-1] + (end / 2) * ksiarr[-1]

        for i in range(len(self.mat) - 2, 0, -1):
            c[i - 1] = tetaarr[i] + c[i] * ksiarr[i]
        
        return c
    
    def getdCoeffs(self, start, end):
        d = [0] * (len(self.mat) - 1)

        for i in range(len(self.mat) - 2):
            d[i] = (self.c[i + 1] - self.c[i]) / (3 * (self.mat[i + 1][0] - self.mat[i][0]))
        
        d[-1] = ((end / 2) - self.c[-1]) / (3 * (self.mat[-1][0] - self.mat[-2][0]))
        return d
    
    def getbCoeffs(self, start, end):
        b = [0] * (len(self.mat) - 1)

        for i in range(len(self.mat) - 2):
            h_i = (self.mat[i + 1][0] - self.mat[i][0])
            b[i] = (self.mat[i + 1][1] - self.mat[i][1]) / h_i - 1 / 3 * h_i * (self.c[i + 1] + 2 * self.c[i])
        h_i = (self.mat[-1][0] - self.mat[-2][0])
        b[-1] = (self.mat[-1][1] - self.mat[-2][1]) / h_i - 1 / 3 * h_i * ((end / 2) + 2 * self.c[-1])

        return b
    
    def approximate(self, x):
        i = 0
        while i < len(self.mat) - 2 and x > self.mat[i + 1][0]:
            i += 1
        
        xi = self.mat[i][0]
        return self.a[i] + (x - xi) * self.b[i] + self.c[i] * (x - xi) ** 2 + self.d[i] * (x - xi) ** 3
        


# func for calculating ksi_i+1
# where 
# ksi1 - ksi_i
# h1 - h_i
# h2 - h_i - 1
# ksi_i + 1 = - hi / (2(h_i-1 + h_i) + h_i - 1*ksi_i)
def ksi(ksi1, h1, h2):
    return - h1 / (2 * (h1 + h2) + h2 * ksi1)


# func for calculating teta_i+1
# where
# teta1 - teta_i 
# ksi1 - ksi_i
# h1 - h_i
# h2 - h_i-1
# dy1 - (yi - yi-1)
# dy1 - (yi-1 - yi-2)
# ksi_i+1 = (3 * ((yi - yi-1)/h_i - (yi-1 - yi-2)/h_i-1) - h_i-1 * teta_i) / (2 * (h_i + h_i-1) + h_i-1 * ksi_i)
def teta(dy1, dy2, h1, h2, teta1, ksi1):
    return (3 * (dy1/h1 - dy2/h2) - h2 * teta1) / (h2 * ksi1 + 2 * (h1 + h2))


def apprspline3d(mat, x, y):
    zx = []
    for yi in range(len(mat.y)):
        sp = Spline(mat.getZXfromY(yi), 0, 0)
        zx.append(sp.approximate(x))
    sp = Spline(list(zip(mat.y, zx)), 0, 0)
    return sp.approximate(y)

def apprspline4d(mat, x, y, z):
    fz = []
    for zi in range(len(mat.z)):
        fz.append(apprspline3d(mat.f[zi], x, y))
    sp = Spline(list(zip(mat.z, fz)), 0, 0)
    return sp.approximate(z)

if __name__ == "__main__":
    # m = m3.Matrix3d("./data/test3d.txt")
    # newx = [((max(m.x) - min(m.x)) * (i / 100)) + min(m.x) for i in range(101)]
    # newy = [((max(m.y) - min(m.y)) * (i / 100)) + min(m.y) for i in range(101)]
    # # print(newx)
    # newz = []
    # for x in newx:
    #     newz.append([])
    #     for y in newy:
    #         newz[-1].append(apprspline3d(m, x, y))
    # data = [
    #     go.Surface(x = m.x, y = m.y, z = m.z),
    #     go.Surface(x=newx, y=newy, z=newz, colorscale='Blues', showscale=False),
    # ]
    # fig = go.Figure(data=data)
    # fig.show()

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
            newz[-1].append(apprspline4d(m, x, y, z))
    data = [
        go.Surface(x = m1.x, y = m1.y, z = m1.z),
        go.Surface(x=m2.x, y=m2.y, z=m2.z, colorscale='Blues', showscale=False),
        go.Surface(x=newx, y=newy, z=newz, colorscale="Viridis", showscale=False)
    ]
    fig = go.Figure(data=data)
    fig.show()