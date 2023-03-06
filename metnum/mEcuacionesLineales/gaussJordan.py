import numpy as np


def gaussJordan(A, b):

    # Convertimos las matrices en matrices de numpy
    A = np.array(A)
    b = np.array(b)

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
            # SOLO DIOS SABE QUE HICE AQUI,
            # Multiplicar toda la fila R1 (o anterior) por el pivote y el resultado de esta restarla por la fila que se esta operando
            matrizAumentada[i + 1] = matrizAumentada[i + 1] - (
                matrizAumentada[filaActual] * pivote
            )

        filaActual = filaActual + 1
        columnaActual = columnaActual + 1

    A = matrizAumentada[:, :nColumnas]
    b = matrizAumentada[:, nColumnas:]

    while nFilas > 0:
        # Se extrea la lista de las inconitas ya encontradas
        xi = b[nFilas:]
        # Se multiplica  las incognitas ya encontradas  en las filas para allar el resto de ellas
        mul = np.dot(A[nFilas - 1, nFilas:], xi)

        # Se despeja el resultado para encontra el valor de la incognita xi
        b[nFilas - 1] = b[nFilas - 1] + (mul * -1)
        nFilas = nFilas - 1

    return b


# A = [[3, -0.1, -0.2], [0.1, 7, -0.3], [0.3, -0.2, 10]]
# b = [[7.85], [-19.3], [71.4]]
# print(gaussJordan(A, b))
