# def secante(
#     f,
#     aproximacion0: int or float,
#     aproximacion1: int or float,
#     tolerancia: int or float,
#     maximoInteraciones: int or float,
# ) -> tuple:
#     """ """

#     iteraciones = 1
#     difsuc = aproximacion1 - aproximacion0
#     aproximacionNueva0 = aproximacion0
#     aproximacionNueva1 = aproximacion1

#     f_de_aproximacioNueva0 = f(aproximacionNueva0)
#     f_de_aproximacionNueva1 = f(aproximacionNueva1)

#     while abs(difsuc) >= tolerancia and iteraciones <= maximoInteraciones:
#         iteraciones = iteraciones + 1
#         difsuc = (
#             f_de_aproximacionNueva1
#             * (aproximacionNueva1 - aproximacionNueva0)
#             / (f_de_aproximacionNueva1 - f_de_aproximacioNueva0)
#         )
#         aproximacionNueva0 = aproximacionNueva1
#         f_de_aproximacioNueva0 = f_de_aproximacionNueva1
#         aproximacionNueva1 = f_de_aproximacionNueva1 - difsuc
#         f_de_aproximacionNueva1 = f(aproximacionNueva1)

#     return aproximacionNueva1, abs(f_de_aproximacionNueva1), iteraciones - 1

from .plot import plot_secante


def secante(f, x0, x1, tol, maxIter, plot) -> object:
    n = 1
    difsuc = x1 - x0
    xnmenos = x0
    xn = x1

    fxnmenos = f(xnmenos)
    fxn = f(xn)

    if plot:
        historialXmenos = [xnmenos]
        historialXn = [xn]

    while abs(difsuc) >= tol and n <= maxIter:
        n = n + 1
        difsuc = fxn * (xn - xnmenos) / (fxn - fxnmenos)
        xnmenos = xn
        fxnmenos = fxn
        xn = xn - difsuc
        fxn = f(xn)

        if plot:
            historialXmenos.append(xnmenos)
            historialXn.append(xn)

    plot and plot_secante.grafica(f, historialXn, historialXmenos).pintarGrafica()

    return {"caprox": xn, "err": abs(fxn), "numiter": n - 1}
