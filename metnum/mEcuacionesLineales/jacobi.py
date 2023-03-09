import numpy as np


def jacobi(
    A,
    b: list[float],
    x0: list[float],
    tol: int or float = pow(10, -12),
    maxiter: int = 25,
):
    A = np.array(A)
    b = np.array(b)
    mIncognitas = np.array([x0], dtype=float)
    (fila, col) = A.shape
    normb = np.linalg.norm(b)

    temp = [[0], [0], [0]]
    iteracion = 0

    while (
        np.linalg.norm(np.subtract(np.dot(A, mIncognitas[iteracion]), b)) > tol * normb
    ) and (iteracion < maxiter):
        for k in range(fila):

            temp[k][0] = np.divide(
                b[k]
                - np.dot(np.delete(A[k, :], k), np.delete(mIncognitas[iteracion], k)),
                A[k][k],
            )[0]

        mIncognitas = np.insert(mIncognitas, iteracion + 1, temp, axis=0)
        iteracion = iteracion + 1

    return mIncognitas[iteracion]
