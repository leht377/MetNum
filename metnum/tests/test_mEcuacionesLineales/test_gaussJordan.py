import pytest
from ...mEcuacionesLineales import gaussJordan
import numpy as np


@pytest.mark.parametrize(
    "A, b, expected", [
        ([[6, 2, 1], [-1, 8, 2], [1, -1, 6]],
         [[25], [-6], [23]],
         [[4], [-1], [3]]),
        ([[3, -0.1, -0.2], [0.1, 7, -0.3], [0.3, -0.2, 10]],
         [[7.85], [-19.3], [71.4]],
         [[3.], [-2.5], [7.]])
    ]
)
def test_encontro_incognitas(A, b, expected):
    resultado = gaussJordan(A, b)
    assert not np.testing.assert_allclose(resultado, expected)


@pytest.mark.parametrize(
    "A, b, expected", [
        ([[6, 2, 1], [-1, 8, 2], [1, -1, 6], [1, -1, 6]],
         [[25], [-6], [23]],
         "La matriz A debe de ser cuadrada"),
        ([[3, -0.1, -0.2], [0.1, 7, -0.3], [0.3, -0.2, 10], [1, -1, 6]],
         [[7.85], [-19.3], [71.4]],
         "La matriz A debe de ser cuadrada")
    ]
)
def test_matriz_no_cuadrada(A, b, expected):
    with pytest.raises(ValueError) as context:
        gaussJordan(A, b)
    assert expected in str(context.value)


@pytest.mark.parametrize(
    "A, b, expected", [
        (
            "[[6, 2, 1], [-1, 8, 2], [1, -1, 6]]",
            [[25], [-6], [23]],
            "La matriz A deben ser de tipo list"
        ),
        (
            [[3, -0.1, -0.2], [0.1, 7, -0.3], [0.3, -0.2, 10]],
            " [[7.85], [-19.3], [71.4]]",
            "La matriz b deben ser de tipo list"
        )
    ]
)
def test_args_types_checking(A, b, expected):
    with pytest.raises(TypeError) as context:
        gaussJordan(A, b)
    assert expected in str(context.value)
