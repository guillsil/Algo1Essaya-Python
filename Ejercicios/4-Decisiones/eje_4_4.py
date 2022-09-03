"""Escribir funciones que permitan encontrar:
a) El máximo o mínimo de un polinomio de segundo grado (dados los coeficientes a, b y
c), indicando si es un máximo o un mínimo.
b) Las raíces (reales o complejas) de un polinomio de segundo grado.
Nota: validar que las operaciones puedan efectuarse antes de realizarlas (no dividir por
cero, ni calcular la raíz de un número negativo).
c) La intersección de dos rectas (dadas las pendientes y ordenada al origen de cada recta).
Nota: validar que no sean dos rectas con la misma pendiente, antes de efectuar la opera-
ción."""
# a)
"""def max_min(a, b, c):
    # Muestra en pantalla el máximo o mínimo de un polinomio de segundo grado
    if a > 0:
        print("El máximo es", -b / (2 * a))
    else:
        print("El mínimo es", -b / (2 * a))

max_min(1, 2, 3)
# b)
def raices(a, b, c):
    # Muestra en pantalla las raíces de un polinomio de segundo grado
    if a != 0:
        if b**2 - 4 * a * c >= 0:
            print("Las raíces son", (-b + (b**2 - 4 * a * c)**0.5) / (2 * a), "y", (-b - (b**2 - 4 * a * c)**0.5) / (2 * a))
        else:
            print("Las raíces son", (-b / (2 * a)), "+", ((-b**2 + 4 * a * c)**0.5) / (2 * a), "i", "y", (-b / (2 * a)), "-", ((-b**2 + 4 * a * c)**0.5) / (2 * a), "i")
    else:
        print("No es un polinomio de segundo grado")

raices(1, 2, 3)"""
# c)
def interseccion(m1, b1, m2, b2):
    # Muestra en pantalla  el punto  intersección entre dos rectas
    if m1 != m2 and m1%m2 == 0:
        print("La intersección es", "x = ",(b2 - b1) / (m1 - m2), ", y =", ((b2 - b1) / (m1 - m2)) * m1 + b1)
    else:
        print("Las rectas son paralelas")
    elif m1%m2 == 0:
        print("No se puede calcular la intersección")

print(interseccion(3, 1, 4, 3))