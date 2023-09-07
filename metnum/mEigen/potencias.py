import numpy as np
from ..decorators import args_types_cheking, args_transform_from_list_to_ndarray


@args_types_cheking
@args_transform_from_list_to_ndarray
def potencias(A: list | np.ndarray, x: list | np.ndarray, tolerancia: float = 10**-12, maxIter: int = 100) -> tuple:
    """
    Calcula el autovalor dominante y el autovector asociado utilizando el método de las potencias.

    Parámetros
    --------------
    A: np.array
        Matriz de entrada para la cual se desea calcular el autovalor dominante y el autovector asociado.
    x: np.array
        Vector inicial utilizado en el proceso iterativo.
    tolerancia: float
        Tolerancia utilizada como criterio de convergencia del método de las potencias.
        El proceso iterativo se detendrá cuando el cambio relativo en el autovalor sea menor o igual que la tolerancia.
    maxIter: int
        Número máximo de iteraciones permitidas antes de detener el proceso iterativo,
        independientemente de si se ha alcanzado o no la tolerancia de convergencia.

    Retorna:
    --------------

    lambda_: float
        El autovalor dominante calculado a partir de la matriz de entrada.
    x: np.array
        El autovector asociado al autovalor dominante.

    Ejemplos:

    >>> potencias([[1, 2], [3, 4]], [1, 1], 1e-6, 100)
    (5.372281323269014, array([0.41597356, 0.90937671]))
    """

    lambdaviejo = 100
    k = 0
    error = 1000
    lambda_ = []
    while k <= maxIter and abs(error) > tolerancia:
        x = np.dot(A, x) / np.linalg.norm(np.dot(A, x))
        lambda_ = np.dot(np.dot(A, x), x) / np.dot(x, x)

        # lambda = (Ax)*x/ (x*x)
        error = abs(lambda_ - lambdaviejo) / lambda_

        lambdaviejo = lambda_
        k = k + 1
    return (lambda_, x)
