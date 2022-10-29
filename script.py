from metnum import biseccion, reglaFalsa, newtonRapson, secante

f = lambda x: x**2 + 53 * x + 5
tolerancia = 10**-8
intervaloA = -1
intervaloB = 1

fdx = lambda x: 2 * x + 53
x0 = -1
x1 = 1
maxIteraciones = 40
print("BISECCION: ", biseccion(f, intervaloA, intervaloB, tolerancia))
print("REGLA FALSA: ", reglaFalsa(f, intervaloA, intervaloB, tolerancia))
print(
    "NEWTON RAPSON: ",
    newtonRapson(f, fdx, x0, tolerancia, maxIteraciones),
)
print("SECANTE: ", secante(f, x0, x1, tolerancia, maxIteraciones))

# print(mRaices.reglaFalsa(lambda x: math.exp(3 * x) - 4, 0, 1, 10**-6))
