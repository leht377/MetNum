def args_type_checking(fn):
    def wrapper(*args):

        argumentos = {
            "f(x)": args[0],
            "intervaloA": args[1],
            "intervaloB": args[2],
            "tolerancia": (args[3]) if len(args) > 3 else 10**-6,
            "plot": (args[4]) if len(args) > 4 else False,
        }

        if not callable(argumentos["f(x)"]):
            raise TypeError("El objeto no es invocable")

        if not isinstance(argumentos["intervaloA"], (int, float)):
            raise TypeError("El intervaloA deben ser entero o float")

        if not isinstance(argumentos["intervaloB"], (int, float)):
            raise TypeError("El intervaloB deben ser entero o float")

        if not isinstance(argumentos["tolerancia"], (int, float)):
            raise TypeError("La toleracia deben ser entero o float")

        if not isinstance(argumentos["plot"], (bool)):
            raise TypeError("Plot debe de ser de tipo bool")

        return fn(*args)

    return wrapper


def args_type_checking_secante(fn):
    def wrapper(*args):
        argumentos = {
            "f(x)": args[0],
            "aproximacion0": args[1],
            "aproximacion1": args[2],
            "tolerancia":  (args[3]) if len(args) > 3 else 10**-6,
            "maximoInteraciones":  (args[4]) if len(args) > 4 else 100,
            "plot": (args[5]) if len(args) > 5 else False,
        }

        if not callable(argumentos["f(x)"]):
            raise TypeError("El objeto no es invocable")

        if not isinstance(argumentos["aproximacion0"], (int, float)):
            raise TypeError("La aproximacion0 deben ser entero o float")

        if not isinstance(argumentos["aproximacion1"], (int, float)):
            raise TypeError("La aproximacion1 deben ser entero o float")

        if not isinstance(argumentos["tolerancia"], (int, float)):
            raise TypeError("La toleracia deben ser entero o float")

        if not isinstance(argumentos["maximoInteraciones"], (int, float)):
            raise TypeError("maximoInteraciones deben ser entero o float")

        if not isinstance(argumentos["plot"], (bool)):
            raise TypeError("Plot debe de ser de tipo bool")

        return fn(*args)
    return wrapper


def args_type_checking_newtonRapson(fn):
    def wrapper(*args):
        argumentos = {
            "f(x)": args[0],
            "fDerivadax": args[1],
            "puntoInicial": args[2],
            "tolerancia":  (args[3]) if len(args) > 3 else 10**-6,
            "maximoInteraciones":  (args[4]) if len(args) > 4 else 100,
            "plot": (args[5]) if len(args) > 5 else False,
        }

        if not callable(argumentos["f(x)"]):
            raise TypeError("El objeto no es invocable")

        if not callable(argumentos["fDerivadax"]):
            raise TypeError("El objeto no es invocable")

        if not isinstance(argumentos["puntoInicial"], (int, float)):
            raise TypeError("El pundoInicial deben ser entero o float")

        if not isinstance(argumentos["tolerancia"], (int, float)):
            raise TypeError("La toleracia deben ser entero o float")

        if not isinstance(argumentos["maximoInteraciones"], (int, float)):
            raise TypeError("maximoInteraciones deben ser entero o float")

        if not isinstance(argumentos["plot"], (bool)):
            raise TypeError("Plot debe de ser de tipo bool")

        return fn(*args)
    return wrapper
