import numpy as np

from .decoradores import args_types_checking_gauss_seidel


@args_types_checking_gauss_seidel
def gaussSeidel(
    A: list[float],
    b: list[float],
    x0: list[float],
    tol: int or float = pow(10, -12),
    maxiter: int = 25,
) -> list:
    """
    Esta funcion resuelve sistemas de ecuaciones liniales usando el método numerico
    de Gauss-Seidel

    Paramatros
    -----------

    A: list[float]
        Matriz de coeficiente del sistema de ecuaciones
    b: list[float]
        Vector de terminos independientes
    x0: list[float]
        vector de estimación inicial al sistema de ecuaciones
    (opcional) tol: int or float
        Tolerancia maxima con la cual se acepta la soluci+on
    (opcional) maxiter: int
        Numero maximo de iteraciones para encontrar una solución


    Retorna
    ----------

    x: list
        Matriz con la solucion al sistema de ecuaciones liniales

    Ejemplos
    ----------

    ejemplo #1

    >>> gaussSeidel([[6, 2, 1], [-1, 8, 2], [1, -1, 6]], [[25], [-6], [23]], [[0], [0], [0]],10^-12, 25)
    [[-4],[-1],[3]]

    ejemplo #2
    >>> gaussSeidel([[3, -0.1, -0.2], [0.1, 7, -0.3], [0.3, -0.2, 10]],[[7.85], [-19.3], [71.4]],[[0], [0], [0]] ,10^-12, 25)
    [[3.],[-2.5],[7.]]
    """
    A = np.array(A)
    b = np.array(b)
    x = np.array(x0, dtype=float)

    n = len(A)
    normb = np.linalg.norm(b)
    iter = 0

    while (np.linalg.norm(np.subtract(np.dot(A, x), b)) > tol * normb) and (
        iter < maxiter
    ):
        iter += 1
        for j in range(n):
            resultA = np.concatenate([A[j][0:j], A[j][j + 1: n + 1]])
            resultX = np.concatenate([x[0:j], x[j + 1: n + 1]])

            x[j] = (np.subtract(b[j], np.dot(resultA, resultX))) / A[j][j]

    return x
