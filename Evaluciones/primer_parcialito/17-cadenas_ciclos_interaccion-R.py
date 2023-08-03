"""Liam suele ir seguido al supermercado para hacerle las compras a sus padres. El problema es que el
listado de compras se lo envían con un mensaje mal escrito y difícil de repasar.
Para ayudarlo, se pide escribir un programa que le pida al usuario un mensaje de un pedido e
imprima cada producto con su respectiva cantidad. Liam sabe con seguridad que cuando aparece un número
en el mensaje, únicamente la palabra siguiente es un producto. Se debe imprimir también la cantidad de
productos totales del mismo mensaje. Si la entrada no tiene productos, el programa debe solicitar un nuevo mensaje
hasta que los haya.
Ejemplo de ejecución:
Ingrese el mensaje: hola liam pasas por el almacen antes de venir?
No se encontraron productos!
Ingrese el mensaje: perfecto comprá 3 papas 4 leches y 1 yogurt
papas - 3
leches - 4
yogurt - 1
Total de productos: 3
"""
#a)

def pedir_mensaje():
    """Pide el mensaje al usuario"""
    mensaje = input("Ingrese el mensaje: ")
    while verificar_mensaje(mensaje):
        print("No se encontraron productos!")
        mensaje = input("Ingrese el mensaje: ")
    return devolver_productos(mensaje)

def verificar_mensaje(mensaje):
    """Verifica si el mensaje tiene productos"""
    for caracter in mensaje:
        if caracter.isdigit():
            if mensaje[mensaje.index(caracter) + 2].isalpha():
                return False
    return True

def devolver_productos(mensaje):
    """Devuelve los productos"""
    productos = []
    palabras = mensaje.split()
    for palabra in palabras:
        if palabra.isdigit():
            productos.append(palabras[palabras.index(palabra) + 1] + " - " + palabra)
    return productos

def imprimir_productos(productos):
    """Imprime los productos"""
    for producto in productos:
        print(producto)
    print("Total de productos: " + str(len(productos)))

def main():
    """Función principal"""
    productos = pedir_mensaje()
    imprimir_productos(productos)

main()