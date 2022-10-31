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


# import numpy as np
# import matplotlib.pyplot as plt


# plt.figure(figsize=(6, 6))
# x = np.linspace(-5, 5, 100)
# plt.plot(x, x**2, "ko", label="quadratic")
# plt.plot(x, x**3, "r*", label="cubic")
# plt.title(f"Plot of Various Polynomials from {x[0]} to {x[-1]}")
# plt.xlabel("X axis")
# plt.ylabel("Y axis")
# plt.legend(loc=2)
# plt.xlim(-100, 100)
# plt.ylim(-10, 10)
# plt.grid()
# plt.show()
