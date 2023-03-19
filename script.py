import math
import matplotlib.pyplot as plt
from metnum import (
    biseccion,
    reglaFalsa,
    newtonRapson,
    secante,
    gaussJordan,
    jacobi,
    LU,
    gaussSeidel
)


# Creamos una lista de resultados
resultados = [[3, 5, 6, 7]]

# Imprimimos la lista en forma de tabla


# A = [
#     [2, -1, 4, 1, -1],
#     [-1, 3, -2, -1, 2],
#     [5, 1, 3, -4, 1],
#     [3, -2, -2, -2, -3],
#     [-4, -1, -5, 3, -4],
# ]
# b = [[7], [1], [33], [24], [-49]]
# print(
#     gaussSeidel(
#         [[6, 2, 1], [-1, 8, 2], [1, -1, 6]], [[25], [-6], [23]], [[0], [0], [0]]
#     )
# )


# print(gaussJordan(A, b))

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

A = [[10, 2, -3], [4, 7, -1], [-2, 1, 4]]
b = [[1], [-1], [5]]
x0 = [[0], [0], [0]]
resultado = jacobi(A, b, x0)
print(jacobi([[6, 2, 1], [-1, 8, 2], [1, -1, 6]],
      [[25], [-6], [23]], [[0], [0], [0]], 10 ^ -12, 25))
print(gaussSeidel([[3, -0.1, -0.2], [0.1, 7, -0.3],
      [0.3, -0.2, 10]], [[7.85], [-19.3], [71.4]], [[0], [0], [0]]))


# print(
#     tabulate(
#         resultado,
#         headers=[
#             "#iter",
#             "x",
#             "y",
#             "z",
#         ],
#         tablefmt="orgtbl",
#         showindex="always",
#     )
# )
