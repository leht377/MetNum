def newtonRapson(
    f,
    fDerivadax,
    puntoInicial: int or float,
    toleracia: int or float,
    maximoInteraciones: int or float,
) -> tuple:
    """ """
    interaciones = 0
    aproxNueva = puntoInicial

    f_de_apoxNueva = f(aproxNueva)
    fdx_aproxNueva = fDerivadax(aproxNueva)

    difsuc = f_de_apoxNueva / fdx_aproxNueva

    while abs(difsuc) >= toleracia and interaciones <= maximoInteraciones:
        interaciones += 1
        aproxNueva = aproxNueva - difsuc
        f_de_apoxNueva = f(aproxNueva)
        fdx_aproxNueva = fDerivadax(aproxNueva)

        difsuc = f_de_apoxNueva / fdx_aproxNueva

    return aproxNueva, abs(f_de_apoxNueva), interaciones
