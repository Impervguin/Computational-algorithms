import matrix3d as m3
import matrix4d as m4
import plotly.graph_objects as go
import newton
import spline
import tio

NEWTONNX = 3
NEWTONNY = 3
NEWTONNZ = 3

matrix4d = m4.Matrix4d("./data/data.txt")

Z = float(input("Фиксированное z(идеально 0-4): "))

Ymax, Ymin, Xmax, Xmin = matrix4d.getYmax(), matrix4d.getYmin(), matrix4d.getXmax(), matrix4d.getXmin()

steps = 20
dy = (Ymax - Ymin) / steps
dx = (Xmax - Xmin) / steps

xarr = [Xmin + dx * i for i in range(steps + 1)]
yarr = [Ymin + dy * i for i in range(steps + 1)]

newtonfarr = [[newton.newton4d(matrix4d, NEWTONNX, NEWTONNY, NEWTONNZ, x, y, Z) for y in yarr] for x in xarr]
splinefarr = [[spline.apprspline4d(matrix4d, x, y, Z) for y in yarr] for x in xarr]

zs, zindexes = zip(*matrix4d.getNearestZIndex(Z, 2))
close1, close2 = matrix4d.f[zindexes[0]], matrix4d.f[zindexes[1]]

traces = [
    go.Surface(x=close1.x, y=close1.y, z=close1.z, name=f"Table Z={zs[0]}"),
    go.Surface(x=close2.x, y=close2.y, z=close2.z, name=f"Table Z={zs[1]}"),
    go.Surface(x=xarr, y=yarr, z=newtonfarr, name=f"Newton for Z={Z}", colorscale="Blues"),
    go.Surface(x=xarr, y=yarr, z=splinefarr, name=f"Spline for Z={Z}", colorscale="Viridis"),
]

fig = go.Figure(data=traces)
fig.show()