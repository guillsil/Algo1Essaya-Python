"""Escribir una funcion que reciba una lista de pedidos a un supermercado, donde cada pedido es hecho por una
persona distinta y puede tener cualquier producto, y tiene la siguiente formato:
{ nombre_producto1: cant1, …, nombre_producto_n: cant_n }. La función debe escribir a un archivo que tenga el
resumen de los pedidos con el siguiente formato:
nombre_producto;cant_total
donde cada producto está una única vez y la cantidad total es la cantidad de todas las personas que compraron ese producto.
Nota: al finalizar la ejecución de la función (haya ocurrido un error o no), todos los archivos abiertos deben quedar
cerrados."""
def resumen_pedidos(pedidos):
    productos = {}
    for pedido in pedidos:
        for producto, cantidad in pedido.items():
            if producto in productos:
                productos[producto] += cantidad
            else:
                productos[producto] = cantidad
    with open("resumen_pedidos.txt", "w") as f:
        for producto, cantidad in productos.items():
            f.write(f"{producto};{cantidad}")
    return productos

print(resumen_pedidos({"leche": 2, "pan": 1, "queso": 1}))