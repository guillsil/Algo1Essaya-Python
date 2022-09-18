""" Sistema de facturación simplificado
Se cuenta con una lista ordenada de productos, en la que uno consiste en una tupla de (identi-
ficador, descripción, precio), y una lista de los productos a facturar, en la que cada uno consiste
en una tupla de (identificador, cantidad).
Se desea generar una factura que incluya la cantidad, la descripción, el precio unitario y el pre-
cio total de cada producto comprado, y al final imprima el total general.
Escribir una función que reciba ambas listas e imprima por pantalla la factura solicitada."""
def facturas(productos, compras):
    print("Factura:")
    total = 0
    for i in range(len(compras)):
        for j in range(len(productos)):
            if compras[i][0] == productos[j][0]:
                print(f"{compras[i][1]} {productos[j][1]} ${productos[j][2]} ${productos[j][2]*compras[i][1]}")
                total += productos[j][2]*compras[i][1]
    print(f"Total: ${total}")
productos = [(1, "Manzana", 100), (2, "Pera", 150), (3, "Banana", 200), (4, "Naranja", 250), (5, "Durazno", 300)]
compras = [(1, 2), (2, 3), (3, 1), (4, 4), (5, 1)]
facturas(productos, compras)