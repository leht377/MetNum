import pytest
from metnum import secante


def test_retorna_una_tupla():
    resultado = secante(lambda x: x**2 + 53 * x + 5, 1, 2, 10**-6, 20)
    assert isinstance(resultado, tuple)


@pytest.mark.parametrize(
    "f, aprox1, aprox2, tol,iteracciones,expected", [
        (lambda x: x**2 - 2, 1, 2, 12**-6, 100,
         (1.4142135623730954, 8.881784197001252e-16, 6)),
        (lambda x: x**2 + 53 * x + 5, 1, 2, 10**-
         6, 20, (-0.09450814697821237, 0.0, 5))
    ]
)
def test_encontro_raiz_aproximada(f, aprox1, aprox2, tol, iteracciones, expected):
    resultado = secante(f, aprox1, aprox2, tol, iteracciones)
    assert resultado == expected


def test_laza_TypeError_si_f_no_es_una_funcion():
    with pytest.raises(TypeError) as context:
        secante("lambda x: x**2 - 2", 1, 2, 12**-6, 100)
    assert "El objeto no es invocable" in str(context.value)


@pytest.mark.parametrize(
    "f, aprox1, aprox2, tol,iteracciones,plot,expected", [
        (lambda x: x**2 - 2, "1", 2, 12**-6, 100, False,
         "La aproximacion0 deben ser entero o float"),
        (lambda x: x**2 - 2, 1, "2", 12**-6, 100, False,
         "La aproximacion1 deben ser entero o float"),
        (lambda x: x**2 - 2, 1, 2, "12**-6", 100, False,
         "La toleracia deben ser entero o float"),
        (lambda x: x**2 - 2, 1, 2, 12**-6, "100", False,
         "maximoInteraciones deben ser entero o float"),
        (lambda x: x**2 - 2, 1, 2, 12**-6, 100,
         "False", "Plot debe de ser de tipo bool"),

    ]
)
def test_laza_TypeError_si_los_parametros_no_son_correctos(f, aprox1, aprox2, tol, iteracciones, plot, expected):
    with pytest.raises(TypeError) as context:
        secante(f, aprox1, aprox2, tol, iteracciones, plot)
    assert expected in str(context.value)
