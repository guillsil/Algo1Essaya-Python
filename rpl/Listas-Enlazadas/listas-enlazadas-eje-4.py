"""Implementar el método remover_todos(elemento) de ListaEnlazada, que recibe un elemento y remueve de la lista todas las apariciones del mismo, devolviendo la cantidad de elementos removidos. La lista debe ser recorrida una sola vez (es decir, no se puede llamar a append).

Por ejemplo para la lista 3 -> 4 -> 2 -> 3 -> 5 -> 3 -> 3 -> 3, si se llama al método con el elemento 3,
la modifica para que quede 4 -> 2 -> 5, y devuelve 5 por la cantidad de elementos 3 eliminados.

Notas:

    Solo completar el método remover_todos. El resto de los métodos no deben ser modificados.
    El método debe actualizar el self.cant!"""
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

    def remover_todos(self, elemento):
        """Elimina todas las apariciones de elemento en la lista.
        Devuelve la cantidad de elementos eliminados."""
        #si la lista está vacía, devolvemos un error.
        if self.prim is None:
            raise ValueError("La lista está vacía")
        #si el primer nodo es el que buscamos, lo borramos.
        if self.prim.dato == elemento:
            self.prim = self.prim.prox
            self.cant -= 1
        #si no, recorremos la lista.
        else:
            n_ant = self.prim
            n_act = n_ant.prox
            while n_act is not None and n_act.dato != elemento:
                n_ant = n_act
                n_act = n_ant.prox
            if n_act is None:
                raise ValueError("El valor no está en la lista.")
            n_ant.prox = n_act.prox
            self.cant -= 1
        return self.cant - 1

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

l1= ListaEnlazada()
l1.append(1)
l1.append(2)
l1.append(3)
l1.append(2)
print(l1)

valor = l1.remover_todos(2)

print(valor)