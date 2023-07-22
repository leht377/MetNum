from .plot import plot_secante
from ..decorators import args_types_cheking
from typing import Callable


@args_types_cheking
def secante(
    f: Callable,
    x0: int | float,
    x1: int | float,
    tolerancia: int | float = 10**-6,
    maxIter: int = 100,
    plot: bool = False,
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
    dfsuc = x1 - x0  # Diferencia sucesiva entre las dos aproximaciones
    aproxAnterior = x0
    aproxActual = x1

    f_aproxAnterior = f(aproxAnterior)
    f_aproxActual = f(aproxActual)

    if plot:
        h_aproxAnterior = [aproxAnterior]
        h_aproxActual = [aproxActual]

    while abs(dfsuc) >= tolerancia and iteraciones <= maxIter:
        iteraciones = iteraciones + 1
        dfsuc = (  # Diferencia sucesiva entre las dos aproximaciones
            f_aproxActual
            * (aproxActual - aproxAnterior)
            / (f_aproxActual - f_aproxAnterior)
        )

        aproxAnterior = aproxActual
        f_aproxAnterior = f_aproxActual
        aproxActual = aproxActual - dfsuc  # Nueva aproximacion
        f_aproxActual = f(aproxActual)

        if plot:
            h_aproxAnterior.append(aproxAnterior)
            h_aproxActual.append(aproxActual)

    plot and plot_secante.grafica(
        f, h_aproxActual, h_aproxAnterior).pintarGrafica()

    return aproxActual, abs(f_aproxActual), iteraciones - 1
