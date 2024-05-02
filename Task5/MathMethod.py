from numpy import sqrt

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

def NewtonSystem(jacobianFunc, funcs : list, x0 : list, maxIter=10, epsilon=1e-2):
    def f(x):
        return [f(*x) for f in funcs]
    
    xk = x0
    n = 1
    while True:
        dx = Gauss(jacobianFunc(*xk), [-y for y in f(xk)])
        xnext = [xk[i] + dx[i] for i in range(len(xk))]
        if sqrt(sum([x ** 2 for x in dx])) < epsilon or n == maxIter:
            return xnext, n
        xk = xnext
        n += 1

def SympsonIntegral(x : list, f):
    
    def symfunc(a, b):
        return ((b - a) / 6) * (f(a) + 4 * f ((a + b) / 2) + f(b))

    return sum([symfunc(x[i], x[i + 1])  for i in range(len(x) - 1)])


def HalfDivision(f, y, a, b, maxIter=10, epsilon=1e-2):
    n = 1
    while True:
        c = (a + b) / 2
        if abs(f(c) - y) < epsilon or n == maxIter:
            return c, n
        if (f(a) - y) * (f(c) - y) < 0:
            b = c
        else:
            a = c
        n += 1


                      

    

