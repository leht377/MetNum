from .plot import plot_newtonRapon
from .decoradores import args_type_checking_newtonRapson


@args_type_checking_newtonRapson
def newtonRapson(
    f,
    fDerivadax,
    puntoInicial: int | float,
    toleracia: int | float = 10**-6,
    maximoInteraciones: int = 100,
    plot: bool = False,
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
                        Número de interaciones máximas permitidas.
    (Opcional)  plot: bool
       Ver graficamente el metodo de newtonRapson.

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
    interaciones = 0
    aproxNueva = puntoInicial

    f_de_apoxNueva = f(aproxNueva)
    fdx_aproxNueva = fDerivadax(aproxNueva)

    dfsuc = f_de_apoxNueva / fdx_aproxNueva

    if plot:
        historialRaiz = [aproxNueva]

    while abs(dfsuc) >= toleracia and interaciones <= maximoInteraciones:
        interaciones += 1
        aproxNueva = aproxNueva - dfsuc
        f_de_apoxNueva = f(aproxNueva)
        fdx_aproxNueva = fDerivadax(aproxNueva)

        dfsuc = f_de_apoxNueva / fdx_aproxNueva

        plot and historialRaiz.append(aproxNueva)

    plot and plot_newtonRapon.grafica(f, historialRaiz).pintarGrafica()
    # plot and plot_newtonRapon.paint_plot(f, historialRaiz)

    return aproxNueva, abs(f_de_apoxNueva), interaciones
