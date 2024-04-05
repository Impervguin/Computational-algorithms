import matrix3d as m3
import matrix4d as m4
import plotly.graph_objects as go
import newton
import spline
import tio
import custom
from math import sin, sqrt, exp

NEWTONNX = 3
NEWTONNY = 2
NEWTONNZ = 5

# matrix4d = m4.Matrix4d("./data/data.txt")
matrix4d = m4.Matrix4d(None)

def f(x, y, z):
    if abs(x + y) < 1e-8:
        return 1e8
    return 1. / (x + y) - z

# def f(x, y, z):
#     return exp(2 * x - y) * z ** 2

# def f(x, y, z):
#     return x ** 2 + y ** 2 + z ** 2

# def f(x, y, z):
#     if (x**2 + y**2) < 1e-8:
#         return 1
#     return (sin(sqrt(x**2+y**2)))/(sqrt(x**2+y**2))

# def f(x, y, z):
#     return x - y + z
STARTX = -5
STOPX = 5
STEPX = 20
STARTY = -3
STOPY = 4
STEPY = 50
STARTZ = -1
STOPZ = 2
STEPZ = 30


matrix4d.generateMatrix(STARTX, STOPX, STEPX, STARTY, STOPY, STEPY, STARTZ, STOPZ, STEPZ, f)
print(m4)
X = -0.152
Y = 1.141
Z = 1.43
# примерно -0.42
newt = newton.newton4d(matrix4d, NEWTONNX, NEWTONNY, NEWTONNZ, X, Y, Z)
spl = spline.apprspline4d(matrix4d, X, Y, Z)
cus = custom.customInterpolation4d(matrix4d, NEWTONNX, NEWTONNY, NEWTONNZ, X, Y, Z, "spline", "spline", "spline")
print(f"func: {f(X, Y, Z)}")
print(f"newton: {newt}")
print(f"spline: {spl}")
print(f"custom: {cus}")


Ymax, Ymin, Xmax, Xmin = matrix4d.getYmax(), matrix4d.getYmin(), matrix4d.getXmax(), matrix4d.getXmin()

stepsx = 50
stepsy = 50
dy = (Ymax - Ymin) / stepsy
dx = (Xmax - Xmin) / stepsx

xarr = [Xmin + dx * i for i in range(stepsx + 1)]
yarr = [Ymin + dy * i for i in range(stepsy + 1)]

farr = [[f(x, y, Z) for x in xarr] for y in yarr]
newtonfarr = [[newton.newton4d(matrix4d, NEWTONNX, NEWTONNY, NEWTONNZ, x, y, Z) for x in xarr] for y in yarr]
# splinefarr = [[spline.apprspline4d(matrix4d, x, y, Z) for x in xarr] for y in yarr]
# customarr = [[custom.customInterpolation4d(matrix4d, NEWTONNX, NEWTONNY, NEWTONNZ, x, y, Z, "spline", "newton", "newton") for y in yarr] for x in xarr]


traces = [
    # go.Surface(x=close1.x, y=close1.y, z=close1.z, name=f"Table Z={zs[0]}"),
    go.Surface(x=xarr, y=yarr, z=farr, name=f"Func Z={Z}"),
    go.Surface(x=xarr, y=yarr, z=newtonfarr, name=f"Newton for Z={Z}", colorscale="Blues"),
    # go.Surface(x=xarr, y=yarr, z=splinefarr, name=f"Spline for Z={Z}", colorscale="Viridis"),
    # go.Surface(x=xarr, y=yarr, z=splinefarr, name=f"Custom for Z={Z}")
]

# fig = go.Figure(data=traces)
# fig.show()