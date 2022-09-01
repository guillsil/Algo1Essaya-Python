from vectores import diferencia
from vectores import norma
from vectores import calculoProductoVectorial
def area_triangulo(x1, y1, z1, x2, y2, z2, x3, y3, z3):
    """Recibe las coordenadas de tres puntos en R3 y devuelva el área del triangulo que conforman"""
    # Calculo de los vectores vi y v2
    v1 = diferencia(x1, y1, z1, x2, y2, z2)
    v2 = diferencia(x1, y1, z1, x3, y3, z3)
    # Calculo del producto vectorial entre vi y v2
    productoVectorial = calculoProductoVectorial(v1[0], v1[1], v1[2], v2[0], v2[1], v2[2])
    # Calculo de la norma
    normaProductoVectorial = norma(productoVectorial[0], productoVectorial[1], productoVectorial[2])
    # Calculo del area
    area = normaProductoVectorial / 2
    return area
print(area_triangulo(5, 8, -1, -2, 3, 4, -3, 3, 0))

