from .pasoVariable import pasoVariable


def inversa(x: list, y: list, yk: int or float) -> float:
    """
    Esta funcion realiza la interpolación inversa para encontrar el valor 
    correspondiente de x dado un valor yk.

    Parámetros
    -------------
    x (list): 
        lista de valores conocidos en x de la funcion f(x).
    y (list): 
        lista de valores conocidos en y = f(x) para las variables x.
    yk (float): 
        valor de la variable dependiente para el cual se desea encontrar el valor correspondiente de x.

    Retorna
    -------------
    xk (float): 
        valor correspondiente de x para el valor de la variable dependiente yk.
    """

    xk = pasoVariable(y, x, yk)
    return xk
