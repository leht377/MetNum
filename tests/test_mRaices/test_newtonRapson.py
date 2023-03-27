import pytest
from metnum import newtonRapson


def test_retorna_una_tupla():
    resultado = newtonRapson(lambda x: x**2 + 53 * x + 5,
                             lambda x: 2*x + 53, 2, 10**-6, 100)
    assert isinstance(resultado, tuple)


@pytest.mark.parametrize(
    "f, derivada, puntoInicial, tolerancia,maxIter,plot,expected", [
        (lambda x: x**3 - 2 * x + 2,
         lambda x: 3 * x**2 - 2, -1, 10**-6, 40, False, (-1.7692923542973595, 4.340705572758452e-10, 7)),
        (lambda x: x**2 + 53 * x + 5,
         lambda x: 2*x + 53, 2, 10**-6, 100, False, (-0.09450814674137271, 1.2507734403754966e-08, 3))
    ]
)
def test_encontro_raiz_aproximada(f, derivada, puntoInicial, tolerancia, maxIter, plot, expected):
    resultado = newtonRapson(f, derivada, puntoInicial,
                             tolerancia, maxIter, plot)
    assert resultado == expected


@pytest.mark.parametrize(
    "f, derivada, puntoInicial, tolerancia,maxIter,plot,expected", [
        ("lambda x: x**3 - 2 * x + 2",
         lambda x: 3 * x**2 - 2, -1, 10**-6, 40, False, "El objeto no es invocable"),
        (lambda x: x**2 + 53 * x + 5,
         "lambda x: 2*x + 53", 2, 10**-6, 100, False, "El objeto no es invocable")
    ]
)
def test_laza_TypeError_si_f_no_es_una_funcion(f, derivada, puntoInicial, tolerancia, maxIter, plot, expected):
    with pytest.raises(TypeError) as context:
        newtonRapson(f, derivada, puntoInicial,
                     tolerancia, maxIter, plot)
    assert expected in str(context.value)


@pytest.mark.parametrize(
    "f, derivada, puntoInicial, tolerancia,maxIter,plot,expected", [
        (lambda x: x**3 - 2 * x + 2,
         lambda x: 3 * x**2 - 2, "-1", 10**-6, 40, False, "El pundoInicial deben ser entero o float"),
        (lambda x: x**3 - 2 * x + 2,
         lambda x: 3 * x**2 - 2, -1, "10**-6", 40, False, "La toleracia deben ser entero o float"),
        (lambda x: x**3 - 2 * x + 2,
         lambda x: 3 * x**2 - 2, -1, 10**-6, "40", False, "maximoInteraciones deben ser entero o float"),
        (lambda x: x**3 - 2 * x + 2,
         lambda x: 3 * x**2 - 2, -1, 10**-6, 40, "False", "Plot debe de ser de tipo bool"),

    ]
)
def test_laza_TypeError_si_los_parametros_no_son_correctos(f, derivada, puntoInicial, tolerancia, maxIter, plot, expected):
    with pytest.raises(TypeError) as context:
        newtonRapson(f, derivada, puntoInicial, tolerancia, maxIter, plot)
    assert expected in str(context.value)
