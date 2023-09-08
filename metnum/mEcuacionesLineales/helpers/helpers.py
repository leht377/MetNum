import numpy as np
from ...decorators import transform_np_array


@transform_np_array
def resolver_para_x(L: np.ndarray, b: np.ndarray) -> np.ndarray:
    """
    Resuelve el sistema de ecuaciones lineales Ux = y utilizando la descomposición LU.

    Parámetros:
    L (np.ndarray): Una matriz triangular inferior de la descomposición LU.
    b (np.ndarray): El vector y en la ecuación Ux = y.

    Devuelve:
    np.ndarray: El vector x que satisface Ux = y.
    """

    # Obtener las dimensiones de la matriz b
    dim, nc = b.shape

    # Crear una matriz x inicializada con ceros del mismo tamaño que b
    x = np.zeros((dim, nc))

    # Recorrer las filas de b desde la última hasta la primera
    for i in range(dim - 1, -1, -1):
        # Calcular la solución para la fila i
        x[i, :] = (b[i, :] - np.dot(L[i, :], x)) / L[i, i]

    return x


@transform_np_array
def resolver_para_y(L: np.ndarray, b: np.ndarray) -> np.ndarray:
    """
    Resuelve un sistema de ecuaciones lineales de la forma Ly = b, donde L es una matriz triangular inferior.

    Parameters:
        L (np.ndarray): Matriz triangular inferior de dimensiones (n, n).
        b (np.ndarray): Vector de términos independientes de dimensiones (n, m).

    Returns:
        np.ndarray: Vector solución 'y' de dimensiones (n, m) que satisface Ly = b.

    """
    # Obtiene las dimensiones de la matriz b (que suele ser U en la descomposición LU)
    dimension, num_columnas = b.shape

    # Inicializa un vector y con ceros de la misma dimensión que b.
    # Este vector y contendrá la solución a la ecuación Ly = b.
    y = np.zeros((dimension, num_columnas))

    # Realiza una iteración sobre las filas de b (L en LU).
    for fila in range(dimension):
        # Calcula el valor de la componente 'fila' del vector y de la siguiente manera:
        # 1. Resta la multiplicación de la fila 'fila' de L por el vector y.
        # 2. Luego, divide el resultado por el elemento diagonal de L en la misma fila ('fila', 'fila').
        y[fila, :] = (b[fila, :] - np.dot(L[fila, :], y)) / L[fila, fila]

    # Devuelve la matriz y, que contiene la solución al sistema Ux = y.
    return y


@transform_np_array
def es_matriz_cuadrada(matriz):
    fila, columna = matriz.shape
    if fila == columna:
        return True
    return False


@transform_np_array
def es_diagonal_dominante(matriz):
    matriz = np.array(matriz)
    fila = matriz.shape[1]

    for i in range(fila):
        if not (np.all(matriz[i][i] > np.absolute(
                np.delete(matriz[i], i, axis=None)))):
            return False
    return True
