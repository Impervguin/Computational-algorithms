

def Readfunction(filename):
    with open(filename, "r") as f:
        data = f.read().splitlines()
    for i in range(len(data)):
        data[i] = data[i].split()

    x = data[0][1:]
    y = []
    for i in range(1, len(data)):
        y.append(data[i][0])
    z = []
    for i in range(1, len(data)):
        z.append(data[i][1:])
    
    x = list(map(float, x))
    y = list(map(float, y))
    z = [[float(z[i][j]) for j in range(len(z[i]))]for i in range(len(z))]

    return x, y, z