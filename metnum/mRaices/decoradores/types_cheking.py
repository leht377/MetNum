def args_type_checking(fn):
    def wrapper(*args):
        # if not isinstance(args[0],)

        argumentos = {
            "intervaloA": args[1],
            "intervaloB": args[2],
            "tolerancia": args[3],
        }

        if not isinstance(argumentos["intervaloA"], (int, float)):
            raise TypeError("Todos los argumentos deben ser enteros o floats")

        if not isinstance(argumentos["intervaloB"], (int, float)):
            raise TypeError("Todos los argumentos deben ser enteros o floats")

        if not isinstance(argumentos["tolerancia"], (int, float)):
            raise TypeError("Todos los argumentos deben ser enteros o floats")

        return fn(*args)

    return wrapper
