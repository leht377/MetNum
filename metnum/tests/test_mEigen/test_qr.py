import pytest
from ...mEigen import qr
import numpy as np


@pytest.mark.parametrize(
    "A, expected", [
        ([[3, 2, 4], [2, 2, 0], [0, 2, 3]], [5.69254381, 0.48690755, 1.82054864]),
        ([[1, 2], [3, 4]], [5.37228132, -0.37228132])
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
        (3, 10 ** -12, 100, "El argumento A debe ser de tipo"),
        ([[3, 2, 4], [2, 2, 0]], "10 ** -12", 100,
         "El argumento tolerancia debe ser de tipo"),
        ([[3, 2, 4], [2, 2, 0]], 10 ** -12, "100",
         "El argumento maxIter debe ser de tipo "),
    ]
)
def test_args_types_checking(A, tolerancia, maxIter, expected):
    with pytest.raises(TypeError) as context:
        qr(A, tolerancia, maxIter)
    assert expected in str(context.value)
