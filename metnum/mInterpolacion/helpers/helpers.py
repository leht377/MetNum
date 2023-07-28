import numpy as np


def diferencias(v: list) -> list:
    """
        Calcula las diferencias entre elementos adyacentes en una lista.

        Parámetros:
        - v (list): Una lista de números.

        Valor de retorno:
        - diferencias (list): Una lista que contiene las diferencias entre elementos adyacentes en la lista original.
    """
    return [v[i + 1] - v[i] for i in range(len(v)-1)]


def calculardeltas(y: list) -> list:
    """
        Esta funcion calcula todas las diferencias progresivamente de y (list)       
        hasta que se encuentre una diferencia igual a cero a este proceso se le conoce como 
        tabla de diferencias.

        Parámetros:
        - y (list): Una lista de números.

        Valor de retorno:
        - deltas (list): Una lista que contiene las primeras diferencias en cada iteración.
    """
    maxIter = len(y) - 1
    listadiferencias = []
    for i in range(maxIter):
        if i == 0:
            d = diferencias(y)
            listadiferencias.append(d)
        else:
            d = diferencias(listadiferencias[i-1])
            listadiferencias.append(d)
        if np.allclose(listadiferencias[i], [0]):
            break

    deltas = []

    for i in range(len(listadiferencias)-1):
        deltas.append(listadiferencias[i][0])
    return deltas


def x0_index_finder(x: list, xk: float) -> int:
    diferencias = np.abs(np.array(x) - xk)
    index = np.argmin(diferencias)
    return index
