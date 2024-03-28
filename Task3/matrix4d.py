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
        
        self.sortZ()
    
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
        
        
if __name__ == "__main__":
    m = Matrix4d("./data/data.txt")
    # print(m.z)
    # print(m.f)
    # print()
    # print(m.z, sep="\n")
    # print(m.getZXfromY(2))
    # fig = go.Figure(go.Surface(x = m.x, y = m.y, z = m.z))
    # fig.show()