from numpy import array


def jacobi_args_types_checking(fn):
    def wrapper(*args):

        argumentos = {
            "A": args[0],
            "b": args[1],
            "x0": args[2],
            "tol": (args[3]) if len(args) > 3 else 10**-12,
            "maxiter": (args[4]) if len(args) > 4 else 25,
        }

        if not isinstance(argumentos["A"], (list)):
            raise TypeError("La matriz A deben ser de tipo list")

        if not isinstance(argumentos["b"], (list)):
            raise TypeError("La matriz b deben ser de tipo list")

        if not isinstance(argumentos["x0"], (list)):
            raise TypeError("La x0 A deben ser de tipo list")

        if not isinstance(argumentos["tol"], (int, float)):
            raise TypeError("La tolerancia debe de ser de tipo entero o float")

        if not isinstance(argumentos["maxiter"], (int)):
            raise TypeError(
                "El numero maximo de iteraciones debe de ser de tipo entero"
            )

        return fn(*args)

    return wrapper


def jacobi_args_transform_np_array(fn):
    def wrapper(*args):

        tempList = list(args)
        tempList = [array(arg, dtype=float) if isinstance(
            arg, (list)) else arg for arg in tempList]

        # Verificando shape de algunos args (b,x0) y haciendo reshape
        if tempList[1].ndim == 1:
            tempList[1] = tempList[1].reshape(tempList[1].shape[0], 1)
        if tempList[2].ndim == 1:
            tempList[2] = tempList[2].reshape(tempList[2].shape[0], 1)

        argsModified = tuple(tempList)
        return fn(*argsModified)

    return wrapper
