from numpy import array


def qr_args_types_checking(fn):
    def wrapper(*args):
        argumentos = {
            "A": args[0],
            "tolerancia": args[1] if len(args) > 1 else 10**-12,
            "maxIter": args[2] if len(args) > 2 else 25,
        }

        if not isinstance(argumentos["A"], (list)):
            raise TypeError("La matriz A deben ser de tipo list")
        if not isinstance(argumentos["tolerancia"], (float)):
            raise TypeError("La tolerancia debe de ser de tipo float")
        if not isinstance(argumentos["maxIter"], (int)):
            raise TypeError(
                "El numero maximo de iteraciones debe de ser de tipo int")
        return fn(*args)

    return wrapper


def qr_args_transform_np_array(fn):
    def wrapper(*args):

        tempList = list(args)
        tempList = [array(arg, dtype=float) if isinstance(
            arg, (list)) else arg for arg in tempList]

        argsModified = tuple(tempList)
        return fn(*argsModified)

    return wrapper
