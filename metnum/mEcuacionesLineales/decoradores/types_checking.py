def args_types_checking_gauss_seidel(fn):
    def wrapper(*args):

        argumentos = {
            "A": args[0],
            "b": args[1],
            "x0": args[2],
            "tol": (args[3]) if len(args) > 3 else 10**-2,
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


def args_types_checking_gauss_jordan(fn):
    pass


def args_types_checking_gauss_jacobi(fn):
    pass


def args_types_checking_gauss_LU(fn):
    pass
