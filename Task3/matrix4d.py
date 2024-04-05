import matrix3d as m3
import tio

class Matrix4d:
    def __init__(self, fname) -> None:
        self.z = []
        self.f = []
        if (fname != None):
            with open(fname, "r") as fin:
                self.readMatrix(fin)
    
    def readMatrix(self, f):
        s = f.readline().strip()
        n = 1
        while s != "":
            try:
                z = float(s)
            except ValueError:
                raise ValueError(f"Incorrect z format in row №{n}")
            
            mat = m3.Matrix3d(None)
            try:
                mat.readMatrix(f)
            except ValueError as e:
                raise ValueError("Error while reading xy matrix") from e
            self.z.append(z)
            self.f.append(mat)

            s = f.readline().strip()
            n += 1
        if not self.checkAxis():
            raise ValueError("Different xy axis in z-slices")
        self.sortZ()

    def checkAxis(self):
        for i in range(len(self.f) - 1):
            if not self.f[i].axiseq(self.f[i - 1]):
                return False
        return True

    def sortZ(self):
        self.z, self.f = zip(*sorted(zip(self.z, self.f), key=lambda t: t[0]))

    def getNearestZIndex(self, z, n):
        if len(self.z) < n:
            raise ValueError(f"Size out of range: Z-size({len(self.Z)}), n({n})")
        t = list(zip(self.z, range(len(self.z))))
        return tio.get_nearest_in_mat(t, n, z)

    def getZSlice(self, zindex):
        if len(self.z) <= zindex:
            raise ValueError(f"Z-slice index out of range: {zindex}")
        return self.f[zindex]

    def getXmax(self):
        return self.f[0].x[-1]

    def getXmin(self):
        return self.f[0].x[0]

    def getYmax(self):
        return self.f[0].y[-1]

    def getYmin(self):
        return self.f[0].y[0]

    def generateMatrix(self, xs, xe, xsteps, ys, ye, ysteps, zs, ze, zsteps, func):
        x = [(xe - xs) / xsteps * i + xs for i in range(xsteps + 1)]
        y = [(ye - ys) / ysteps * i + ys for i in range(ysteps + 1)]
        z = [(ze - zs) / zsteps * i + zs for i in range(zsteps + 1)]
        for zv in z:
            m = m3.Matrix3d(None)
            m.x = x
            m.y = y
            m.z = [[0] * len(x) for _ in range(len(y))]
            for i in range(len(x)):
                for j in range(len(y)):
                    
                    # if abs(x[i] + y[j]) < 10e-8:
                    #     f = 1e8
                    # else:
                    #     f = func(x[i], y[j], zv)
                    f = func(x[i], y[j], zv)
                    m.z[j][i] = f
            self.f.append(m)
        self.z = z

        
        
if __name__ == "__main__":
    m = Matrix4d("./data/data.txt")
    # print(m.z)
    # print(m.f)
    # print()
    # print(m.z, sep="\n")
    # print(m.getZXfromY(2))
    # fig = go.Figure(go.Surface(x = m.x, y = m.y, z = m.z))
    # fig.show()