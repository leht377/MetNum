from metnum import biseccion, reglaFalsa, newtonRapson, secante
import matplotlib.pyplot as plt
import math

# print(
#     "BISECCION: ",
#     biseccion(lambda x: -1 * x**3 + 3 * x - 4, -3, -1.5, 10**-6, True),
# )

# print(
#     "REGLA FALSA: ",
#     reglaFalsa(lambda x: -1 * x**3 + 3 * x - 4, -3, -1.5, 10**-6, True),
# )
# print(
#     "NEWTON RAPSON: ",
#     newtonRapson(
#         lambda x: x**3 - 2 * x + 2,
#         lambda x: 3 * x**2 - 2,
#         0,
#         10**-6,
#         40,
#         True,
#     ),
# )
# secante(lambda x: x**3 - x**2, 1, 0, 10**-6, 50, True), PROBLEMA DIVISION CON CERO
# print(
#     "SECANTE: ",
#     secante(lambda x: x**3 - x**2, 4, 8, 10**-6, 50, True),
# )
