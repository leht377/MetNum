from metnum import biseccion, reglaFalsa, newtonRapson, secante
import matplotlib.pyplot as plt
import math


print(
    "BISECCION: ",
    biseccion(lambda x: -1 * x**3 + 3 * x - 4, -3, -1.5, 10**-6, True),
)
print(
    "REGLA FALSA: ",
    reglaFalsa(lambda x: -1 * x**3 + 3 * x - 4, -3, -1.5, 10**-6, True),
)
print(
    "NEWTON RAPSON: ",
    newtonRapson(
        lambda x: -1 * x**3 + 3 * x - 4,
        lambda x: -3 * x**2 + 3,
        -1.5,
        10**-6,
        20,
        True,
    ),
)
# print(
#     "REGLA FALSA: ",
#     reglaFalsa(lambda x: x**3 - 1 * x - 1, 1, 1.8, 10**-6, True),
# )
# print(
#     "NEWTON RAPSON: ",
#     newtonRapson(
#         lambda x: x**7 - 4 * x**4 - x,
#         lambda x: 7 * x**6 - 16 * x**3,
#         4,
#         10**-6,
#         20,
#         True,
#     ),
# )
# print("SECANTE: ", secante(f, x0, x1, tolerancia, maxIteraciones))
