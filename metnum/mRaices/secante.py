def secante(
    f,
    aproximacion0: int or float,
    aproximacion1: int or float,
    tolerancia: int or float,
    maximoInteraciones: int or float,
) -> tuple:
    """ """

    iteraciones = 1
    difsuc = aproximacion1 - aproximacion0
    aproximacionNueva0 = aproximacion0
    aproximacionNueva1 = aproximacion1

    f_de_aproximacioNueva0 = f(aproximacionNueva0)
    f_de_aproximacionNueva1 = f(aproximacionNueva1)

    while abs(difsuc) >= tolerancia and iteraciones <= maximoInteraciones:
        iteraciones = iteraciones + 1
        difsuc = (
            f_de_aproximacionNueva1
            * (aproximacionNueva1 - aproximacionNueva0)
            / (f_de_aproximacionNueva1 - f_de_aproximacioNueva0)
        )
        aproximacionNueva0 = aproximacionNueva1
        f_de_aproximacioNueva0 = f_de_aproximacionNueva1
        aproximacionNueva1 = f_de_aproximacionNueva1 - difsuc
        f_de_aproximacionNueva1 = f(aproximacionNueva1)

    return aproximacionNueva1, abs(f_de_aproximacionNueva1), iteraciones - 1


# f = lambda x: x**2 + 3 * x - 34
# a = 3
# b = 8
# tol = 10**-6

# print(secante(f, a, b, tol, 21))
