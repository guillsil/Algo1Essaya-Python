"""Crear una clase Fraccion, que cuente con dos atributos: numerador y divisor (ambos enteros), que se
asignan en el constructor, y se imprimen como X/Y en el método __str__.
La clase debe tener los siguientes métodos:
1) __add__ recibe otra fracción y devuelve una nueva fracción con la suma de ambas, con el numerador y divisor simplificados.
2) __mul__ recibe otra fracción y devuelve una nueva fracción con el producto de ambas, con el dividendo y divisor simplificados.
3) simplificar, cambia la fracción de tal forma que los valores de numerador y divisor sean los menores posibles, manteniendo el valor equivalente de la fracción.
Nota: Se recomienda leer la sección 14.4 Métodos especiales del apunte teórico de la materia
Un ejemplo del comportamiento:
#>>> f1 = Fraccion(2, 5)
#>>> f2 = Fraccion(13, 5)
#>>> f_suma = f1 + f2
#>>> print(f_suma)
3/1
#>>> f3 = Fraccion(3, 4)
#>>> f4 = Fraccion(4, 12)
#>>> f_mul = f3 * f4
#>>> print(f_mul)
1/4
#>>> f4.simplificar()
#>>> print(f4)
1/3"""
import math
class Fraccion:
    '''
    Apuntes -Clase para representar una fraccion entre dos numeros
    '''

    def __init__(self, num, den):
        '''Inicializa la fraccion dado el numerador y el denominador'''
        self.num = num
        self.den = den
    def __str__(self):
        '''Cadena de la fraccion con el formato `num/den`'''
        return f'{self.num}/{self.den}'

    def simplificar(self):
        '''Modifica la misma fraccion para que el numerador y el denominador estén simplificados'''
        # Buscamos el maximo comun divisor entre el numerador y el denominador
        mcd = math.gcd(self.num, self.den)
        self.num //= mcd
        self.den //= mcd
    def __add__(self, f2):
        '''Devuelve una nueva fraccion, dada por la suma entre la fraccion actual y `f2`.La fraccion resultante es simplificada.'''
        #simplificar si se puede antes de sumar
        num = self.num * f2.den + self.den * f2.num
        den = self.den * f2.den
        return Fraccion(num, den)
    def __mul__(self, f2):
        ''' Devuelve una nueva fraccion, dada por la multiplicacion entre la fraccion actual y `f2`. La fraccion resultante es simplificada.'''
        num = self.num * f2.num
        den = self.den * f2.den
        return Fraccion(num, den)

f1 = Fraccion(2, 5)
f2 = Fraccion(13, 5)
f3 = Fraccion(3, 4)
f4 = Fraccion(4, 12)
f_suma = f1 + f2

print(f_suma)