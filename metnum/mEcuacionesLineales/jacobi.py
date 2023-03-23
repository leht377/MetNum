import numpy as np
from .helpers import es_diagonal_dominante
from .decoradores import jacobi_args_types_checking
# TODO implementer jacobi_args_types_checking

# @jacobi_args_types_checking


def jacobi(
    A,
    b: list,
    x0: list,
    tol: int or float = pow(10, -12),
    maxiter: int = 25,
):
    """
    Esta funcion resuelve sistemas de ecuaciones lineales Ax=b usando el método de jacobi

    Parametros
    ------------
    A: list
        Matriz de coeficiente del sistema de ecuaciones
    b: list
        Vector de terminos independientes
    x0: list
        Vector de aproximacion inicial 
    (opcional) tol: int or float
        Tolerancia maxima con la cual se acepta la soluci+on
    (opcional) maxiter: int
        Numero maximo de iteraciones para encontrar una solución


    Retorna
    ------------
    vectorSolucion: list 
        Vector con la solucion aproximada al sistema de ecuaciones 

    Ejemplos
    ----------

    ejemplo #1

    >>> jacobi([[6, 2, 1], [-1, 8, 2], [1, -1, 6]], [[25], [-6], [23]], [[0], [0], [0]], 10**-12, 25)
    [[4],[-1],[3]]

    ejemplo #2
    >>> jacobi([[3, -0.1, -0.2], [0.1, 7, -0.3], [0.3, -0.2, 10]],[[7.85], [-19.3], [71.4]],[[0], [0], [0]],10**-12, 25 )
    [[3.],[-2.5],[7.]]

    """
    A = np.array(A)
    b = np.array(b)
    x0 = np.array(x0, dtype=float)
    if b.ndim == 1:
        b = b.reshape(b.shape[0], 1)
    if x0.ndim == 1:
        x0 = x0.reshape(x0.shape[0], 1)

    if not (es_diagonal_dominante(A)):
        raise ValueError(
            "La diagonal de la matriz coeficientes A debe de ser dominante")

    # 1. np.diag tiene el siguiente comportamiento si se le pasa solo un vector [..,..,..] este contruira una matriz con estos valores como diagonal
    # y el resto sera 0

    # 2. El segundo comportamiento si se le pasa una matriz extraera solo los elementos de la diagonal

    # Crea una matriz solo con los elementos de la diagonal de la matriz A el resto de las posiciones las llena con 0
    D = np.diag(np.diag(A))
    R = A.copy()
    np.fill_diagonal(R, 0)  # Remplaza la diagonal de la matriz por 0

    mIncognitas = np.array([x0], dtype=float)

    aproxNuevas = [[0], [0], [0]]
    iteracion = 0

    while iteracion < maxiter:
        aproxNuevas = np.dot(np.linalg.inv(
            D), b - np.dot(R, mIncognitas[iteracion]))
        mIncognitas = np.insert(
            mIncognitas, iteracion + 1, aproxNuevas, axis=0)
        iteracion = iteracion + 1

        E = np.linalg.norm(mIncognitas[iteracion] - mIncognitas[iteracion - 1])
        if E < tol:
            break

    vectorSolucion = mIncognitas[iteracion]

    return vectorSolucion
