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
def productos(mensaje):
    mensaje = mensaje.split()
    productos = []
    for i in range(len(mensaje)):
        if mensaje[i].isdigit():
            productos.append((mensaje[i+1], mensaje[i]))
    return productos
print(productos("hola liam pasas por el almacen antes de venir?"))