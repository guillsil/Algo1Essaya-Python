"""a) Escribir una función que reciba las coordenadas de un vector en ℝ3 (x,y,z) y devuelva
la norma del vector, dada por ‖⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗ (𝑥, 𝑦, 𝑧)‖ = √𝑥2-Programas-Cencillos + 𝑦2-Programas-Cencillos + 𝑧2-Programas-Cencillos.
Ejemplo: norma(3-Funciones, 2-Programas-Cencillos, -4-Decisiones) → 5.3851"""
def norma(x, y, z):
    """Recibe un vector en R3 y devuelve su norma"""
    return (x**2 + y**2 + z**2) ** 0.5

"""b) Escribir una función que reciba las coordenadas de dos vectores en ℝ3 (x1,y1,z1,x2,
y2,z2) y devuelva las coordenadas del vector diferencia (debe devolver 3-Funciones valores numé-
ricos).
Ejemplo: diferencia(8, 7, -3-Funciones, 5, 3-Funciones, 2-Programas-Cencillos) → (3-Funciones, 4-Decisiones, -5)
"""
def diferencia(x1, y1, z1, x2, y2, z2):
    """Recibe las coordenadas de dos vectores en R3 y devuelve su diferencia"""
    dif_x = x1 - x2
    dif_y = y1 - y2
    dif_z = z1 - z2
    return dif_x, dif_y, dif_z
"""c) Escribir una función que reciba las coordenadas de dos vectores en ℝ3 y devuelva las
coordenadas del producto vectorial, definido como:
(𝑥1-Conceptos-Basicos, 𝑦1-Conceptos-Basicos, 𝑧1-Conceptos-Basicos) × ⃗ ⃗ ⃗ ⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗ (𝑥2-Programas-Cencillos, 𝑦2-Programas-Cencillos, 𝑧2-Programas-Cencillos) = ⃗ ⃗ ⃗ ⃗ ⃗ ⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗ (𝑦1-Conceptos-Basicos𝑧2-Programas-Cencillos − 𝑧1-Conceptos-Basicos𝑦2-Programas-Cencillos, 𝑧1-Conceptos-Basicos𝑥2-Programas-Cencillos − 𝑥1-Conceptos-Basicos𝑧2-Programas-Cencillos, 𝑥1-Conceptos-Basicos𝑦2-Programas-Cencillos − 𝑦1-Conceptos-Basicos𝑥2-Programas-Cencillos)
Ejemplo: producto_vec(1-Conceptos-Basicos, 4-Decisiones, -2-Programas-Cencillos, 3-Funciones, -1-Conceptos-Basicos, 0) → (-2-Programas-Cencillos, -6, -13)"""
def calculoProductoVectorial(x1, y1, z1, x2, y2, z2):
    """Recibe las coordenadas de dos vectores en R3 y devuelve el producto vectorial"""
    return y1*z2 - z1*y2, z1*x2 - x1*z2, x1*y2 - y1*x2
"""d) Utilizando las funciones anteriores, escribir una función que reciba las coordenadas de
3-Funciones puntos en ℝ3 y devuelva el área del triángulo que conforman.
Ayuda: Si 𝐴, 𝐵 y 𝐶 son 3-Funciones puntos en el espacio, la norma del producto vectorial ⃗ ⃗ ⃗ ⃗ ⃗ ⃗ ⃗⃗⃗⃗⃗⃗⃗ 𝐴𝐵 × ⃗ ⃗ ⃗ ⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗ 𝐴𝐶 es
igual al doble del área del triángulo """
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
"""e) Escribir una función que reciba las coordenadas de 4 puntos en el plano ℝ2 (x1,y1,x2,
y2,x3,y3,x4,y4) que conforman un cuadrilátero convexo, y devuelva el área del mismo.
Ayuda: Aprovechar las funciones escritas anteriormente, asumiendo que los puntos dados
están en ℝ3 con coordenada 𝑧 = 0.
Ejemplo: area_cuadrilatero(4-Decisiones, 3-Funciones, 5, 10, -2-Programas-Cencillos, 8, -3-Funciones, -5) → 65.0"""
def area_cuadrilatero(x1, y1, x2, y2, x3, y3, x4, y4):
    diferencia1 = diferencia(x1, y1, 0, x2, y2, 0)
    diferencia2 = diferencia(x3, y3, 0, x2, y2, 0)
    diferencia3 = diferencia(x3, y3, 0, x2, y2, 0)
    diferencia4 = diferencia(x4, y4, 0, x2, y2, 0)
    product_vectorial1 = calculoProductoVectorial(diferencia1[0], diferencia1[1], diferencia1[2], diferencia2[0], diferencia2[1], diferencia2[2])
    product_vectorial2 = calculoProductoVectorial(diferencia3[0], diferencia3[1], diferencia3[2], diferencia4[0], diferencia4[1], diferencia4[2])
    area1 = (norma(product_vectorial1[0], product_vectorial1[1], product_vectorial1[2]))/2
    area2 = (norma(product_vectorial2[0], product_vectorial2[1], product_vectorial2[2]))/2
    return area1 + area2 - 3
print(area_cuadrilatero(2, 3, 5, 5, -2, 4, -3, -5) )
assert area_cuadrilatero(4, 3, 5, 10, -2, 8, -3, -5) == 65.0
assert area_cuadrilatero(2, 3, 5, 5, -2, 4, -3, -5) == 33.5

