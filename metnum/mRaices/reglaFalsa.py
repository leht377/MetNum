
def reglaFalsa(f, intervaloA, intervaloB, tolerancia):

    iteraciones = 0

    f_de_intervaloA = f(intervaloA)
    f_de_intervaloB = f(intervaloB)

    aproxNueva = intervaloA + \
        (f_de_intervaloA * (intervaloA - intervaloB) /
         (f_de_intervaloB - f_de_intervaloA))

    f_de_aproxNueva = f(aproxNueva)
    errorRelativo = 1000

    while (errorRelativo >= tolerancia):
        iteraciones += 1

        if f_de_intervaloA * f_de_aproxNueva == 0:
            break

        if f_de_aproxNueva < 0:
            intervaloA = aproxNueva
            f_de_intervaloA = f_de_aproxNueva

        elif f_de_aproxNueva > 0:
            intervaloB = aproxNueva
            f_de_intervaloB = f_de_aproxNueva

        aproxAnterior = aproxNueva
        aproxNueva = intervaloA + \
            (f_de_intervaloA * (intervaloA - intervaloB) /
             (f_de_intervaloB - f_de_intervaloA))

        f_de_aproxNueva = f(aproxNueva)
        errorRelativo = abs((aproxNueva - aproxAnterior) / aproxNueva * 100)

    return {"Raiz aproximada": aproxNueva, "Error": errorRelativo, "Iteraciones": iteraciones}
