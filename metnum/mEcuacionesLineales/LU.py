import numpy as np
from .helpers import resolver_para_x, resolver_para_y
from ..decorators import args_types_cheking, transform_np_array


@args_types_cheking
@transform_np_array
def LU(A: list | np.ndarray, b: list | np.ndarray) -> np.ndarray:
    """
    Realiza la descomposición LU por el método Doolitle de una matriz A y resuelve el sistema de ecuaciones lineales Ax = b .

    Params:
    A (list | np.ndarray): Matriz de coeficientes del sistema de ecuaciones lineales.
    b (list | np.ndarray): Vector de términos independientes.

    Return:
    np.ndarray: El vector x que satisface el sistema de ecuaciones lineales Ax = b.

    Raise:
    ValueError: Si no se puede realizar la factorización LU debido a un elemento diagonal igual a cero.

    Examples: 

    >>> A = np.array([[2, -1, 0],
    ...               [-1, 2, -1],
    ...               [0, -1, 2]])
    >>> b = np.array([1, 0, -1])
    >>> LU(A, b)
    >>> [ 1.  1.  0.]
    """

    n = len(A)

    # Matriz auxiliar para aplicar Doolitle
    aux = np.zeros((n, n), dtype=float)

    aux[0] = A[0]

    if A[0][0] == 0:
        raise ValueError("No se puede realizar la factorizacion LU")

    for i in range(1, n):  # Calculo de Factores de la primera columna
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

    y = resolver_para_y(L, b)  # type: ignore
    x = resolver_para_x(U, y)

    return x
