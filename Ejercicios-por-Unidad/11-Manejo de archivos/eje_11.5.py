"""Escribir una función, llamada rot13, que reciba un archivo de texto de origen
y uno de destino, de modo que para cada línea del archivo origen, se guarde una línea cifrada
en el archivo destino. El algoritmo de cifrado a utilizar será muy sencillo: a cada caracter com-
prendido entre la a y la z, se le suma 13 y luego se aplica el módulo 26, para obtener un nuevo
caracter."""
def rot13(archivo1, archivo2):
    with open(archivo1, 'r') as f1, open(archivo2, 'w') as f2:
        for linea in f1:
            for caracter in linea:
                if caracter.isalpha():
                    if caracter.islower():
                        f2.write(chr((ord(caracter) - 97 + 13) % 26 + 97))
                    else:
                        f2.write(chr((ord(caracter) - 65 + 13) % 26 + 65))
                else:
                    f2.write(caracter)
rot13('archivo.txt', 'archivo2.txt')
#muestra el contenido del archivo2.txt
with open('archivo2.txt', 'r') as f:
    print(f.read())