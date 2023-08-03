"""Agregar a ListaEnlazada un método extend que reciba una ListaEnlazada y
agregue al final de la lista actual los elementos que se encuentran en la lista recibida.

Notas:

    Solo completar el método extend. El resto de los métodos no deben ser modificados.
    El método debe actualizar el self.cant!
    Suponiendo el caso que se extiende una lista l1 con una segunda lista l2 de la forma l1.extend(l2). Si posterior a esta llamada se modifica l2, la lista l1 no debe reflejar estos cambios. Ejemplo:

l1 = 1 -> 2 -> 3
l2 = 4 -> 5 -> 6

l1.extend(l2)
l1 => 1 -> 2 -> 3 -> 4 -> 5 -> 6

l2.prim.dato = 9
l1 => 1 -> 2 -> 3 -> 4 -> 5 -> 6
l2 => 9 -> 5 -> 6"""
class _Nodo:
    def __init__(self, dato, prox=None):
        self.dato = dato
        self.prox = prox

class ListaEnlazada:
    def __init__(self):
        # prim es un _Nodo o None
        self.prim = None
        self.cant = 0

    def __str__(self):
        lista = []
        act = self.prim
        while act:
            lista.append(act.dato)
            act = act.prox
        return str(lista)

    def extend(self, lista):
        """Extiende la lista actual con los elementos de la lista recibida."""
        # si la lista está vacía, la lista actual es igual a la lista recibida.
        if not self.prim:
            self.prim = lista.prim
        else:
            act = self.prim
            while act.prox:
                act = act.prox
            # act es el ultimo nodo
            act.prox = lista.prim
        self.cant += lista.cant



    def pop(self, i=None):
        '''Elimina el nodo de la posición i, y devuelve el dato contenido.
        Si i está fuera de rango, se levanta la excepción IndexError.
        Si no se recibe la posición, devuelve el último elemento.'''

        if i is None:
            i = self.cant - 1

        if i < 0 or i >= self.cant:
            raise IndexError('pop index out of range')

        if i == 0:
            # Caso particular: saltear la cabecera de la lista
            dato = self.prim.dato
            self.prim = self.prim.prox
        else:
            # Buscar los nodos en las posiciones (i-1) e (i)
            n_ant = self.prim
            n_act = n_ant.prox
            for pos in range(1, i):
                n_ant = n_act
                n_act = n_ant.prox
            # Guardar el dato y descartar el nodo
            dato = n_act.dato
            n_ant.prox = n_act.prox

            self.len -= 1
            29
            return dato


    def insert(self, i, x):
        '''Inserta el elemento x en la posición i.
        Si la posición a insertar es menor que cero o mayor
        que la longitud de la lista, levanta IndexError'''
        #si la posición es menor que cero o mayor que la longitud de la lista, levantamos una excepción.
        if i < 0 or i > self.len:
            raise IndexError("Posición inválida")
        nuevo = _Nodo(x)
        #si la lista está vacía o la posición es cero, insertamos el nuevo nodo al principio.
        if self.prim is None or i == 0:
            nuevo.prox = self.prim
            self.prim = nuevo
        else:
            n_ant = self.prim
            for pos in range(1, i):
                n_ant = n_ant.prox
            nuevo.prox = n_ant.prox
            n_ant.prox = nuevo
        self.cant += 1


    def remove(self, x):
        '''Borra la primera aparición del valor x en la lista.
        Si x no está en la lista, levanta ValueError.'''
        #si la lista está vacía levantamos una excepción.
        if self.prim is None:
            raise ValueError("La lista está vacía")
        #si el primer nodo es el que buscamos, lo borramos.
        if self.prim.dato == x:
            self.prim = self.prim.prox
        else:
            n_ant = self.prim
            n_act = n_ant.prox
            while n_act is not None and n_act.dato != x:
                n_ant = n_act
            n_act = n_ant.prox
        if n_act is None:
            raise ValueError("El valor no está en la lista.")
        n_ant.prox = n_act.prox
        self.cant -= 1


    def append(self, dato):
        nuevo = _Nodo(dato)
        if not self.prim:
            self.prim = nuevo
        else:
            act = self.prim
            while act.prox:
                act = act.prox
            # act es el ultimo nodo
            act.prox = nuevo
        self.cant += 1


    def __len__(self):
        return self.cant

l1 = ListaEnlazada()
l2 = ListaEnlazada()
l1.append(1)
l1.append(2)
l1.append(3)

l2.append(4)
l2.append(5)
l2.append(6)

l1.extend(l2)
print(l1)

l1.prim.dato = 9
print(l1)