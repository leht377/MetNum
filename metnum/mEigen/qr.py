import numpy as np
from .decoradores import qr_args_types_checking,  qr_args_transform_np_array


@qr_args_types_checking
@qr_args_transform_np_array
def qr(A, tolerancia: float = 10 ** -12, maxIter: int = 100):
    """
    Calcula los autovalores de una matriz utilizando el método QR.

    Parámetros
    ------------

    A: np.array
        Matriz de entrada para la cual se desean calcular los autovalores.
    (opcional) tolerancia: float (valor predeterminado: 10 ** -12)
        Tolerancia utilizada como criterio de convergencia del método QR.
        El proceso iterativo se detendrá cuando la norma de la parte triangular inferior
        de la matriz actual sea menor o igual que la tolerancia.
    (opcional) maxIter: int, (valor predeterminado: 100)
        Número máximo de iteraciones permitidas antes de detener el proceso iterativo,
        independientemente de si se ha alcanzado o no la tolerancia de convergencia.

    Retorna
    -----------

    np.array
        Un array que contiene los autovalores calculados a partir de la matriz de entrada.

    Ejemplos
    -----------

    >>> qr([[3, 2, 4],[2, 2, 0],[0, 2, 3]])
    np.array([5.69254381 0.48690755 1.82054864])
    >>> qr([[1, 2], [3, 4]])
    np.array([-0.37228132,  5.37228132])
    """

    Ak = np.array(A)
    i = 0
    error = np.linalg.norm(np.tril(Ak, -1), np.inf)
    # np.tril(Ak, -1) Extrae los elementos que estan por debajo de la diagonal
    while i < maxIter and error > tolerancia:
        (Q, R) = np.linalg.qr(Ak)
        Ak = np.dot(R, Q)
        error = np.linalg.norm(np.tril(Ak, -1), np.inf)
        i += 1
    return np.diag(Ak)
