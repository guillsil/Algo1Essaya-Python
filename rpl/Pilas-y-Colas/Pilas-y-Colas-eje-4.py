"""Escribir una función que recibe una expresión matemática (en forma de cadena)
y devuelve True si los paréntesis ('()'), corchetes ('[]') y llaves ('{}') están correctamente
balanceados, False en caso contrario. Ejemplos:
validar('(x+y)/2') -> True
validar('[8*4(x+y)]+{2/5}') -> True
validar('(x+y]/2') -> False
validar('1+)2(+3') -> False"""
#inportar la clase pila
from pila import Pila
def validar(expresion):
    pila = Pila()
    for c in expresion:
        if c in '([{':
            pila.apilar(c)
        elif c in ')]}':
            if pila.esta_vacia():
                return False
            if c == ')' and pila.ver_tope() != '(':
                return False
            if c == ']' and pila.ver_tope() != '[':
                return False
            if c == '}' and pila.ver_tope() != '{':
                return False
            pila.desapilar()
    return pila.esta_vacia()

#prueba
print(validar('(x+y)/2'))
print(validar('[8*4(x+y)]+{2/5}'))
print(validar('(x+y]/2'))
print(validar('1+)2(+3'))
