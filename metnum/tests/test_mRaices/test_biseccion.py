import unittest
from ...mRaices import biseccion


class test_biseccion(unittest.TestCase):
    def test_retorna_una_tupla(self):
        resultado = biseccion(lambda x: x**2 + 53 * x + 5, -1, 1, 10**-6)
        self.assertIsInstance(resultado, tuple)

    def test_encontro_raiz_aproximada(self):
        resultado = biseccion(lambda x: x**2 + 53 * x + 5, -1, 1, 10**-6)
        resultado2 = biseccion(lambda x: x**3 + 3 * x**2, -5, -2, 10**-8)

        self.assertAlmostEqual(resultado[0], -0.09450811)
        self.assertAlmostEqual(resultado2[0], -3.00000)

    def test_laza_TypeError_si_f_no_es_una_funcion(self):
        with self.assertRaises(TypeError) as context:
            biseccion("lambda x: x**2 + 53 * x + 5", -1, 1, 10**-6)
        self.assertTrue(
            "El argumento f debe ser de tipo typing.Callable" in str(context.exception))

    def test_laza_TypeError_si_los_parametros_no_son_correctos(self):

        with self.assertRaises(TypeError) as context:
            biseccion(lambda x: x**2 + 53 * x + 5, "-1", 1, 10**-6)
        self.assertTrue(
            "El argumento intervaloA debe ser de tipo int | float" in str(
                context.exception)
        )

        with self.assertRaises(TypeError) as context:
            biseccion(lambda x: x**2 + 53 * x + 5, -1, "1", 10**-6)
        self.assertTrue(
            "El argumento intervaloB debe ser de tipo" in str(
                context.exception)
        )

        with self.assertRaises(TypeError) as context:
            biseccion(lambda x: x**2 + 53 * x + 5, -1, 1, "10**-6")
        self.assertTrue(
            "El argumento tolerancia debe ser de tipo" in str(
                context.exception)
        )

        with self.assertRaises(TypeError) as context:
            biseccion(lambda x: x**2 + 53 * x + 5, -1, 1, 10**-6, "string")
        self.assertTrue(
            "El argumento plot debe ser de tipo" in str(context.exception))

    def test_laza_Error_si_el_intervalo_no_tiene_una_raiz(self):
        with self.assertRaises(ValueError) as context:
            biseccion(lambda x: x**2 + 53 * x + 5, 10, 1, 10**-6)

        self.assertTrue(
            "No hay raiz en el intervalo [10, 1]" in str(context.exception))


if __name__ == "__main__":
    unittest.main()
