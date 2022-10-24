

# def biseccion(f, a, b, tol, plot=False) -> object:

#     n = 1
#     c = (a + b) / 2
#     yc = f(c)
#     maxIter = ceil((log(b - a) - log(tol)) / log(2)) - 1
#     ya = f(a)
#     yb = f(b)

#     historyA = np.array([a])
#     historyB = np.array([b])
#     historyC = np.array([c])

#     for n in range(maxIter):

#         if yc == 0:  # La rai­z es c
#             a = c
#             b = c
#             print("Se ha alcanzado el cero exacto \n")
#             break
#         elif yb * yc > 0:  # La rai­z esta en [a,c]
#             b = c
#             yb = yc
#         else:  # La rai­z esta en [c,b]
#             a = c
#             ya = yc

#         c = (a + b) / 2
#         yc = f(c)

#         historyA = np.append(historyA, a)
#         historyB = np.append(historyB, b)
#         historyC = np.append(historyC, c)

#     #plot and biseccionPlot.paintgrafico(f, historyA, historyB, historyC)

#     return {"caprox": c, "err": abs(yc), "numiter": n + 1}


# def args_type_checking(fn):
#     def wrapper(*args):
#         if all(isinstance(arg, (float, int,)) for arg in args):
#             return fn(*args)
#         raise ValueError("Todos los argumentos deben ser enteros o floats")
#     return wrapper


# @args_type_checking
def biseccion(f, intervaloA: int or float, intervaloB: int or float, tolerancia: float or int) -> tuple:
    """
    Esta funcion entrega el valor aproximado de una raíz que esta en la función continua f(x)

    Parametros
    -----------

    f : function
        funcion f(x)
    intervaloA : float or int  
        Primer extremo del intervalo donde se encuentra la raíz [intervaloA , ... ]
    intervaloB : float or int
        Segundo extremo del intervalo donde se encuentra la raíz [..., intervaloB]       
    tolerancia : float or int
        Tolerancia maxima con la cual se acepta la aproximación de la raíz

    Retorna
    -----------

    (aproxNueva, errorRelativo, iteraciones) : tuple

    aproxNueva : float
        Valor aproximado de la raíz
    errorRelativo : float
        Error relativo de la raiz aproximada encontrada 
    iteraciones : int
        Numero de iteracciones necesarias para encontrar la raiz aproximada 

    Ejemplos
    ----------

    ejemplo #1
    >>> biseccion (lambda x : x**2 + 3*x - 34, 3, 5, 10**-6)
    (4.520793914794922, 8.43811360907401e-07, 18)

    ejemplo #2
    >>> biseccion (lambda x : x + exp(2 * x), -1, 0, 10**-6)
    (-0.4263026714324951, 5.592706663094791e-07, 21)
    """

    if (f(intervaloA) * f(intervaloB) > 0):
        raise (
            f'No hay raiz en el intervalo [{intervaloA}, {intervaloB}]')

    aproxNueva = ((intervaloA + intervaloB) / 2)
    errorRelativo = 1000
    iteraciones = 0

    f_de_aproxNueva = f(aproxNueva)
    f_de_intervaloA = f(intervaloA)
    f_de_intervaloB = f(intervaloB)

    while errorRelativo > tolerancia:
        if (f_de_intervaloA * f_de_aproxNueva == 0):  # Se encontro la raíz exacta
            break
        # La raíz  esta en [aproxNueva, intervaloB]
        if (f_de_intervaloB * f_de_aproxNueva < 0):
            intervaloA = aproxNueva
            f_de_intervaloA = f_de_aproxNueva

        # La raíz  esta en [intervaloA, aproxNueva]
        elif (f_de_intervaloB * f_de_aproxNueva > 0):
            intervaloB = aproxNueva
            f_de_intervaloB = f_de_aproxNueva

        aproxAnterior = aproxNueva
        aproxNueva = ((intervaloA + intervaloB) / 2)
        f_de_aproxNueva = f(aproxNueva)
        errorRelativo = abs((aproxNueva - aproxAnterior) / aproxNueva)

        iteraciones += 1

    return aproxNueva, errorRelativo, iteraciones
