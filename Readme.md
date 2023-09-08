<p align="center">
  <img src="https://github.com/leht377/pagina_web/blob/master/Logo.png" alt="Logo of metnum">
</p>

MetNum es una libreria de métodos numéricos, los métodos numéricos son una herramienta esencial para los científicos y matemáticos que necesitan resolver problemas que no se pueden resolver mediante métodos analíticos tradicionales. En lugar de obtener soluciones exactas, los métodos numéricos utilizan cálculos aproximados para encontrar soluciones que se acercan lo suficiente a la respuesta real.

Esta libreria incluye los siguientes modulos:

- Métodos para encontrar raíces de funciones.
- Métodos para resolver sistemas de ecuaciones lineales.
- Métodos de interpolación.
- Métodos de valores propios y vectores propios.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install metnum.

```bash

```

## Run Test

```bash
pytest tests
```

## Usage

### Métodos para encontrar raíces

La librería contiene varios métodos para encontrar raíces de funciones, los cuales son:

- Método bisección.
- Método de Newton-Raphson.
- Método de la secante.
- Método de la Regla Falsa.

```python
import metnum.mRaices as r

# (aproxRaiz, errorRelativo, Iteraciones)
# returns (-2.195822238922119, 6.514696177371724e-07, 19)
r.biseccion(lambda x: -1 * x**3 + 3 * x - 4, -3, -1.5, 10**-6),

# (aproxRaiz, errorRelativo, Iteraciones)
# returns (-2.195823344883275, 2.161972486337072e-07, 10)
r.reglaFalsa(lambda x: -1 * x**3 + 3 * x - 4, -3, -1.5, 10**-6),

# (aproxRaiz, errorRelativo, Iteraciones)
# returns (1.0, 1.0, 41)
r.newtonRapson(lambda x: x**3 - 2 * x + 2,lambda x: 3 * x**2 - 2, -1, 10**-6, 40)

# (aproxRaiz, errorRelativo, Iteraciones)
# returns (1.0000000000102873, 1.02873265461767e-11, 13)
r.secante(lambda x: x**3 - x**2, 4, 8, 10**-6, 50)
```

##### Componente gráfico

<div style="display:flex">
  <img src="https://github.com/leht377/pagina_web/blob/master/Biseccion.png?raw=true" alt="Screenshot of biseccion" width="300px">
  <img src="https://github.com/leht377/pagina_web/blob/master/reglaFalsa.png?raw=true" alt="Screenshot of reglaFalsa" width="300px">
  <img src="https://github.com/leht377/pagina_web/blob/master/newton.png?raw=true" alt="Screenshot of newtonRapson" width="300px">
  <img src="https://github.com/leht377/pagina_web/blob/master/secante.png?raw=true" alt="Screenshot of secante" width="300px">
</div>

### Métodos para resolver sistemas de ecuaciones lineales

La librería cuenta con los siguientes métodos para solucionar sistemas de ecuaciones lineales de la forma Ax = b.

- Método Gauss-Jordan.
- Método Gauss-Seidel.
- Método de Jacobi.
- Método de descomposición LU.

```python
import metnum.mEcuacionesLineales as ln

A = [[6, 2, 1], [-1, 8, 2], [1, -1, 6]]
b =  [25, -6, 23]
x0 = [0, 0, 0]
tolerancia = 10**-12
maxIter = 100

# returns ([[4],[-1],[3]])
ln.gaussJordan(A, b)

# returns ([[-4],[-1],[3]])
ln.gaussSeidel(A, b, tolerancia, maxIter)

# returns ([[4],[-1],[3]])
ln.jacobi(A, b, tolerancia, maxIter)

# returns ([[4],[-1],[3]])
ln.LU(A, b)
```

### Métodos de interpolación

La librería contiene varios métodos de iterpolacion, los cuales son:

- Método de interpolación inversa
- Método de interpolación de paso constate
- Método de interpolación de paso variable

```python
import metnum.mInterpolacion as interp

x = [2, 4, 6, 8, 10]
y = [8, 26, 52, 86, 128]
xk = 3

#returns (16.0,[18, 8])
interp.pasoConstante(x,y,xk)


x = [0, 1, 2, 5]
y = [5, 7, 9, 15]
xk = 3

#return 11.0
interp.pasoVariable(x,y,xk)

x = [0.2, 0.4, 0.6]
y = [-1.472, -0.656, 0.496]
yk = 0

#returns 0.5257080610021786
interp.inversa(x,y,yk)
```

### Métodos de valores propios y vectores propios

La librería cuenta con los siguientes para encontrar valores propios y vectores propios de una matriz

- Método de descomposición QR
- Método de las potencias

```python
import metnum.mEigen as eg
matrizA = [[3, 2, 4],[2, 2, 0],[0, 2, 3]]

#returns array([5.69254381 0.48690755 1.82054864])
eg.qr(matrizA)


matrizB = [[1, 2], [3, 4]]
vectorInicial = [1, 1]

# returns (5.372281323269014, array([0.41597356, 0.90937671]))
eg.potencias(matrizB,vectorInicial)
```
