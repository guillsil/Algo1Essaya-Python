"""Escribir una funcion que reciba una lista de pedidos a un supermercado, donde cada pedido es hecho por una
persona distinta y puede tener cualquier producto, y tiene la siguiente formato:
{ nombre_producto1: cant1, …, nombre_producto_n: cant_n }. La función debe escribir a un archivo que tenga el
resumen de los pedidos con el siguiente formato:
nombre_producto;cant_total
donde cada producto está una única vez y la cantidad total es la cantidad de todas las personas que compraron ese producto.
Nota: al finalizar la ejecución de la función (haya ocurrido un error o no), todos los archivos abiertos deben quedar
cerrados."""
def resumen_pedidos(pedidos):
    try:
        archivo = open("resumen_pedidos.txt", "w")
        diccionario = {}
        for pedido in pedidos:
            for producto in pedido:
                if producto in diccionario:
                    diccionario[producto] += pedido[producto]
                else:
                    diccionario[producto] = pedido[producto]
        for producto in diccionario:
            archivo.write(producto + ";" + str(diccionario[producto]) + "")
        archivo.close()
    except:
        archivo.close()
        return "Error"