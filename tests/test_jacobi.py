import unittest
import numpy as np
from metnum import jacobi


class test_jacobi(unittest.TestCase):
    def test_encontro_incognita1(self):
        A = [[10, 2, -3], [4, 7, -1], [-2, 1, 4]]
        b = [[1], [-1], [5]]
        x0 = [[0], [0], [0]]
        resultado = jacobi(A, b, x0)
        self.assertIsNone(
            np.testing.assert_allclose(
                resultado,
                [[0.64903836], [-0.27884608], [1.64423064]],
                atol=10**-5,
            )
        )


if __name__ == "__main__":
    unittest.main()
