from numpy import array


def gaussJordan_args_types_checking(fn):
    def wrapper(*args):
        argumentos = {
            "A": args[0],
            "b": args[1],
        }

        if not isinstance(argumentos["A"], (list)):
            raise TypeError("La matriz A deben ser de tipo list")

        if not isinstance(argumentos["b"], (list)):
            raise TypeError("La matriz b deben ser de tipo list")
        return fn(*args)

    return wrapper


def gaussJordan_args_transform_np_array(fn):
    def wrapper(*args):

        tempList = list(args)
        tempList = [array(arg, dtype=float) if isinstance(
            arg, (list)) else arg for arg in tempList]

        # Verificando shape de algunos args (b,x0) y haciendo reshape
        if tempList[1].ndim == 1:
            tempList[1] = tempList[1].reshape(tempList[1].shape[0], 1)

        argsModified = tuple(tempList)
        return fn(*argsModified)

    return wrapper
