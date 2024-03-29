import unittest
from ...mRaices import reglaFalsa
from ..helpers import mensaje_error


class test_reglaFalsa(unittest.TestCase):
    def test_retorna_una_tupla(self):
        resultado = reglaFalsa(lambda x: x**2 + 53 * x + 5, -1, 1, 10**-6)
        self.assertIsInstance(resultado, tuple)

    def test_encontro_raiz_aproximada(self):
        resultado = reglaFalsa(lambda x: x**2 + 53 * x + 5, -1, 1, 10**-6)
        resultado2 = reglaFalsa(lambda x: x**3 + 3 * x**2, -5, -2, 10**-8)

        self.assertAlmostEqual(resultado[0], -0.09450811)
        self.assertAlmostEqual(resultado2[0], -3.00000)

    def test_laza_TypeError_si_f_no_es_una_funcion(self):
        with self.assertRaises(TypeError) as context:
            reglaFalsa("lambda x: x**2 + 53 * x + 5", -1, 1, 10**-6)
        self.assertTrue(mensaje_error("f", "typing.Callable")
                        in str(context.exception))

    def test_laza_TypeError_si_los_parametros_no_son_numericos(self):
        with self.assertRaises(TypeError) as context:
            reglaFalsa(lambda x: x**2 + 53 * x + 5, "-1", 1, 10**-6)
        self.assertTrue(
            mensaje_error("intervaloA", "int | float") in str(
                context.exception)
        )

        with self.assertRaises(TypeError) as context:
            reglaFalsa(lambda x: x**2 + 53 * x + 5, -1, "1", 10**-6)
        self.assertTrue(
            mensaje_error("intervaloB", "int | float") in str(
                context.exception)
        )

        with self.assertRaises(TypeError) as context:
            reglaFalsa(lambda x: x**2 + 53 * x + 5, -1, 1, "10**-6")
        self.assertTrue(
            mensaje_error("tolerancia", "int | float") in str(
                context.exception)
        )


if __name__ == "__main__":
    unittest.main()
