import pytest
from numpy import testing
from metnum import jacobi
# TODO test args_types


@pytest.mark.parametrize(
    "A, b, x0, expected", [
        ([[6, 2, 1], [-1, 8, 2], [1, -1, 6]],
         [[25], [-6], [23]],
         [[0], [0], [0]],
         [[4], [-1], [3]]),
        ([[3, -0.1, -0.2], [0.1, 7, -0.3], [0.3, -0.2, 10]],
         [[7.85], [-19.3], [71.4]],
         [[0], [0], [0]],
         [[3.], [-2.5], [7.]])
    ]
)
def test_encontro_incognitas(A, b, x0, expected):
    resultado = jacobi(A, b, x0, 10**-12, 25)
    assert not testing.assert_allclose(resultado, expected)


@pytest.mark.parametrize(
    "A, b, x0, expected", [
        ([[6, 2, 1], [-1, 8, 2], [1, -1, 6], [1, -1, 6]],
         [[25], [-6], [23]],
         [[0], [0], [0]],
         "La matriz A debe de ser cuadrada"),
        ([[3, -0.1, -0.2], [0.1, 7, -0.3], [0.3, -0.2, 10], [1, -1, 6]],
         [[7.85], [-19.3], [71.4]],
         [[0], [0], [0]],
         "La matriz A debe de ser cuadrada")
    ]
)
def test_matriz_no_cuadrada(A, b, x0, expected):
    with pytest.raises(ValueError) as context:
        jacobi(A, b, x0)
    assert expected in str(context.value)


@pytest.mark.parametrize(
    "A, b, x0, expected", [
        ([[6, 2, 1], [-1, 0, 2], [1, -1, 6]],
         [[25], [-6], [23]],
         [[0], [0], [0]],
         "La diagonal de la matriz coeficientes A debe de ser dominante"),
        ([[3, -0.1, -0.2], [0.1, 0, -0.3], [0.3, -0.2, 10]],
         [[7.85], [-19.3], [71.4]],
         [[0], [0], [0]],
         "La diagonal de la matriz coeficientes A debe de ser dominante")
    ]
)
def test_matriz_diagonal_dominantes(A, b, x0, expected):
    with pytest.raises(ValueError) as context:
        jacobi(A, b, x0)
    assert expected in str(context.value)
