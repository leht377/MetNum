import numpy as np

from ..decorators import args_types_cheking, transform_np_array
from .helpers import es_diagonal_dominante, es_matriz_cuadrada


@args_types_cheking
@transform_np_array
def gaussSeidel(
    A: list | np.ndarray,
    b: list | np.ndarray,
    x0: list | np.ndarray,
    tol: float = pow(10, -12),
    maxiter: int = 25,
) -> list | np.ndarray:
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

    x0: list
        Matriz con la solucion al sistema de ecuaciones liniales

    Ejemplos
    ----------

    ejemplo #1

    >>> gaussSeidel([[6, 2, 1], [-1, 8, 2], [1, -1, 6]], [[25], [-6], [23]], [[0], [0], [0]],10**-12, 25)
    [[-4],[-1],[3]]

    ejemplo #2
    >>> gaussSeidel([[3, -0.1, -0.2], [0.1, 7, -0.3], [0.3, -0.2, 10]],[[7.85], [-19.3], [71.4]],[[0], [0], [0]] ,10**-12, 25)
    [[3.],[-2.5],[7.]]
    """
    if not (es_matriz_cuadrada(A)):
        raise ValueError("La matriz A debe de ser cuadrada")

    if not (es_diagonal_dominante(A)):
        raise ValueError(
            "La diagonal de la matriz coeficientes A debe de ser dominante")

    n = len(A)
    normb = np.linalg.norm(b)
    iter = 0

    while (np.linalg.norm(np.subtract(np.dot(A, x0), b)) > tol * normb) and (
        iter < maxiter
    ):
        iter += 1
        for j in range(n):
            resultA = np.concatenate([A[j][0:j], A[j][j + 1: n + 1]])
            resultX = np.concatenate([x0[0:j], x0[j + 1: n + 1]])

            x0[j] = (np.subtract(b[j], np.dot(resultA, resultX))) / A[j][j]

    return x0
