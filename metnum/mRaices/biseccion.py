
from .plot import plot_biseccion_manual, plot_biseccion
from ..decorators import args_types_cheking
from typing import Callable
from ..helpers import tabulate_output


@args_types_cheking
def biseccion(
    f: Callable,
    intervaloA: int | float,
    intervaloB: int | float,
    tolerancia: float | int = 10**-6,
    plot: bool = False,
    tabulate: bool = False
) -> tuple:
    """
    Esta funcion entrega el valor aproximado de una raíz que esta en la función continua f(x)
    usando el método de biseccion

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
    (Opcional)  plot: bool
       Ver graficamente el metodo de biseccion

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

    if f(intervaloA) * f(intervaloB) > 0:
        raise ValueError(
            f"No hay raiz en el intervalo [{intervaloA}, {intervaloB}]")

    aproxNueva = (intervaloA + intervaloB) / 2
    errorRelativo = 1000
    iteraciones = 0

    f_de_aproxNueva = f(aproxNueva)
    f_de_intervaloA = f(intervaloA)
    f_de_intervaloB = f(intervaloB)

    historial = {
        "A": [intervaloA],
        "b": [intervaloB],
        "Raiz": [aproxNueva],
        "Error": [None]
    }

    while errorRelativo > tolerancia:
        iteraciones += 1
        if f_de_intervaloA * f_de_aproxNueva == 0:  # Se encontro la raíz exacta
            errorRelativo = 0
            break
        # La raíz  esta en [aproxNueva, intervaloB]
        if f_de_intervaloB * f_de_aproxNueva < 0:
            intervaloA = aproxNueva
            f_de_intervaloA = f_de_aproxNueva

        # La raíz  esta en [intervaloA, aproxNueva]
        elif f_de_intervaloB * f_de_aproxNueva > 0:
            intervaloB = aproxNueva
            f_de_intervaloB = f_de_aproxNueva

        aproxAnterior = aproxNueva
        aproxNueva = (intervaloA + intervaloB) / 2
        f_de_aproxNueva = f(aproxNueva)
        errorRelativo = abs((aproxNueva - aproxAnterior) / aproxNueva)

        if plot | tabulate:
            historial["A"].append(intervaloA)
            historial["b"].append(intervaloB)
            historial["Raiz"].append(aproxNueva)
            historial["Error"].append(errorRelativo)

    if plot:
        plot_biseccion_manual.grafica(
            f, historial["A"],  historial["b"], historial["Raiz"]).pintarGrafica()
    if tabulate:
        tabulate_output(historial)

    return aproxNueva, errorRelativo, iteraciones
