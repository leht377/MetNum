
from numpy import array, ndarray


def qr_args_types_checking(fn):
    def wrapper(*args, **kwargs):
        argumentos = {
            "A": kwargs.get("A", args[0]),
            "tolerancia": kwargs.get("tolerancia", args[1] if len(args) > 1 else 10**-12),
            "maxIter": kwargs.get("maxIter", args[2] if len(args) > 2 else 25),
        }
        argumentos.update(kwargs)

        if not isinstance(argumentos["A"], (list, ndarray)):
            raise TypeError("El argumento A deben ser de tipo list o ndarray")
        if not isinstance(argumentos["tolerancia"], (float)):
            raise TypeError("La tolerancia debe de ser de tipo float")
        if not isinstance(argumentos["maxIter"], (int)):
            raise TypeError(
                "El numero maximo de iteraciones debe de ser de tipo int")
        return fn(*args, **kwargs)

    return wrapper


def qr_args_transform_np_array(fn):
    def wrapper(*args, **kwargs):

        tempList = list(args)
        tempList = [array(arg, dtype=float) if isinstance(
            arg, (list)) else arg for arg in tempList]

        argsModified = tuple(tempList)
        return fn(*argsModified, **kwargs)

    return wrapper
