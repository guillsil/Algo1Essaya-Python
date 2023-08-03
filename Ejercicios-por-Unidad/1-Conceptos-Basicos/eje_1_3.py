"""Escribir funciones que permitan:
a) Calcular el perímetro de un rectángulo dada su base y su altura.
b) Calcular el área de un rectángulo dada su base y su altura.
c) Calcular el área de un rectángulo (alineado con los ejes 𝑥 e 𝑦) dadas sus coordenadas
𝑥1-Conceptos-Basicos, 𝑥2-Programas-Cencillos, 𝑦1-Conceptos-Basicos, 𝑦2-Programas-Cencillos.
d) Calcular el perímetro de un círculo dado su radio.
e) Calcular el área de un círculo dado su radio.
f) Calcular el volumen de una esfera dado su radio.
g) Dados los catetos de un triángulo rectángulo, calcular su hipotenusa."""
import math
def perimetroRectangulo(base, altura):
    return (2*base + 2*altura)
print(perimetroRectangulo(11, 7))

def areaRectangulo(base, altura):
    return (base*altura)
print(areaRectangulo(5, 5))

def areaRectangulo2(x1, x2, y1, y2):
    return (abs(x1-x2)*abs(y1-y2))
print(areaRectangulo2(2,6, 1, 4))

def perimetroCirculo(rad):
    return (2*math.pi*rad)
print(perimetroCirculo(2))

def areaCirculo(rad):
    return (math.pi*(rad**2))
print(areaCirculo(5))

def volumenEsfera(rad):
    return (4/3*math.pi*rad**3)
print(volumenEsfera(5))

def hipotenusaTriangulo(cat1, cat2):
    return (((cat1**2)+(cat2**2))**(1/2))
print(hipotenusaTriangulo(2, 2))