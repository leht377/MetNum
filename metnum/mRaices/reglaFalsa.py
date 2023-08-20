from ..decorators import args_types_cheking
from ..helpers import tabulate_output
from .plot import graphReglaFalsa
from typing import Callable


@args_types_cheking
def reglaFalsa(
    f: Callable,
    intervaloA: int | float,
    intervaloB: int | float,
    tolerancia: int | float = 10**-6,
    plot: bool = False,
    tabulate: bool = False
) -> tuple:
    """
    En esta funcion podemos encontrar el valor de la raiz en una funcion F(x)

    Parametros
    ----------
    f: function
    funcion f(x)

    intervaloA: int or float
        Extremo izquierdo del intervalo a evaluar

    intervaloB: int or float
        Extremo derecho del intervalo a evaluar

    tolerancia: int or float
       Tolerancia maxima con la cual se acepta la aproximación de la raíz

    (Opcional)  plot: bool
       Ver graficamente el metodo de biseccion

    (Opcional)  tabulate: bool
       Ver de forma tabulada todas las iteraciones

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
    >>> reglaFalsa (lambda x: math.exp(3 * x) - 4, 0, 1, 10**-6)
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

    historial = {
        "A": [intervaloA],
        "b": [intervaloB],
        "Raiz": [aproxNueva],
        "Error": [None],
    }

    while errorRelativo >= tolerancia:
        iteraciones += 1

        if f_de_intervaloA * f_de_aproxNueva == 0:
            break

        if f_de_intervaloB * f_de_aproxNueva < 0:
            intervaloA = aproxNueva
            f_de_intervaloA = f_de_aproxNueva

        elif f_de_intervaloB * f_de_aproxNueva > 0:
            intervaloB = aproxNueva
            f_de_intervaloB = f_de_aproxNueva

        aproxAnterior = aproxNueva
        aproxNueva = intervaloA + (
            f_de_intervaloA
            * (intervaloA - intervaloB)
            / (f_de_intervaloB - f_de_intervaloA)
        )

        f_de_aproxNueva = f(aproxNueva)
        errorRelativo = abs((aproxNueva - aproxAnterior) / aproxNueva)

        if plot | tabulate:
            historial["A"].append(intervaloA)
            historial["b"].append(intervaloB)
            historial["Raiz"].append(aproxNueva)
            historial["Error"].append(errorRelativo)

    if plot:
        graphReglaFalsa.graph(
            f,  historial["A"],  historial["b"],  historial["Raiz"]).paint()
    if tabulate:
        tabulate_output(historial)

    return aproxNueva, errorRelativo, iteraciones
