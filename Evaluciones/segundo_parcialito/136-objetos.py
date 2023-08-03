"""Se quiere modelar una sesión de Google Meet junto con sus usuarios.

Para esto se pide crear una clase Usuario con los siguientes métodos:
- __init__(): Recibe el nombre y el mail del usuario. - __str__(): Devuelve una cadena indicando el nombre y
mail del usuario.
Y la clase GoogleMeet: - __init__(): Recibe al creador de la sesión. - __str__(): Devuelve una cadena representando
a los usuarios en la sesión y a los usuarios esperando a ser aceptados. - ingresar(): Recibe un usuario y lo deja en
espera para que sea aceptado. Si ya se encuentra en la sesión o en espera, levanta excepciones con mensajes
"Usuario ya se encuentra en la sesión" y "Usuario ya se encuentra en espera" respectivamente. - aceptar():
Recibe el mail de un usuario para aceptar a la sesión. Si no se encuentra en espera, levanta una excepción con
mensaje "Usuario no se encuentra en espera". - eliminar(): Recibe el mail de un usuario para eliminar de la sesión
o de espera. Si no se encuentra al usuario o se intenta eliminar al creador de la sesión, levanta una excepción con
mensajes "Usuario no encontrado" y "No se puede eliminar al creador", respectivamente.
"""
class Usuario:
    def __init__(self, nombre, mail):
        self.nombre = nombre
        self.mail = mail
    def __str__(self):
        return 'Usuario({}, {})'.format(self.nombre, self.mail)
class GoogleMeet:
    def __init__(self, creador):
        self.creador = creador
        self.usuarios = [creador]
        self.espera = []
    def __str__(self):
        return 'Usuarios: {} - Espera: {}'.format(self.usuarios, self.espera)
    def ingresar(self, usuario):
        if usuario in self.usuarios:
            raise Exception('Usuario ya se encuentra en la sesión')
        if usuario in self.espera:
            raise Exception('Usuario ya se encuentra en espera')
        self.espera.append(usuario)

    def aceptar(self, mail):
        for usuario in self.espera:
            if usuario.mail == mail:
                self.espera.remove(usuario)
                self.usuarios.append(usuario)
                return
        raise Exception('Usuario no se encuentra en espera')

    def eliminar(self, mail):
        if mail == self.creador.mail:
            raise Exception('No se puede eliminar al creador')
        for usuario in self.usuarios:
            if usuario.mail == mail:
                self.usuarios.remove(usuario)
                return
        for usuario in self.espera:
            if usuario.mail == mail:
                self.espera.remove(usuario)
                return
        raise Exception('Usuario no encontrado')