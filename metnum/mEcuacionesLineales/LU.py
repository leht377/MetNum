import numpy as np
from .helpers import sustprogr, sustregr


def LU(A, b):
    A = np.array(A)
    b = np.array(b)

    n = len(A)
    aux = np.zeros((n, n), dtype=float)

    aux[0][0] = A[0][0]

    if aux[0][0] == 0:
        print("No")
        return 0

    for s in range(1, n):

        aux[0][s] = A[0][s]
        aux[s][0] = np.divide(A[s][0], aux[0][0])

    for r in range(1, n):

        aux[r][r] = A[r][r] - (np.dot(aux[r, :r], aux[:r, r]))
        if aux[r][r] == 0:
            print("lazar error")
            return 0
        for s in range(r + 1, n):
            aux[r][s] = A[r][s] - np.dot(aux[r, :r], aux[:r, s])
            aux[s][r] = (A[s][r] - np.dot(aux[s, :r], aux[:r, r])) / aux[r][r]

    L = np.tril(aux, -1) + np.eye(n)
    U = np.triu(aux)

    y = sustprogr(L, b)
    x = sustregr(U, y)

    return x
