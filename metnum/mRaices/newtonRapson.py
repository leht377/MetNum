from .plot import plot_newtonRapon


def newtonRapson(
    f,
    fDerivadax,
    puntoInicial: int or float,
    toleracia: int or float,
    maximoInteraciones: int or float,
    plot: bool = False,
) -> tuple:
    """ """
    interaciones = 0
    aproxNueva = puntoInicial

    f_de_apoxNueva = f(aproxNueva)
    fdx_aproxNueva = fDerivadax(aproxNueva)

    difsuc = f_de_apoxNueva / fdx_aproxNueva

    if plot:
        historialRaiz = [aproxNueva]

    while abs(difsuc) >= toleracia and interaciones <= maximoInteraciones:
        interaciones += 1
        aproxNueva = aproxNueva - difsuc
        f_de_apoxNueva = f(aproxNueva)
        fdx_aproxNueva = fDerivadax(aproxNueva)

        difsuc = f_de_apoxNueva / fdx_aproxNueva

        plot and historialRaiz.append(aproxNueva)

    plot and plot_newtonRapon.grafica(f, historialRaiz).pintarGrafica()
    # plot and plot_newtonRapon.paint_plot(f, historialRaiz)

    return aproxNueva, abs(f_de_apoxNueva), interaciones
