import inspect
from functools import wraps


def args_types_cheking(funcion):
    firma = inspect.signature(funcion)
    parametros = firma.parameters

    @wraps(funcion)
    def wrapper(*args, **kwargs):
        # Verificar los tipos de los argumentos posicionales
        for i, arg in enumerate(args):
            nombre_parametro = list(parametros.keys())[i]
            tipo_esperado = parametros[nombre_parametro].annotation

            if tipo_esperado != inspect.Parameter.empty and not isinstance(arg, tipo_esperado):
                raise TypeError(
                    f"El argumento {nombre_parametro} debe ser de tipo {tipo_esperado}")

        # Verificar los tipos de los argumentos con nombre
        for nombre, valor in kwargs.items():
            if nombre in parametros:
                tipo_esperado = parametros[nombre].annotation

                if tipo_esperado != inspect.Parameter.empty and not isinstance(valor, tipo_esperado):
                    raise TypeError(
                        f"El argumento {nombre} debe ser de tipo {tipo_esperado}")

        # Llamar a la función original
        return funcion(*args, **kwargs)

    return wrapper
