import math
import matplotlib.pyplot as plt
import numpy as np
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
print(biseccion(lambda x: x**2 + 3*x - 34, 3, 5, 10**-6, True))
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

# A = [[-3, 3, 2],
#      [4, 1, -1],
#      [1, -2, 1]
#     ]


# b = [
#     [1],
#     [2],
#      [3]]
# x0 = [[0], [0], [0]]

# A = [[6, 2, 1], [-1, 8, 2], [1, -1, 6]]
# b = [[25], [-6], [23]]

# A = [[3, 2, -1], [2, -2, 4], [-1, 0.5, -1]]
# b = [[1], [-2], [0]]

# A = [[-3, 3, 2], [4, 1, -1], [1, -2, 1]]
# b = np.array([[1], [2], [3]])

# print(gaussSeidel([[3, -0.1, -0.2], [0.1, 7, -0.3], [0.3, -0.2, 10]],
#       [7.85, -19.3, 71.4], [0, 0, 0]))


# def comprobacion(A, b, res):
#     vectorInconitasResueltas = np.sum(
#         (A * res), axis=1).reshape((3, 1))
#     return np.allclose(vectorInconitasResueltas, b)
