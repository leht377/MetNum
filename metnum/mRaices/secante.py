# def secante(
#     f,
#     aproximacion0: int or float,
#     aproximacion1: int or float,
#     tolerancia: int or float,
#     maximoInteraciones: int or float,
# ) -> tuple:
#     """ """

#     iteraciones = 1
#     dfsuc = aproximacion1 - aproximacion0
#     aproximacionNueva0 = aproximacion0
#     aproximacionNueva1 = aproximacion1

#     f_de_aproximacioNueva0 = f(aproximacionNueva0)
#     f_de_aproximacionNueva1 = f(aproximacionNueva1)

#     while abs(dfsuc) >= tolerancia and iteraciones <= maximoInteraciones:
#         iteraciones = iteraciones + 1
#         dfsuc = (
#             f_de_aproximacionNueva1
#             * (aproximacionNueva1 - aproximacionNueva0)
#             / (f_de_aproximacionNueva1 - f_de_aproximacioNueva0)
#         )
#         aproximacionNueva0 = aproximacionNueva1
#         f_de_aproximacioNueva0 = f_de_aproximacionNueva1
#         aproximacionNueva1 = f_de_aproximacionNueva1 - dfsuc
#         f_de_aproximacionNueva1 = f(aproximacionNueva1)

#     return aproximacionNueva1, abs(f_de_aproximacionNueva1), iteraciones - 1

from .plot import plot_secante


def secante(
    f,
    aproximacion0: int or float,
    aproximacion1: int or float,
    tolerancia: int or float,
    maximoInteraciones: int or float,
    plot: bool = False,
) -> tuple:
    """
    Encuentra una aproximación de la raíz de la función f utilizando el método de la secante.

    Parametros
    ------------
    f: function
       función a la que se busca aproximar la raíz.
    aproximacion0: int or float
                   valor de partida para la aproximación de la raíz.
    aproximacion1: int or float
                   segundo valor de partidapara la aproximación de la raíz
    tolerancia: int or float
                valor mínimo de la función en la raíz que se considera suficiente para detener la búsqueda.
    maximoInteraciones: int or float
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

    >>> secante(lambda x: x**2 - 2, 1, 2, 1e-6, 100, True),
               (1.4142135623730954, 8.881784197001252e-16, 6)



    """

    iteraciones = 1
    dfsuc = aproximacion1 - aproximacion0
    aproximacionNueva0 = aproximacion0
    aproximacionNueva1 = aproximacion1

    f_de_aproximacioNueva0 = f(aproximacionNueva0)
    f_de_aproximacionNueva1 = f(aproximacionNueva1)

    if plot:
        HistorialAproximacion0 = [aproximacionNueva0]
        HistorialAproximacion1 = [aproximacionNueva1]

    while abs(dfsuc) >= tolerancia and iteraciones <= maximoInteraciones:
        iteraciones = iteraciones + 1
        dfsuc = (
            f_de_aproximacionNueva1
            * (aproximacionNueva1 - aproximacionNueva0)
            / (f_de_aproximacionNueva1 - f_de_aproximacioNueva0)
        )
        aproximacionNueva0 = aproximacionNueva1
        f_de_aproximacioNueva0 = f_de_aproximacionNueva1
        aproximacionNueva1 = aproximacionNueva1 - dfsuc
        f_de_aproximacionNueva1 = f(aproximacionNueva1)

        if plot:
            HistorialAproximacion0.append(aproximacionNueva0)
            HistorialAproximacion1.append(aproximacionNueva1)

    plot and plot_secante.grafica(
        f, HistorialAproximacion1, HistorialAproximacion0
    ).pintarGrafica()

    return aproximacionNueva1, abs(f_de_aproximacionNueva1), iteraciones - 1
