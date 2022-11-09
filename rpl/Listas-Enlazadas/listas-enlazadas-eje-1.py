"""Los siguientes métodos a implementar se encuentran detallados y resueltos en el apunte teórico de
la materia en la sección 15 Listas Enlazadas. Se recomienda fuertemente leer el capítulo para que los
ejercicios de la guía salgan con mayor facilidad.
Después de leerlo, se puede saltear esta actividad. Queda solo a modo de práctica o prueba.
Para una ListaEnlazada con referencia al primer nodo prim y su cantidad cant, implementar los siguientes métodos:
    pop(i): elimina de la lista el nodo correspondiente al índice i, y devuelve su dato. Si i está fuera de rango, debe levantar la excepción IndexError. Si no se recibe la posición, elimina el último elemento.
    insert(i, x) inserta el elemento x en la posición i. Si se intenta insertar en una posición menor que cero o mayor que la longitud de la lista, levanta IndexError.
    remove(x) elimina la primera aparición del valor x en la lista. Si x no está en la lista, levanta ValueError.
Notas:
    Todos los métodos deben actualizar self.cant cuando corresponda.
    Solo se deben completar los métodos indicados. El resto del código no debe ser modificado.
    Las pruebas de los métodos son independientes entre sí. Entonces se podría, por ejemplo, completar y
     probar el insert antes de escribir la implementación del pop.
"""
class _Nodo:
    def __init__(self, dato, prox=None):
        self.dato = dato
        self.prox = prox

class ListaEnlazada:
    def __init__(self):
        # prim es un _Nodo o None
        self.prim = None
        self.cant = 0

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

