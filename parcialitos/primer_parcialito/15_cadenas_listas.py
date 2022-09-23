"""a. Escribir una función que reciba una cadena con un nombre y un número N, y devuelva una cadena representando
el slogan.
Un slogan se forma con:
    Las 2 primeras letras de la cadena seguidas por una coma, repetido N veces separado por un espacio
    El nombre seguido de un espacio
    Las 2 primeras letras de la cadena seguidas por la segunda letra de la cadena repetida N veces.
Ejemplo: - Para "Alan" y 3 debe devolver "Al, Al, Al, Alan Allll" - Para "Barbara" y 2 debe devolver "Ba, Ba, Barbara Baaa"
b. Escribir un programa que utilice la función, pidiendole al usuario que ingrese por separado el nombre y el numero, y
 finalmente imprima el resultado. El programa debe asegurarse que lo ingresado por el usuario es válido (es decir, el
  programa no lanza error) y volviéndole a pedir que ingrese los valores necesarios hasta que cumpla con las condiciones
  necesarias.
"""
def slogan(nombre, n):
    """Devuelve el slogan"""
    slogan = ""
    for i in range(n):
        slogan += nombre[:2] + ", "
    slogan += nombre + " " + nombre[0] + nombre[1] * n
    return slogan
print(slogan("Alan", 5))