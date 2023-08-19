from .plot import plot_secante
from ..decorators import args_types_cheking
from ..helpers import tabulate_output
from typing import Callable


@args_types_cheking
def secante(
    f: Callable,
    x0: int | float,
    x1: int | float,
    tolerancia: int | float = 10**-6,
    maxIter: int = 100,
    plot: bool = False,
    tabulate: bool = False,
) -> tuple:
    """
    Encuentra una aproximación de la raíz de la función f utilizando el método de la secante.

    Parametros
    ------------
    f: function
       función a la que se busca aproximar la raíz.
    x0: int or float
        valor de partida para la aproximación de la raíz.
    x1: int or float
        segundo valor de partida para la aproximación de la raíz
    (Opcional) tolerancia: int or float
        valor mínimo de la función en la raíz que se considera suficiente para detener la búsqueda.
    (Opcional) maxIter: int or float
        Número de interaciones máximas permitidas.
    (Opcional)  plot: bool
       Ver graficamente el metodo de la secante.
    (Opcional)  tabulate: bool
       Ver de forma tabulada todas las iteraciones

    Retorna
    --------
    - la aproximación de la raíz encontrada.
    - el valor de la función en la aproximación de la raíz encontrada.
    - el número de iteraciones realizadas.

     Ejemplo
     ---------

    >>> secante(lambda x: x**2 - 2, 1, 2, 12**-6, 100, False)
    (1.4142135623730954, 8.881784197001252e-16, 6)



    """

    iteraciones = 1

    aproxAnterior = x0
    aproxActual = x1

    f_aproxAnterior = f(aproxAnterior)
    f_aproxActual = f(aproxActual)
    error = abs(x1 - x0)

    historial = {
        "xi+1": [],
        "xi": [],
        "xi-1": [],
        "Error": []
    }

    while error >= tolerancia:
        iteraciones = iteraciones + 1
        nuevaAproximacion = aproxActual - (
            f_aproxActual
            * (aproxActual - aproxAnterior)
            / (f_aproxActual - f_aproxAnterior)
        )
        error = abs(nuevaAproximacion-aproxActual)

        if plot | tabulate:
            historial["xi-1"].append(aproxAnterior)
            historial["xi"].append(aproxActual)
            historial["xi+1"].append(nuevaAproximacion)
            historial["Error"].append(error)
        if iteraciones == maxIter:
            raise ValueError(
                "El método de la secante no convergió después de alcanzar el número máximo de iteraciones.")

        aproxAnterior = aproxActual
        f_aproxAnterior = f_aproxActual
        aproxActual = nuevaAproximacion  # Nueva aproximacion
        f_aproxActual = f(aproxActual)

    if plot:
        plot_secante.grafica(
            f, historial["xi"], historial["xi-1"]).pintarGrafica()
    if tabulate:
        tabulate_output(historial)

    return aproxActual, error, iteraciones - 1
