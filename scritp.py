from metnum import mRaices
import math

print(mRaices.biseccion(lambda x: x**2 + 3 * x - 34, 3, 5, 10**-6))


print(mRaices.reglaFalsa(lambda x: math.exp(3 * x) - 4, 0, 1, 10**-6))
