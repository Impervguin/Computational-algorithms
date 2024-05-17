from numpy import sqrt, cos, pi
import numpy as np

def Gauss(CoeffMat, Rights):
    n = len(CoeffMat)
    if n != len(Rights):
        raise ValueError("Mat and Rights must have the same length")
    # приводим к треугольному виду
    for i in range(n):
        for j in range(i + 1, n):
            coeff = -(CoeffMat[j][i] / CoeffMat[i][i])
            for k in range(i, n):
                CoeffMat[j][k] += coeff * CoeffMat[i][k]
            Rights[j] += coeff * Rights[i]
    # Приводим к диагональному виду
    for i in range(n - 1, -1, -1):
        for j in range(i - 1, -1, -1):
            coeff = -(CoeffMat[j][i] / CoeffMat[i][i])
            CoeffMat[j][i] += coeff * CoeffMat[i][i]
            Rights[j] += coeff * Rights[i]
    #  Находим решения слау
    res = [Rights[i] / CoeffMat[i][i] for i in range(n)]
    return res

def SympsonIntegral(x : list, f):
    
    def symfunc(a, b):
        return ((b - a) / 6) * (f(a) + 4 * f ((a + b) / 2) + f(b))

    return sum([symfunc(x[i], x[i + 1])  for i in range(len(x) - 1)])

# def LegendrePolynom(n : int, x : float):
#     if n < 0:
#         raise ValueError("n must be >= 0")
#     if n == 0:
#         return 1
#     if n == 1:
#         return x
#     return ((2 * n - 1) * x * LegendrePolynom(n - 1, x) - (n - 1) * LegendrePolynom(n - 2, x)) / n

PascalTriangleMat = [[1]]

def CalculatePascalTriangle(n: int):
    for i in range(len(PascalTriangleMat), n + 1):
        row = [1]
        for k in range(len(PascalTriangleMat[i - 1]) - 1):
            row.append(PascalTriangleMat[i - 1][k] + PascalTriangleMat[i - 1][k + 1])
        row.append(1)
        PascalTriangleMat.append(row)

def PascalTriangle(n : int, k : int):
    CalculatePascalTriangle(n)
    return PascalTriangleMat[n][k]


def LegendrePolynom(n : int, x : float):
    return 1 / 2**n * sum([(-1)**i * PascalTriangle(n, i) * PascalTriangle(2 * n - 2 * i, n) * x ** (n - 2 * i)   for i in range(n // 2 + 1)])

def LegendrePolynomDiff(n : int, x : float):
    return n / (1 - x ** 2) * (LegendrePolynom(n - 1, x) - x * LegendrePolynom(n, x))

def LegendreRoots(n : int, eps=1e-8):
    roots = [cos(pi * (4 * i + 3) / (4 * n + 2)) for i in range(n)]
    for i in range(len(roots)):
        rootVal = LegendrePolynom(n, roots[i])
        while abs(rootVal) > eps:
            roots[i] -= rootVal / LegendrePolynomDiff(n, roots[i])
            rootVal = LegendrePolynom(n, roots[i])
    return roots

def GaussIntegral(a, b, n, f):
    tValues = LegendreRoots(n)
    xValues = [(b + a) / 2 + (b - a) / 2 * t for t in  tValues]

    Amatrix = [[tValues[j] ** i for j in range(n)] for i in range(n)]
    Y = [2 / (i + 1) if i % 2 == 0 else 0 for i in range(n)]
    Acoeffs = Gauss(Amatrix, Y)
    return (b - a) / 2 * sum([Acoeffs[i] * f(xValues[i]) for i in range(n)])

def SplineCoeffs(x, y):
    x = np.array(x)
    y = np.array(y)

    deltaX = np.diff(x)
    deltaY = np.diff(y)

    A = np.zeros((len(x), len(x)))
    B = np.zeros(len(x))
    A[0, 0] = 1
    A[-1, -1] = 1

    for i in range(1, len(x) - 1):
        A[i, i - 1] = deltaX[i - 1]
        A[i, i] = 2 * (deltaX[i - 1] + deltaX[i])
        A[i, i + 1] = deltaX[i]
        B[i] = 3 * ((deltaY[i] / deltaX[i]) - (deltaY[i - 1] / deltaX[i - 1]))
    
    C = np.array(Gauss(A, B))

    B = np.zeros(len(x) - 1)
    D = np.zeros(len(x) - 1)
    A = np.zeros(len(x) - 1)

    for i in range(0, len(x) - 1):
        D[i] = (C[i + 1] - C[i]) / (3 * deltaX[i])
        B[i] = (deltaY[i] / deltaX[i]) - (deltaX[i] / 3) * (2 * C[i] + C[i + 1])
        A[i] = y[i]

    return A, B, C, D

def SplineFunc(x, y):
    A, B, C, D = SplineCoeffs(x, y)
    def f(x0):
        xInd = 0
        if x0 < x[0]:
            xInd = 0
        # elif x0 > x[-1]:
        #     xInd = len(x) - 2
        else:
            for i in range(1, len(x)):
                if x0 < x[i]:
                    xInd = i - 1
                    break
            else:
                xInd = len(x) - 2
        return A[xInd] + (x0 - x[xInd]) * B[xInd] +(x0 - x[xInd]) ** 2 * C[xInd] + (x0 - x[xInd]) ** 3 * D[xInd]
    return f

def Spline2DFunc(x, y, z):
    FixYFuncs = []
    for yi in range(len(y)):
        FixYFuncs.append(SplineFunc(x, [z[yi][i] for i in range(len(x))]))
        # zx.append(spf(x0))

    def f(x0, y0):
        zx = []
        for yi in range(len(y)):
            zx.append(FixYFuncs[yi](x0))
        return SplineFunc(y, zx)(y0)
    # spf = SplineFunc(y, zx)
    # return spf(y0)
    return f

# if __name__ == "__main__":
#     print(LegendrePolynom(5, 0.2))
#     print(LegendrePolynomA(5, 0.2))