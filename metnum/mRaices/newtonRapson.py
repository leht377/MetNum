# feval -> octave = eval -> python

# eval ->  eval(expresion,globales,locales)
# expresión : la cadena analizada y evaluada como una expresión de Python
# globales (opcional) - un diccionario
# locales (opcional)- un objeto de mapeo. El diccionario es el tipo de mapeo estándar y de uso común en Python.


def newtonRapson(f, fdx, x0, tol, maxIter):
    n = 0
    xn = x0

    # fxn = eval("f(x)", {"__builtins__": None}, {"f": f, "x": xn})
    # fdxxn = eval("fdx(x)", {"__builtins__": None}, {"fdx": fdx, "x": xn})

    fxn = f(xn)
    fdxxn = fdx(xn)

    # fxn = f(xn)
    # fdxxn =fdx(xn)

    difsuc = fxn / fdxxn  # Diferencia entre iteraciones sucesivas

    while abs(difsuc) >= tol and n <= maxIter:
        n += 1
        xn = xn - difsuc
        fxn = f(xn)
        fdxxn = fdx(xn)

        # fxn = eval("f(x)", {"__builtins__": None}, {"f": f, "x": xn})
        # fdxxn = eval("fdx(x)", {"__builtins__": None}, {"fdx": fdx, "x": xn})

        difsuc = fxn / fdxxn

    return {"c": xn, "error": abs(fxn), "numiter": n}
