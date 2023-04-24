# MetNum 📚

MetNum es una libreria de métodos numéricos, los métodos numéricos son una herramienta esencial para los científicos y matemáticos que necesitan resolver problemas que no se pueden resolver mediante métodos analíticos tradicionales. En lugar de obtener soluciones exactas, los métodos numéricos utilizan cálculos aproximados para encontrar soluciones que se acercan lo suficiente a la respuesta real.

Esta libreria incluye los siguientes modulos:


* Métodos para encontrar raíces de funciones.
* Métodos para resolver sistemas de ecuaciones lineales.
* Métodos de interpolación.
* Métodos de valores propios y vectores propios.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install metnum.

```bash

```

## Usage

### Métodos para encontrar raíces

La librería contiene varios métodos para encontrar raíces de funciones, incluyendo:

* Método de la bisección.
* Método de Newton-Raphson.
* Método de la secante.
* Método de la Regla Falsa.

```python
import metnum.mRaices as r

# (aproxRaiz, errorRelativo, Iteraciones)
# returns (-2.195822238922119, 6.514696177371724e-07, 19)
r.biseccion(lambda x: -1 * x**3 + 3 * x - 4, -3, -1.5, 10**-6, True),

# (aproxRaiz, errorRelativo, Iteraciones)
# returns (-2.195823344883275, 2.161972486337072e-07, 10)
r.reglaFalsa(lambda x: -1 * x**3 + 3 * x - 4, -3, -1.5, 10**-6, True),

# (aproxRaiz, errorRelativo, Iteraciones)
# returns (1.0, 1.0, 41)
r.newtonRapson(lambda x: x**3 - 2 * x + 2,lambda x: 3 * x**2 - 2, -1, 10**-6, 40)

# (aproxRaiz, errorRelativo, Iteraciones)
# returns (1.0000000000102873, 1.02873265461767e-11, 13)
r.secante(lambda x: x**3 - x**2, 4, 8, 10**-6, 50)
```

##### Componente grafico 

<div style="display:flex">
  <img src="https://github.com/leht377/pagina_web/blob/master/Biseccion.png?raw=true" alt="Screenshot of biseccion" width="300px">
  <img src="https://github.com/leht377/pagina_web/blob/master/reglaFalsa.png?raw=true" alt="Screenshot of reglaFalsa" width="300px">
  <img src="https://github.com/leht377/pagina_web/blob/master/newton.png?raw=true" alt="Screenshot of newtonRapson" width="300px">
  <img src="https://github.com/leht377/pagina_web/blob/master/secante.png?raw=true" alt="Screenshot of secante" width="300px">
</div>

### Métodos para resolver sistemas de ecuaciones lineales 






### Métodos de interpolación
### Métodos de valores propios y vectores propios

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
















<!-- Librería de Métodos Numéricos en Python
Esta es una librería de Python que contiene implementaciones de diversos métodos numéricos utilizados en la resolución de problemas matemáticos y científicos. Los métodos implementados incluyen métodos de integración numérica, métodos de diferenciación numérica, métodos de solución de ecuaciones diferenciales ordinarias, métodos de solución de ecuaciones no lineales, entre otros.

Instalación

python setup.py install

## Correr solo un test

py -m unittest tests/test_biseccion.py

## Correr todo los tests

python -m unittest discover -s tests -v

pytest tests\test_mEcuacionesLineales -->
