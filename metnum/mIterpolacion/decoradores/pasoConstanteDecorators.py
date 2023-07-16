from functools import wraps
from numpy import ndarray


def pasoConstante_args_types_checking(fn):
    @wraps(fn)
    def wrapper(x, y, xk):

        if not isinstance(x, (list, ndarray)):
            raise TypeError("La variable x deben ser de tipo list o ndarray")
        if not isinstance(y, (list, ndarray)):
            raise TypeError("La variable y debe de ser de tipo list o ndarray")
        if not isinstance(xk, (float, int)):
            raise TypeError("La variable xk debe de ser de tipo float o int")

        return fn(x, y, xk)

    return wrapper


def verificar_rango_inversion(fn):
    @wraps(fn)
    def wrapper(x, y, xk):
        if xk < min(x) or xk > max(x):
            raise ValueError(
                "xk debe estar en el rango de los puntos conocidos")

        if xk >= x[len(x) // 2 - 1]:
            x = x[::-1]
            y = y[::-1]

        return fn(x, y, xk)

    return wrapper
