def reglaFalsa(f, a, b, tol):
    n = 0
    yA = f(a)
    yB = f(b)
    xi = a + (yA * (a - b) / (yB - yA))
    dif = xi * 100
    yi = f(xi)

    while abs(dif) > tol:
        n += 1
        if yi == 0:
            print("Se ha alcanzado el cero exacto \n")
        elif yB * yi > 0:  # La raÃ­z estÃ¡ en [a,c]
            b = xi
            yB = yi
        else:  # La raÃ­z estÃ¡ en [c,b]
            a = xi
            yA = yi

        xAnterior = xi
        xi = a + (yA * (a - b) / (yB - yA))
        yi = f(xi)
        dif = (xi - xAnterior) / xi * 100

    return {"caprox": xi, "err": abs(dif), "numiter": n}


f = lambda x: x**2 + 3 * x - 34
a = 3
b = 5
tol = 10**-2


print(reglaFalsa(f, a, b, tol))
