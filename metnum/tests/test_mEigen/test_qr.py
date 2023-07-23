import pytest
from ...mEigen import qr
import numpy as np
from ..helpers import mensaje_error


@pytest.mark.parametrize(
    "A, expected", [
        ([[3, 2, 4], [2, 2, 0], [0, 2, 3]], [5.69254381, 0.48690755, 1.82054864]),
        ([[1, 2], [3, 4]], [5.37228132, -0.37228132]),
        ([[1, -3, 3], [3, -5, 3], [6, -6, 4]], [4., - 2., - 2.]),
        ([[2, 0, 0], [1, 0, 1], [0, 0, 0]], [2., 0., 0.])
    ]
)
def test_encontro_autovectores(A, expected):
    result = qr(A)
    assert not np.testing.assert_allclose(result, expected)


def test_soporta_kwargs():
    rest = qr(A=[[3, 2, 4], [2, 2, 0], [0, 2, 3]])
    assert not np.testing.assert_allclose(
        rest, [5.69254381, 0.48690755, 1.82054864])


@pytest.mark.parametrize(
    "A, tolerancia, maxIter, expected", [
        (3, 10 ** -12, 100,
         mensaje_error("A", "list | numpy.ndarray")),
        ([[3, 2, 4], [2, 2, 0]], "10 ** -12", 100,
         mensaje_error("tolerancia", "<class 'float'>")),
        ([[3, 2, 4], [2, 2, 0]], 10 ** -12, "100",
         mensaje_error("maxIter", "<class 'int'>")),
    ]
)
def test_args_types_checking(A, tolerancia, maxIter, expected):
    with pytest.raises(TypeError) as context:
        qr(A, tolerancia, maxIter)
    assert expected in str(context.value)
