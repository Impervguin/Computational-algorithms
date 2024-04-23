from Utility import *
def LeastSquaresCoefs(x, y, p, n):
    dataLen = len(x)
    if dataLen != len(y) or dataLen != len(p):
        raise ValueError("x, y and p must have the same length")

    aCoeffsx = [sum([p[i] * x[i] ** j for i in range(dataLen)]) for j in range(2 * n + 1)]
    aCoeffsy = [sum([p[i] * y[i] * x[i] ** j for i in range(dataLen)]) for j in range(n + 1)]
    CoeffMat = [[aCoeffsx[i + j] for i in range(n + 1)] for j in range(n + 1)]

    return Gauss(CoeffMat, aCoeffsy)

def LeastSquare(x, y, p, n, xp):
    a = LeastSquaresCoefs(x, y, p, n)
    return sum([a[i] * xp ** i for i in range(n + 1)])

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

x, y, p = read_xypdata("data/tmp41")


print(LeastSquaresCoefs(x, y, p, 2))