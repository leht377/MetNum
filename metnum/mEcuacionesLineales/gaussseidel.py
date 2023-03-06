# import numpy as np


# def gaussseidel(A, b, x0, tol=pow(10, -12), maxiter=25):
#     A = np.array(A)
#     b = np.array(b)

#     n = len(A)
#     x = np.array(x0, dtype=float)
#     iter = 0
#     normb = np.linalg.norm(b)

#     while (np.linalg.norm((A * x - b)[:, 0]) > tol * normb) and (iter < maxiter):
#         iter += 1
#         for j in range(3):
#             resultA = np.concatenate([A[j][0:j], A[j][j + 1 : n + 1]])
#             resultX = np.concatenate([x[0:j], x[j + 1 : n + 1]])

#             x[j] = ((b[j] - resultA * resultX) / A[j][j])[0][0]
#     return x


# matrizA = [[6, 2, 1], [-1, 8, 2], [1, -1, 6]]
# matrizB = [[25], [-6], [23]]
# x0 = np.array([[0], [0], [0]])

# print(*gaussseidel(matrizA, matrizB, x0))


# x = np.array([matrizA[0][0:0], matrizA[0][0 + 1 : n + 1]], dtype=list)


# print(np.linalg.norm((matrizA * matrizX - matizB)[:, 0]))


# print(np.array([[1], [2], [3]], ndmin=2))

# print(np.linalg.norm(matizB))


import numpy as np


# norm -> octave = np.linalg.norm -> python libreria numpy
# panda


def gaussSeidel(a, b, x0, tol=pow(10, -12), maxiter=25) -> list:

    a = np.array(a)
    b = np.array(b)
    x = np.array(x0, dtype=float)

    n = len(a)
    normb = np.linalg.norm(b)
    iter = 0

    while (np.linalg.norm(np.subtract(np.dot(a, x), b)) > tol * normb) and (
        iter < maxiter
    ):
        iter += 1
        for j in range(n):
            resultA = np.concatenate([a[j][0:j], a[j][j + 1 : n + 1]])
            resultX = np.concatenate([x[0:j], x[j + 1 : n + 1]])

            x[j] = (np.subtract(b[j], np.dot(resultA, resultX))) / a[j][j]

    return x
