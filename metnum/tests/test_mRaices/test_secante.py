import pytest
from ...mRaices import secante
from ..helpers import mensaje_error


def test_retorna_una_tupla():
    resultado = secante(lambda x: x**2 + 53 * x + 5, 1, 2, 10**-6, 20)
    assert isinstance(resultado, tuple)


@pytest.mark.parametrize(
    "f, aprox1, aprox2, tol,iteracciones,expected", [
        (lambda x: x**2 - 2, 1, 2, 12**-6, 100,
         1.4142135623730954),
        (lambda x: x**2 + 53 * x + 5, 1, 2, 10**-
         6, 20, -0.09450814697821237)
    ]
)
def test_encontro_raiz_aproximada(f, aprox1, aprox2, tol, iteracciones, expected):
    resultado = secante(f, aprox1, aprox2, tol, iteracciones)
    assert resultado[0] == expected


def test_laza_TypeError_si_f_no_es_una_funcion():
    with pytest.raises(TypeError) as context:
        secante("lambda x: x**2 - 2", 1, 2, 12**-6, 100)
    assert mensaje_error("f", "typing.Callable") in str(context.value)


@pytest.mark.parametrize(
    "f, aprox1, aprox2, tol,iteracciones,plot,expected", [
        (lambda x: x**2 - 2, "1", 2, 12**-6, 100, False,
         mensaje_error("x0", "int | float")),
        (lambda x: x**2 - 2, 1, "2", 12**-6, 100, False,
         mensaje_error("x1", "int | float")),
        (lambda x: x**2 - 2, 1, 2, "12**-6", 100, False,
         mensaje_error("tolerancia", "int | float")),
        (lambda x: x**2 - 2, 1, 2, 12**-6, "100", False,
         mensaje_error("maxIter", "<class 'int'>"))

    ]
)
def test_laza_TypeError_si_los_parametros_no_son_correctos(f, aprox1, aprox2, tol, iteracciones, plot, expected):
    with pytest.raises(TypeError) as context:
        secante(f, aprox1, aprox2, tol, iteracciones, plot)
    assert expected in str(context.value)
