"""Escribir una función, llamada cp, que copie todo el contenido de un archivo (sea
de texto o binario) a otro, de modo que quede exactamente igual."""
#de forma binaria
def cp(archivo1, archivo2):
    with open(archivo1, 'rb') as f1, open(archivo2, 'wb') as f2:
        f2.write(f1.read())
#de forma textual
def cp(archivo1, archivo2):
    with open(archivo1, 'r') as f1, open(archivo2, 'w') as f2:
        f2.write(f1.read())
cp('archivo.txt', 'archivo2.txt')
#muestra el contenido del archivo2.txt
with open('archivo2.txt', 'r') as f:
    print(f.read())

