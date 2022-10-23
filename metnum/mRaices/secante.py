def secante(f, x0, x1, tol, maxIter) -> object:
    n = 1
    difsuc = x1 - x0
    xnmenos = x0
    xn = x1

    fxnmenos = f(xnmenos)
    fxn = f(xn)

    while abs(difsuc) >= tol and n <= maxIter:
        n = n + 1
        difsuc = fxn * (xn - xnmenos) / (fxn - fxnmenos)
        xnmenos = xn
        fxnmenos = fxn
        xn = xn - difsuc
        fxn = f(xn)

    return {"caprox": xn, "err": abs(fxn), "numiter": n - 1}


# f = lambda x: x**2 + 3 * x - 34
# a = 3
# b = 8
# tol = 10**-6

# print(secante(f, a, b, tol, 21))
