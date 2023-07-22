from numpy import array


def potencias_args_types_checking(fn):
    def wrapper(*args, **kwargs):
        argumentos = {
            "A": args[0],
            "x": args[1],
            "tolerancia": args[2] if len(args) > 2 else 10**-12,
            "maxIter": args[3] if len(args) > 3 else 100,
        }

        if not isinstance(argumentos["A"], (list)):
            raise TypeError("La matriz A deben ser de tipo list")
        if not isinstance(argumentos["x"], (list)):
            raise TypeError("El vector x debe de ser de tipo list")
        if not isinstance(argumentos["tolerancia"], (float)):
            raise TypeError("La tolerancia debe de ser de tipo float")
        if not isinstance(argumentos["maxIter"], (int)):
            raise TypeError(
                "El numero maximo de iteraciones debe de ser de tipo int")
        return fn(*args, **kwargs)

    return wrapper


def potencias_args_transform_np_array(fn):
    def wrapper(*args, **kwargs):

        tempList = list(args)
        tempList = [array(arg, dtype=float) if isinstance(
            arg, (list)) else arg for arg in tempList]

        argsModified = tuple(tempList)
        return fn(*argsModified, **kwargs)

    return wrapper
