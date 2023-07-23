import pytest
from ...mEigen import potencias
import numpy as np
from ..helpers import mensaje_error


@pytest.mark.parametrize(
    "A, b, expected", [
        ([[1, 2], [3, 4]], [1, 1], (5.372281323268953, [0.41597356, 0.90937671])),
        ([[1, 0], [1, 3]], [1, 1], (3., [7.86823591e-13, 1.]))
    ]
)
def test_encontro_autovector_y_autovalor_dominante(A, b, expected):
    autoValor, autoVector = potencias(A, b)
    assert autoValor == pytest.approx(expected[0])
    assert not np.testing.assert_allclose(autoVector, expected[1])


@pytest.mark.parametrize(
    "A, x, tolerancia, maxIter, expected", [
        (1, [1, 1], 10 ** -12, 100,
         mensaje_error("A", "list | numpy.ndarray")),
        ([[1, 2], [3, 4]], 1, 10 ** -12, 100,
         mensaje_error("x", "list | numpy.ndarray")),
        ([[1, 2], [3, 4]], [1, 1], " 10 ** -12", 100,
         mensaje_error("tolerancia", "<class 'float'>")),
        ([[1, 2], [3, 4]], [1, 1], 10 ** -12, "100",
         mensaje_error("maxIter", "<class 'int'>")),

    ]
)
def test_args_types_checking(A, x, tolerancia, maxIter, expected):
    with pytest.raises(TypeError) as context:
        potencias(A, x, tolerancia, maxIter)
    assert expected in str(context.value)
