import numpy as np
from .helpers import sustprogr, sustregr

# TODO revisar codigo en la obtencion de L, U
# TODO realizar documentacion del metodo
# TODO realizar cheking de tipos de datos del metodo


def LU(A, b):
    A = np.array(A)
    b = np.array(b)

    n = len(A)
    aux = np.zeros((n, n), dtype=float)

    aux[0][0] = A[0][0]

    if aux[0][0] == 0:  # TODO Hacer exepciones
        raise ValueError("No se puede realizar la factorizacion LU")

    for i in range(1, n):

        aux[0][i] = A[0][i]
        aux[i][0] = np.divide(A[i][0], aux[0][0])

    for j in range(1, n):

        aux[j][j] = A[j][j] - (np.dot(aux[j, :j], aux[:j, j]))
        if aux[j][j] == 0:
            raise ValueError("No se puede realizar la factorizacion LU")
        for i in range(j + 1, n):
            aux[j][i] = A[j][i] - np.dot(aux[j, :j], aux[:j, i])
            aux[i][j] = (A[i][j] - np.dot(aux[i, :j], aux[:j, j])) / aux[j][j]

    L = np.tril(aux, -1) + np.eye(n)
    U = np.triu(aux)

    y = sustprogr(L, b)
    x = sustregr(U, y)

    return x
