import unittest
from metnum import gaussJordan
import numpy as np

# print(gaussJordan([[5, 2, 1], [2, 1, 2], [4, 1, 3]], [[20, 10, 17]]))
# print(gaussJordan([[6, 2, 1], [-1, 8, 2], [1, -1, 6]], [[25, -6, 23]]))
# print(
#
# )

# print(
#     gaussJordan(
#         [[1, -2, 2, -3], [3, 4, -1, 1], [2, -3, 2, -1], [1, 1, -3, -2]],
#         [[15, -6, 17, -7]],
#     )
# )


class test_gaussJordan(unittest.TestCase):
    def test_encontro_incognita1(self):
        matrizA = [[3, -0.1, -0.2], [0.1, 7, -0.3], [0.3, -0.2, 10]]
        matrizB = [[7.85, -19.3, 71.4]]
        resultado = gaussJordan(matrizA, matrizB)
        self.assertIsNone(np.testing.assert_allclose(resultado, [[3], [-2.5], [7]]))

    # def test_encontro_incognita2(self):
    #     matrizA = [[6, 2, 1], [-1, 8, 2], [1, -1, 6]]
    #     matrizB = [[25, -6, 23]]
    #     resultado = gaussJordan(matrizA, matrizB)
    #     self.assertIsNone(np.testing.assert_allclose(resultado, [[3], [-2.5], [7]]))

    def test_encontro_incognita3(self):
        matrizA = [[5, 2, 1], [2, 1, 2], [4, 1, 3]]
        matrizB = [[20, 10, 17]]
        resultado = gaussJordan(matrizA, matrizB)
        self.assertIsNone(np.testing.assert_allclose(resultado, [[3], [2], [1]]))

    # self.assertAlmostEqual(resultado, [[3.0], [-2.5], [7.0]])


if __name__ == "__main__":
    unittest.main()
