import numpy as np
from .helpers import es_matriz_cuadrada
from .decoradores import gaussJordan_args_transform_np_array

# TODO Realizar verificacion de tipos de datos en parametros


@gaussJordan_args_transform_np_array
def gaussJordan(A: list, b: list):
    """
    Esta funcion resuelve sistemas de ecuaciones lineales Ax=b usando el método de Gauss-Jordan

    Parametros
    -----------
    A: list[float]
        Matriz de coeficiente del sistema de ecuaciones
    b: list[float]
        Vector de terminos independientes

    Retorna
    ---------

    bx: list[float]
          Vector con la solucion aproximada al sistema de ecuaciones Ax=b

    Ejemplo
    ---------

    >>> gaussJordan([[6, 2, 1], [-1, 8, 2], [1, -1, 6]], [[25], [-6], [23]])
    [[4],[-1],[3]]

    >>> gaussJordan([[3, -0.1, -0.2], [0.1, 7, -0.3], [0.3, -0.2, 10]],[[7.85], [-19.3], [71.4]])
    [[3.],[-2.5],[7.]]
    """

    # Convertimos las lista en matrices de numpy

    if not (es_matriz_cuadrada(A)):
        raise ValueError("La matriz A debe de ser cuadrada")

    # Creamos la matriz aumentada
    matrizAumentada = np.concatenate((A, b), axis=1, dtype=float)

    (nFilas, nColumnas) = matrizAumentada.shape

    nFilas = nFilas - 1
    nColumnas = nColumnas - 1

    filaActual = 0
    columnaActual = 0

    while columnaActual < (nColumnas):

        pivote = matrizAumentada[filaActual][columnaActual]
        matrizAumentada[filaActual] = matrizAumentada[filaActual] / pivote

        for i in range(filaActual, nFilas):

            pivote = matrizAumentada[i + 1][columnaActual]
            # Multiplicar toda la fila R1 (o anterior) por el pivote y con el resultado de esta restarla por la fila que se esta operando
            matrizAumentada[i + 1] = matrizAumentada[i + 1] - (
                matrizAumentada[filaActual] * pivote
            )

        filaActual = filaActual + 1
        columnaActual = columnaActual + 1

    Ax = matrizAumentada[:, :nColumnas]
    bx = matrizAumentada[:, nColumnas:]

    while nFilas > 0:
        # Se extrea la lista de las inconitas ya encontradas
        xi = bx[nFilas:]
        # Se multiplica  las incognitas ya encontradas  en las filas para hallar el resto de ellas
        mul = np.dot(Ax[nFilas - 1, nFilas:], xi)

        # Se despeja el resultado para encontra el valor de la incognita xi
        bx[nFilas - 1] = bx[nFilas - 1] + (mul * -1)
        nFilas = nFilas - 1

    return bx
