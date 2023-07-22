# import pytest
# from metnum import potencias
# import numpy as np


# @pytest.mark.parametrize(
#     "A, expected", [
#         ([[3, 2, 4], [2, 2, 0], [0, 2, 3]], [5.69254381, 0.48690755, 1.82054864]),
#         ([[1, 2], [3, 4]], [5.37228132, -0.37228132])
#     ]
# )
# def test_encontro_autovectores(A, expected):
#     result = potencias(A)
#     assert not np.testing.assert_allclose(result, expected)
