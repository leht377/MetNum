import pytest
from numpy import testing
from ...mEcuacionesLineales import LU
from ..helpers import mensaje_error


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
    resultado = LU(A, b)
    assert not testing.assert_allclose(resultado, expected)


@pytest.mark.parametrize(
    "A, b, expected", [
        (
            " [[6, 2, 1], [-1, 8, 2], [1, -1, 6]]",
            [[25], [-6], [23]],
            mensaje_error("A", "list | numpy.ndarray")),
        (
            [[6, 2, 1], [-1, 8, 2], [1, -1, 6]],
            "[[25], [-6], [23]]",
            mensaje_error("b", "list | numpy.ndarray")
        )
    ])
def test_args_types_checking(A, b, expected):
    with pytest.raises(TypeError) as context:
        LU(A, b)
    assert expected in str(context.value)


@pytest.mark.parametrize(
    "A, b, expected", [
        (
            [[0, 2, 1], [-1, 8, 2], [1, -1, 6]],
            [[25], [-6], [23]],
            "No se puede realizar la factorizacion LU"
        )
    ])
def test_error_factorizacion(A, b, expected):
    with pytest.raises(ValueError) as context:
        LU(A, b)
    assert expected in str(context.value)
