import plotly.graph_objects as go
import plotly.express as px

class Matrix3d:
    def __init__(self, fname) -> None:
        self.x = []
        self.y = []
        self.z = []
        if (fname != None):
            with open(fname, "r") as fin:
                self.readMatrix(fin)
    

    def readMatrix(self, fin):
        self.x = list(map(float, fin.readline().split()[1:]))
        self.y = []
        self.z = []
        s = fin.readline()
        while s != "":
            # print(s)
            s = s.split()
            self.y.append(float(s[0]))
            self.z.append(list(map(float, s[1:])))
            s = fin.readline()


if __name__ == "__main__":
    m = Matrix3d("./data/test3d.txt")
    print(m.x)
    print(m.y)
    print()
    print(m.z, sep="\n")


    # trace = go.Surface(x=m.x, y=m.y, z=m.z)
    # fig = go.Figure(data=[trace])
    fig = go.Figure(go.Surface(x = m.x, y = m.y, z = m.z))
    # z = m.z[0]
    # fig = px.scatter_3d(x=m.x, y=m.y, z=z)
    # px.l
    fig.show()

        
            


