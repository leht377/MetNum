from .plot import plot_newtonRapon
from ..decorators import args_types_cheking
from ..helpers import tabulate_output
from typing import Callable


@args_types_cheking
def newtonRapson(
    f: Callable,
    fDerivadax: Callable,
    puntoInicial: int | float,
    toleracia: int | float = 10**-6,
    maximoInteraciones: int = 100,
    plot: bool = False,
    tabulate: bool = False
) -> tuple:
    """
    Esta función implementa el método de Newton-Raphson para encontrar raíces de una función.

    Parametros
    -----------
    f: function
       Funcion a la que se le va a encontra una raíz.
    fderivadax: function
                Derivada de la funcion f.
    puntoInicial: int or float
                  Punto de partida para la busqueda de la raíz.
    toleracia: int or float
               Tolerancia aceptable del error para la raíz.
    maximoInteraciones: int or float
                        Número de iteraciones máximas permitidas.
    (Opcional)  plot: bool
       Ver graficamente el metodo de newtonRapson.
    (Opcional)  tabulate: bool
       Ver de forma tabulada todas las iteraciones

    Retorna
    --------

    Una tupla con la raíz encontrada,
    el valor absoluto del error,
    el número de iteraciones realizadas.

    Ejemplo
    --------
    >>> newtonRapson( lambda x: x**3 - 2 * x + 2,
                  lambda x: 3 * x**2 - 2, -1, 10**-6, 40, True,
    )
     (-1.7692923542973595, 4.340705572758452e-10, 7)

    """
    iteraciones = 0
    aproxNueva = puntoInicial

    f_de_apoxNueva = f(aproxNueva)
    fdx_aproxNueva = fDerivadax(aproxNueva)

    dfsuc = f_de_apoxNueva / fdx_aproxNueva

    historial = {
        "xi": [aproxNueva],
        "Error": [None]
    }

    while abs(dfsuc) >= toleracia:
        iteraciones += 1
        aproxNueva = aproxNueva - dfsuc
        f_de_apoxNueva = f(aproxNueva)
        fdx_aproxNueva = fDerivadax(aproxNueva)

        dfsuc = f_de_apoxNueva / fdx_aproxNueva

        if plot | tabulate:
            historial["xi"].append(aproxNueva)
            historial["Error"].append(dfsuc)

        if iteraciones == maximoInteraciones:
            raise ValueError(
                "El método de la secante no convergió después de alcanzar el número máximo de iteraciones.")

    if plot:
        plot_newtonRapon.grafica(f, historial["xi"]).pintarGrafica()
    if tabulate:
        tabulate_output(historial)

    return aproxNueva, dfsuc, iteraciones
