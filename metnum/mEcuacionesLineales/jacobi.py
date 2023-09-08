import numpy as np
from .helpers import es_diagonal_dominante, es_matriz_cuadrada
from ..decorators import transform_np_array, args_types_cheking
from ..helpers import tabulate_output


@args_types_cheking
@transform_np_array
def jacobi(
    A: list | np.ndarray,
    b:  list | np.ndarray,
    x0:  list | np.ndarray,
    tol:  float = 10 ** -12,
    maxiter: int = 25,
    tabulate: bool = False
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
       El vector x que satisface el sistema de ecuaciones lineales Ax = b

    Ejemplos
    ----------

    ejemplo #1

    >>> jacobi([[6, 2, 1], [-1, 8, 2], [1, -1, 6]], [[25], [-6], [23]], [[0], [0], [0]], 10**-12, 25)
    [[4],[-1],[3]]

    ejemplo #2
    >>> jacobi([[3, -0.1, -0.2], [0.1, 7, -0.3], [0.3, -0.2, 10]],[[7.85], [-19.3], [71.4]],[[0], [0], [0]],10**-12, 25 )
    [[3.],[-2.5],[7.]]

    """

    if not (es_matriz_cuadrada(A)):
        raise ValueError("La matriz A debe de ser cuadrada")

    if not (es_diagonal_dominante(A)):
        raise ValueError(
            "La diagonal de la matriz coeficientes A debe de ser dominante")

    # 1. np.diag tiene el siguiente comportamiento si se le pasa solo un vector [..,..,..] este contruira una matriz con estos valores como diagonal
    # y el resto sera 0

    # 2. El segundo comportamiento si se le pasa una matriz extraera solo los elementos de la diagonal

    # Crea una matriz solo con los elementos de la diagonal de la matriz A el resto de las posiciones las llena con 0
    D = np.diag(np.diag(A))
    R = A.copy()

    # Remplaza la diagonal de la matriz por 0
    np.fill_diagonal(R, 0)  # type: ignore

    mIncognitas = np.array([x0], dtype=float)

    aproxNuevas = [[0], [0], [0]]
    iteracion = 0

    historial = {
        "Incognitas": [x0.reshape(-1)],  # type: ignore
        "Error": [None]
    }

    while iteracion < maxiter:
        aproxNuevas = np.dot(np.linalg.inv(
            D), b - np.dot(R, mIncognitas[iteracion]))  # type: ignore
        mIncognitas = np.insert(
            mIncognitas, iteracion + 1, aproxNuevas, axis=0)
        iteracion = iteracion + 1
        E = np.linalg.norm(mIncognitas[iteracion] - mIncognitas[iteracion - 1])

        if tabulate:
            historial["Incognitas"].append(aproxNuevas.reshape(-1))
            historial["Error"].append(E)

        if E < tol:
            break

    vectorSolucion = mIncognitas[iteracion]

    if tabulate:
        tabulate_output(historial)

    return vectorSolucion
