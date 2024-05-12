

def OneSideDiff(X, Y) -> list[float]:
    if len(X)!= len(Y):
        raise ValueError("X and Y must have the same length")
    return [(Y[i + 1] - Y[i]) / (X[i + 1] - X[i]) for i in range(len(X) - 1)] + \
           [(Y[-1] - Y[-2]) / (X[-1] - X[-2])]

def TwoSideDiff(X, Y) -> list[float]:
    if len(X)!= len(Y):
        raise ValueError("X and Y must have the same length")
    return [(-3 * Y[0] + 4 * Y[1] - Y[2]) / (X[2] - X[0])] + \
           [(Y[i + 1] - Y[i - 1]) / (X[i + 1] - X[i - 1]) for i in range(1, len(X) - 1)] + \
           [(Y[-3] - 4 * Y[-2] + 3 * Y[-1]) / (X[-1] - X[-3])]

def SecondRungeDiff(X, Y) -> list[float]:
    if len(X)!= len(Y):
        raise ValueError("X and Y must have the same length")
    return [(-Y[i + 2] + 4 * Y[i + 1] - 3 * Y[i]) / (X[i + 2] - X[i]) for i in range(len(X) -2)] + \
        [(3 * Y[i] - 4 * Y[i - 1] + Y[i - 2]) / (X[i] - X[i - 2]) for i in range(len(X) - 2, len(X))]

def LevellingDiff(X, Y) -> list[float]:
    if len(X)!= len(Y):
        raise ValueError("X and Y must have the same length")
    return [(Y[i] / X[i]) * (X[i+1] / Y[i+1]) * ((Y[i] - Y[i+1]) / (X[i] - X[i+1])) for i in range(len(X) - 1)] + \
           [(Y[-2] / X[-2]) * (X[-1] / Y[-1]) * ((Y[-2] - Y[-1]) / (X[-2] - X[-1]))]


def SecondDiff(X, Y) -> list[float]:
    if len(X)!= len(Y):
        raise ValueError("X and Y must have the same length")
    return [(Y[2] - 2 * Y[1] + Y[0]) / ((X[2] - X[1]) * (X[1] - X[0]))] + \
           [(Y[i + 1] - 2 * Y[i] + Y[i - 1]) / ((X[i + 1] - X[i]) * (X[i] - X[i - 1])) for i in range(1, len(X) - 1)] + \
           [(Y[-3] - 2 * Y[-2] + Y[-1]) / ((X[-3] - X[-2]) * (X[-2] - X[-1]))]

