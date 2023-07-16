def pasoVariable(x: list, y: list, xk: int or float) -> float:
    """
    Esta función encuentra el valor en y a un xk x dado como parametro
    usando el método de Lagrange con paso variable 

    Parámetros
    -----------
    x (list): 
      lista de valores conocidos en x de la funcion f(x).
    y (list): 
      lista de valores conocidos en y = f(x) para las variables x.
    xk (int or float): 
      Valor de x para el cual se desea interpolar.

    Retorna
    ----------
    xk (float): 
      valor dependiente de yk para el valor de la variable xk.

    Ejemplo
    ----------

    >>> pasoVariable([0, 1, 2, 5], [5, 7, 9, 15], 3)
    11.0
    >>> pasoVariable([-6, -4, -2, 0, 2, 4], [2245, 361, -3, 1, -11, 345], -3)
    79.0
    >>> pasoVariable([-6, -5, -2, 1], [2245, 1011, -3, -5], -3)
    30.809523809523792
    """

    n = len(x)
    yk = 0.0

    for i in range(n):
        lagrange = y[i]
        for j in range(n):
            if i != j:
                lagrange *= (xk - x[j]) / (x[i] - x[j])
        yk += lagrange
    return yk
