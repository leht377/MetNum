from math import log, ceil
import numpy as np
from module.plot import biseccionPlot


def biseccion(f, a, b, tol, plot=False) -> object:

    n = 1
    c = (a + b) / 2
    yc = f(c)
    maxIter = ceil((log(b - a) - log(tol)) / log(2)) - 1
    ya = f(a)
    yb = f(b)

    historyA = np.array([a])
    historyB = np.array([b])
    historyC = np.array([c])

    for n in range(maxIter):

        if yc == 0:  # La rai­z es c
            a = c
            b = c
            print("Se ha alcanzado el cero exacto \n")
            break
        elif yb * yc > 0:  # La rai­z esta en [a,c]
            b = c
            yb = yc
        else:  # La rai­z esta en [c,b]
            a = c
            ya = yc

        c = (a + b) / 2
        yc = f(c)

        historyA = np.append(historyA, a)
        historyB = np.append(historyB, b)
        historyC = np.append(historyC, c)

    plot and biseccionPlot.paintgrafico(f, historyA, historyB, historyC)

    return {"caprox": c, "err": abs(yc), "numiter": n + 1}


f = lambda x: x**2 + 3 * x - 34
a = 3
b = 8
tol = 10**-6


print(biseccion(f, a, b, tol))
