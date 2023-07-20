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
#a)
def slogan(nombre, n):
    """Devuelve el slogan"""
    slogan = ""
    for i in range(n):
        slogan += nombre[:2] + ", "
    slogan += nombre + " " + nombre[:2] + nombre[1]* n
    return slogan
#b)

def pedir_nombre_y_n():
    """Pide el nombre y el n al usuario"""
    nombre = input("Ingrese el nombre: ")
    n = input("Ingrese el n: ")
    while not nombre.isalpha() and len(nombre) > 0 and not n.isdigit():
        print("El nombre debe ser una cadena de caracteres y el n un número.")
        nombre = input("Ingrese el nombre: ")
        n = input("Ingrese el n: ")
    return nombre, int(n)

def main():
    """Función principal"""
    nombre, n = pedir_nombre_y_n()
    print(slogan(nombre, n))
main()


