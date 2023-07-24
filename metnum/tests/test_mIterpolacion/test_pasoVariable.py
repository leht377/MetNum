import pytest
from ...mIterpolacion import pasoVariable
from ..helpers import mensaje_error


@pytest.mark.parametrize(
    "x,y,xk,expected",
    [([5, 10, 15, 20, 25, 30, 35, 40], [-25, 0, 75, 200, 375, 600, 875, 1200], 12, 24),  # lambda x: x**2 -10*x
     ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], [1, 8, 27, 64,
      125, 216, 343, 512, 729, 1000, 1331], 8.5, 614.125),  # lambda x: x**3
     ([12, 15, 18, 21, 24], [1728, 3375, 5832,
      9261, 13824], 21, 9261),  # lambda x: x**3
     ([12, 15, 18, 21, 24], [1728, 3375, 5832, 9261, 13824], 12, 1728),
     ([1, 55, 66, 787, 4555, 99999], [4, 3190, 4554, 621730, 20761690, 10000099998], 500, 251500)]  # lambda x: x**3
)
def test_encontro_yk(x, y, xk, expected):
    yk = pasoVariable(x, y, xk)
    assert yk == pytest.approx(expected)


@pytest.mark.parametrize(
    "x, y, xk, expected",
    [(1, [-25, 0, 75, 200, 375, 600, 875, 1200], 12, mensaje_error("x", "list | numpy.ndarray")),
     ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], 2, 8.5,
      mensaje_error("y", "list | numpy.ndarray")),
     ([12, 15, 18, 21, 24], [1728, 3375, 5832,
      9261, 13824], "21", mensaje_error("xk", "int | float")),
     ]
)
def test_args_types(x, y, xk, expected):
    with pytest.raises(TypeError) as context:
        pasoVariable(x, y, xk)
    assert expected in str(context.value)
