from functools import wraps
from numpy import ndarray


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
