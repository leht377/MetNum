import unittest
import sys

sys.path.append("..\\metnum")


print(sys.path)
import metnum


class test_biseccion(unittest.TestCase):
    def test_retorna_una_tupla(self):
        pass

    def test_encontro_raiz_aproximada(self):
        def f(x):
            return x**2 + 53 * x + 5

        intervaloA = -1
        intervaloB = 1
        tolerancia = 10**-6

        resultado = metnum.biseccion(f, intervaloA, intervaloB, tolerancia)

        self.assertAlmostEqual(resultado[0], (1, 2, 4))
        pass

    def test_laza_TypeError_si_f_no_es_una_funcion(self):
        pass

    def test_laza_TypeError_si_los_parametros_no_son_numericos(self):
        pass

    def test_error_si_el_intervalo_no_tiene_una_raiz(self):
        pass


if __name__ == "__main__":
    unittest.main()
