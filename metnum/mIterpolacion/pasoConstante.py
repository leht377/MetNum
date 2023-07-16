
from math import factorial
from .helpers import x0_index_finder, calculardeltas
from .decoradores import pasoConstante_args_types_checking, verificar_rango_inversion
from numpy import ndarray


@pasoConstante_args_types_checking
@verificar_rango_inversion
def pasoConstante(x: list or ndarray, y: list or ndarray, xk: float or int) -> tuple:
    """
    Realiza una interpolación con paso constante para encontrar el valor correspondiente de yk dado un valor xk.

    Parámetros
    ------------
    x (list or ndarray): 
       Lista de valores conocidos en x de la funcion f(x).
    y (list or ndarray ): 
       Lista de valores conocidos en y = f(x) para las variables x.
    xk (float or int): 
        Valor de la variable independiente para el cual se desea encontrar el valor correspondiente de y.

    Retorna
    ------------
    yk (float):
        Valor correspondiente de y para el valor de la variable independiente xk.
    deltas_y (list):
        lista de primeras diferencias de y para el valor independite xk


    Ejemplos 
    -----------
    >>> pasoConstante([2, 4, 6, 8, 10],[8, 26, 52, 86, 128], 3)
    (16.0,[18, 8])
    >>> pasoConstante([2, 4, 6, 8, 10],[8, 26, 52, 86, 128], 7)
    (68.0,[-34, 8])
    >>> pasoConstante([10, 20, 30, 40, 50, 60],[128, 458, 988, 1718, 2648, 3778], 12)
    (178.0,[330, 200])

    """

    indexInicio = x0_index_finder(x, xk)
    indexInicio = indexInicio-1 if indexInicio > 1 else indexInicio

    x = x[indexInicio:]
    y = y[indexInicio:]

    x0 = x[0]
    y0 = y[0]

    h = x[1] - x[0]  # tamaño del paso
    k = (xk - x0) / h

    deltas_y = calculardeltas(y)

    yk = y0 + k * deltas_y[0]

    for i in range(1, len(deltas_y)):
        combinatoria = 1
        for j in range(i):
            combinatoria *= k - (j + 1)
        yk += (combinatoria * k / factorial(i+1)) * deltas_y[i]

    return yk, deltas_y
