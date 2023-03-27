from .decoradores import args_type_checking
from .plot import plot_reglaFalsa


@args_type_checking
def reglaFalsa(
    f,
    intervaloA: int or float,
    intervaloB: int or float,
    tolerancia: int or float = 10**-6,
    plot: bool = False,
) -> tuple:
    """
    En esta funcion podemos encontrar el valor de la raiz en una funcion F(x)

    Parametros
    ----------
    f: function
    funcion f(x)

    intervaloA: int or float
        primer intervalo a evaluar

    intervaloB: int or float
       Segundo intervalo a evaluar

    tolerancia: int or float
       Tolerancia maxima con la cual se acepta la aproximación de la raíz

    (Opcional)  plot: bool
       Ver graficamente el metodo de biseccion

    retorna
    ----------

    (aproxNueva, errorRelativo, iteraciones) : tuple

    aproxNueva : float
        Valor aproximado de la raíz
    errorRelativo : float
        Error relativo de la raiz aproximada encontrada
    iteraciones : int
        Numero de iteracciones necesarias para encontrar la raiz aproximada


    ejemplo:
    --------
    >>> regla falsa (lambda x: math.exp(3 * x) - 4, 0, 1, 10**-6)
    (0.46209811446609667, 8.567878429991425e-07, 35)
    """
    iteraciones = 0

    f_de_intervaloA = f(intervaloA)
    f_de_intervaloB = f(intervaloB)

    aproxNueva = intervaloA + (
        f_de_intervaloA
        * (intervaloA - intervaloB)
        / (f_de_intervaloB - f_de_intervaloA)
    )

    f_de_aproxNueva = f(aproxNueva)
    errorRelativo = 1000

    if plot:
        historial_A = [intervaloA]
        historial_B = [intervaloB]
        historial_Raiz = [aproxNueva]

    while errorRelativo >= tolerancia:
        iteraciones += 1

        if f_de_intervaloA * f_de_aproxNueva == 0:
            break

        if f_de_aproxNueva < 0:
            intervaloA = aproxNueva
            f_de_intervaloA = f_de_aproxNueva

        elif f_de_aproxNueva > 0:
            intervaloB = aproxNueva
            f_de_intervaloB = f_de_aproxNueva

        aproxAnterior = aproxNueva
        aproxNueva = intervaloA + (
            f_de_intervaloA
            * (intervaloA - intervaloB)
            / (f_de_intervaloB - f_de_intervaloA)
        )

        f_de_aproxNueva = f(aproxNueva)
        errorRelativo = abs((aproxNueva - aproxAnterior) / aproxNueva * 100)

        if plot:
            historial_A.append(intervaloA)
            historial_B.append(intervaloB)
            historial_Raiz.append(aproxNueva)

    # if plot:
    #     plot_reglaFalsa.paint_plot(f, historial_A, historial_B, historial_Raiz)

    plot and plot_reglaFalsa.grafica(
        f, historial_A, historial_B, historial_Raiz
    ).pintarGrafica()

    return aproxNueva, errorRelativo, iteraciones
